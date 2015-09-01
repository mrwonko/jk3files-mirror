# -*- coding: utf-8 -*-
from __future__ import print_function
import config, local_config
import os, os.path
import shutil
import json
import jinja2

entries = [ json.loads( line ) for line in open( local_config.INPUT ) if line.strip() != "" ]
entries = [ entry for entry in entries if entry["id"] not in config.BLACKLIST ]
#entriesByUrl = { entry["pageUrl"] : entry for entry in entries }
entriesById = { entry["id"]: entry for entry in entries }

keys = { key for entry in entries for key in entry.keys() }

# set successorId based on successorUrl
for entry in filter( lambda entry: "successorUrl" in entry, entries ):
    entry["successorId"] = int( entry["successorUrl"].rsplit( ";", 1 )[1] )
# some entries have broken successors; fix those
for id, successor in config.SUCCESSOR_FIXES.items():
    entriesById[id]["successorId"] = successor
# or if no fix is known, delete them
for id in config.NO_SUCCESSOR:
    del entriesById[id]["successorId"]
assert( all([entry["successorId"] in entriesById for entry in entries if "successorId" in entry]) )

# adjust category names; cache URLs; add screenshot thumbs
for entry in entries:
    entry["category"] = [ config.CATEGORY_RENAMES.get( piece, piece ) for piece in entry["category"] ]
    entry["path"] = "/".join( entry["category"] + [ str( entry["id"] ) ] )
    if "screenshots" in entry:
        entry["screenshots"] = [{"thumb": os.path.splitext( x )[0] + "_thumb" + os.path.splitext( x )[1], "full": x} for x in entry["screenshots"]]

# create search entries, which are stripped down entries
search_entries = [ {
        "id": entry[ "id" ],
        "category": "/".join( entry[ "category" ] ),
        "title": entry[ "title" ],
        "version": entry.get( "version", None ),
        "author": entry[ "author" ]
    } for entry in entries ]

# create and fill category tree

env = jinja2.Environment(
    loader = jinja2.FileSystemLoader( "templates", encoding='utf-8' )
)
category_template = env.get_template( "category.html" )
root_template = env.get_template( "root.html" )
entry_template = env.get_template( "file.html" )
search_template = env.get_template( "search.html" )

class Category:
    def __init__( self, name, parent=None ):
        self.name = name
        self.parent = parent
        self.children = {}
        self.files = []
    def insert( self, entry, category ):
        if len( category ) == 0:
            self.files.append( entry )
        else:
            if category[ 0 ] not in self.children:
                self.children[ category[ 0 ] ] = Category( category[ 0 ], self )
            self.children[ category[ 0 ] ].insert( entry, category[ 1: ] )
    def write( self, directory, parents = None ):
        # list of (path, name) parent pairs
        parents = parents or []

        # write category file
        if not os.path.isdir( directory ):
            os.makedirs( directory )
        with open( os.path.join( directory, "index.html" ), "wb" ) as index:
            template = category_template if self.parent else root_template
            html = template.render(
                name = self.name,
                parents = parents,
                children = self.children,
                entries = self.files,
                root = parents[ 0 ][ 0 ] if parents else "."
                )
            index.write( html.encode( "utf-8" ) )

        # write subcategories
        parents = [ ("../" + path, name) for (path, name) in parents ] + [ ( "..", self.name ) ]
        for child in self.children.values():
            child.write( os.path.join( directory, child.name ), parents )
            if local_config.BREAK_EARLY:
                break
        # write entries
        myname = "/".join( [ name for (path, name) in parents ] )
        for entry in self.files:
            entry_dir = os.path.join( directory, str( entry["id"] ) )
            if not os.path.isdir( entry_dir ):
                os.makedirs( entry_dir )
            with open( os.path.join( entry_dir, "index.html" ), "wb" ) as index:
                html = entry_template.render(
                    entry = entry,
                    parents = parents,
                    root = parents[0][0],
                    successor = entriesById[ entry[ "successorId" ] ] if "successorId" in entry else None,
                    screenshot_dir = parents[0][0] + "/" + local_config.SCREENSHOTS if local_config.SCREENSHOTS_RELATIVE else local_config.SCREENSHOTS,
                    files_dir = parents[0][0] + "/" + local_config.FILES if local_config.FILES_RELATIVE else local_config.FILES
                    )
                index.write( html.encode( "utf-8" ) )
            #print( "/".join( [ myname, entry["title"] ] ) )
            if local_config.BREAK_EARLY:
                break
        print( myname + "/" )

root = Category( u"jk3files mirror" )
for entry in entries:
    root.insert( entry, entry["category"] )

root.write( local_config.OUTPUT_DIR )
with open( os.path.join( local_config.OUTPUT_DIR, "search.html" ), "wb" ) as search:
    html = search_template.render(
        root = "."
        )
    search.write( html.encode( "utf-8" ) )
with open( os.path.join( local_config.OUTPUT_DIR, "entries.json" ), "wb" ) as json_file:
    json.dump( search_entries, json_file )
# copy fontawesome files
for folder in [ "css", "fonts" ]:
    shutil.rmtree( os.path.join( local_config.OUTPUT_DIR, folder ), True )
    shutil.copytree( os.path.join( "fontawesome", folder ), os.path.join( local_config.OUTPUT_DIR, folder ) )
# copy bootstrap files
for name in [ "bootstrap.min.css", "bootstrap-theme.min.css" ]:
    shutil.copy( os.path.join( "bootstrap", name ), os.path.join( local_config.OUTPUT_DIR, "css", name ) )
# copy scripts
for name in [ "angular.min.js", "lodash.min.js", "search.js" ]:
    shutil.copy( os.path.join( "js", name ), os.path.join( local_config.OUTPUT_DIR, name ) )