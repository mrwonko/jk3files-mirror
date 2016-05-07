# some files have broken successors
SUCCESSOR_FIXES = {
    9180: 9220, # FFAMod (1.0) -> FFAMod (1.02)
    19448: 21714, # Goku -> Goku 2.0
    21503: 25915, # Big Boss (2.0) -> Big Boss (v3)
    63223: 76493, # Clan Mod (v1.0) -> Clan Mod (v1.08)
    69308: 73386 # Recolor of Major Kusanagi -> Recolor of 'Major Kusanagi' (v2)
}
NO_SUCCESSOR = [
    4294, # JediMod++ (v3.0) - I have no idea what the successor of that is
    9220 # FFAMod (1.02) - doesn't appear to have a successor?
]

# IDs to omit per the author's request or similar
BLACKLIST = [
    # files by afiNity
    66973, 71666, 71893, 73127, 74141, 74579, 86817, 104039, 117522,
    # The Arena of Ankor per request of Cody Small
    69132,
    # SiLink's readmes contain his mail, which he doesn't want online; editing the readme during processing would be a PITA, so they're simply blacklisted.
    89294, 90878, 95303,
    # Luciel's files
    91030, 92067, 87693, 87884, 87918, 92110, 89229, 91063, 59308, 92080, 90922, 89548, 91030,
]

# categories to rename
CATEGORY_RENAMES = {
    u"Jedi Knight 2: Jedi Outcast Downloads": u"Jedi Outcast",
    u"Jedi Knight 3: Jedi Academy Downloads": u"Jedi Academy"
}
