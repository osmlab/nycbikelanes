nycbikelanes
============

Coordination for the [NYC bike lane cleanup and
update](http://wiki.openstreetmap.org/wiki/New_York,_New_York/Bike_Lanes_and_Roads_Cleanup).
We plan on creating [MapRoulette](http://maproulette.org/)
[challenges](https://gist.github.com/mvexel/b5ad1cb0c91ac245ea3f) to update
OSM's bike lane data using the latest data available from the city.


Data
----

The simplest way to get going is to clone this repository, `cd` into it and run:

    make

This will download all the relevant data and process it, then create challenge
data.

The data is in two shapefiles: `data/nyclines.shp` and `data/osmlines.shp`. The
data was created using the `Makefile`.

The `Makefile` contains recipes for downloading an OSM extract for NYC.
It clips to NYC borders (not just the bounding box) and attempts to select just
the features that are bicycle-related. Run the following to get OSM data:

    make boroughs osm_bikelanes

You'll need [osmtogeojson](https://github.com/tyrasd/osmtogeojson) to run the 
above recipe, you can install it with npm:

    npm install -g osmtogeojson

The city's latest bike lane data is in `data/cscl_bike_routes/original`. This
data is not available online, otherwise we would download it from there. We have
reprojected and simplified it, and you can do the same with:

    make nyc_bikelanes


Collaborators
-------------

* [Eric Brelsford](https://github.com/ebrelsford)
* [Colin Reilly](https://github.com/colinreilly)
* [Chris Henrick](https://github.com/clhenrick)
