CREATE TABLE IF NOT EXISTS marts.dim_measure_type (
	measure_type_id SERIAL PRIMARY KEY,
	measure_type VARCHAR(20) NOT NULL UNIQUE
);
