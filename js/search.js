"use strict";

angular.module( 'lodash', [] )
.factory( '_', function( $window ) {
    var _ = $window._;
    delete( $window._ );
    return _;
} )
.run( function( _ ) {
    // force factory to be run at bootstrap, removing global _ variable
} )
;

angular.module( 'search', [ 'lodash' ] )
.controller( 'SearchCtrl', function( $scope, $http ) {
    $scope.limit = 100;
    $scope.loading = true;
    $scope.filter = {};
    
    $scope.sortBy = "id";
    $scope.reverseOrder = false;
    function mkSortBy( key ) {
        return function() {
            if( $scope.sortBy == key ) {
                $scope.reverseOrder = !$scope.reverseOrder;
            } else {
                $scope.reverseOrder = false;
                $scope.sortBy = key;
            }
        }
    }
    $scope.orderString = function() {
        return $scope.reverseOrder ? "desc" : "asc";
    };
    $scope.sortByID = mkSortBy( "id" );
    $scope.sortByCategory = mkSortBy( "category" );
    $scope.sortByTitle = mkSortBy( "title" );
    $scope.sortByAuthor = mkSortBy( "author" );
    
    $http.get( "entries.json" ).then( function( response ) {
        $scope.loading = false;
        $scope.entries = response.data;
    }, function( response ) {
        $scope.error = response.status + ": " + response.statusText;
        $scope.loading = false;
    } );
} )
.filter( 'filterAndSort', function( _, $log ) {
    var sortKeys = {
        "id": [ "id" ],
        "category": [ "category", "title", "version" ],
        "title": [ "title", "version" ],
        "author": [ "author", "title", "version" ]
    };
    
    function containsNoCase( haystack, needle ) {
        return haystack.toLocaleLowerCase().indexOf( needle.toLocaleLowerCase() ) > -1;
    }
    
    return function( entries, filter, sortBy, reverse ) {
        var keys = sortKeys[ sortBy ];
        return _(entries)
            .filter( function( entry ) {
                if( filter.id && entry.id != filter.id ) {
                    return false;
                }
                if( filter.category && !containsNoCase( entry.category, filter.category ) ) {
                    return false;
                }
                if( filter.title && !containsNoCase( entry.title, filter.title ) ) {
                    return false;
                }
                if( filter.author && !containsNoCase( entry.author, filter.author ) ) {
                    return false;
                }
                return true;
            } )
            .sort( function( a, b ) {
                var i, key;
                for( i = 0; i < keys.length; ++i ) {
                    key = keys[ i ];
                    if( a[ key ] < b[ key ] ) {
                        return reverse ? 1 : -1;
                    } else if( a[ key ] > b[ key ] ) {
                        return reverse ? -1 : 1;
                    }
                }
                return 0;
            } )
            .value();
    }
} )
;

