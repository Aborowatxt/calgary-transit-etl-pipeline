-- Create the Calgary Transit stops table
CREATE TABLE IF NOT EXISTS transit_stops (
    teleride_number BIGINT PRIMARY KEY,
    stop_name VARCHAR(255) NOT NULL,
    status VARCHAR(20) NOT NULL,
    longitude DOUBLE NOT NULL,
    latitude DOUBLE NOT NULL
);
