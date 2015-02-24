-- select all lines from city data that don't intersect with osm data in CartoDB
SELECT a.* FROM cscl_bike_routes AS a 
LEFT JOIN
osm_bike_lines AS b ON
St_Intersects(a.the_geom, b.the_geom)
WHERE b.cartodb_id IS NULL;

-- buffer osm lines prior to doing intersection
-- too slow, better to create buffer first as a separate table
-- and to use EPSG:2263 for calculating distance
SELECT a.* FROM cscl_bike_routes_not_simp AS a 
LEFT JOIN
  (
    SELECT cartodb_id, the_geom, 
    ST_Buffer(the_geom_webmercator, 5) as the_geom_webmercator 
    FROM osm_bike_lines
  ) AS b ON
St_Intersects(a.the_geom,b.the_geom)
WHERE b.cartodb_id IS NULL

-- create a new table from this query in CartoDB
SELECT cartodb_id, the_geom, 
ST_Buffer(the_geom_webmercator, 5) as the_geom_webmercator 
FROM osm_bike_lines