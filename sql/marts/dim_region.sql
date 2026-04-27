CREATE TABLE marts.dim_region (
    region_id SERIAL PRIMARY KEY,
    region_name TEXT UNIQUE
);
