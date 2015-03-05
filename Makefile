datadir = data
bicyclewhere = "highway='cycleway' or (bicycle is not null and bicycle != 'no')"

clean_boroughs:
	rm -rf data/boroughs data/nybbwi_14d data/boroughs.zip

boroughs: clean_boroughs
	mkdir -p data
	mkdir -p data/boroughs
	
	@echo "Downloading boroughs..."
	curl -L "https://data.cityofnewyork.us/api/geospatial/tv64-9x69?method=export&format=Shapefile" -o data/boroughs/boroughs.zip
	unzip data/boroughs/boroughs.zip -d data/boroughs/
	
	@echo "Dissolving boroughs"
	ogr2ogr -simplify 0.2 -t_srs EPSG:4326 -overwrite data/boroughs/dissolved.shp data/boroughs/nybbwi_14d/nybbwi.shp -dialect sqlite -sql "select ST_union(ST_buffer(Geometry,0.001)) from nybbwi"

clean_osm:
	rm -rf $(datadir)/osmlines.*
	rm -rf $(datadir)/osm.zip

osm_bikelanes: clean_osm
	mkdir -p $(datadir)
	@echo "Downloading OSM data..."
	curl -L "https://s3.amazonaws.com/metro-extracts.mapzen.com/new-york_new-york.osm2pgsql-shapefiles.zip" -o $(datadir)/osm.zip
	unzip $(datadir)/osm.zip -d $(datadir)
	
	@echo "Filtering and clipping"
	ogr2ogr -clipsrc data/boroughs/dissolved.shp -t_srs EPSG:4326 $(datadir)/osmlines.shp $(datadir)/*line.shp -where $(bicyclewhere)
	
	@echo "Deleting original files"
	rm $(datadir)/new-york_new-york.osm-*

nyc_bikelanes:
	rm -f $(datadir)/nyclines.*
	ogr2ogr -simplify 0.2 -t_srs EPSG:4326 $(datadir)/nyclines.shp $(datadir)/cscl_bike_routes/original/CSCL_BikeRoute.shp

osm_pgsql:
	ogr2ogr -skipfailures -overwrite -f PostgreSQL PG:"dbname='nycbikelanes' user='nycbikelanes'" $(datadir)/osmlines.shp -nln osmlines

nyc_pgsql:
	ogr2ogr -skipfailures -overwrite -f PostgreSQL PG:"dbname='nycbikelanes' user='nycbikelanes'" $(datadir)/nyclines.shp -nln nyclines
