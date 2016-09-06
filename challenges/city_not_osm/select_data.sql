SELECT ST_linemerge(ST_collect(city.wkb_geometry)) AS wkb_geometry, street, boro, bikedir, ft_facilit, tf_facilit, facilitycl
FROM nyclines city, osmlines_buffer osm_buffer
WHERE NOT ST_within(city.wkb_geometry, osm_buffer.wkb_geometry)
GROUP BY street, boro, bikedir, ft_facilit, tf_facilit, facilitycl
