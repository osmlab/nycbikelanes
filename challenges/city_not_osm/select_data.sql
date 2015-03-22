SELECT nyclines.*
FROM nyclines, osmlines_buffer
WHERE NOT ST_within(nyclines.wkb_geometry, osmlines_buffer.wkb_geometry)
