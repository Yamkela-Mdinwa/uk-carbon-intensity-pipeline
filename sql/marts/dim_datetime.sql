CREATE TABLE IF NOT EXISTS marts.dim_datetime (
    datetime_id SERIAL PRIMARY KEY,
    datetime_utc TIMESTAMPTZ NOT NULL UNIQUE,
    date DATE NOT NULL,
    hour INTEGER NOT NULL,
    minute INTEGER NOT NULL,
    day INTEGER NOT NULL,
    month INTEGER NOT NULL,
    year INTEGER NOT NULL
);

