USE calgary_transit;

-- Preview the loaded data
SELECT *
FROM transit_stops
LIMIT 10;

-- Count the total number of transit stops
SELECT COUNT(*) AS total_stops
FROM transit_stops;

-- Count stops by status
SELECT status, COUNT(*) AS number_of_stops
FROM transit_stops
GROUP BY status;

-- View the first 10 active stops
SELECT teleride_number, stop_name
FROM transit_stops
WHERE status = 'ACTIVE'
LIMIT 10;

-- View active stops alphabetically
SELECT teleride_number, stop_name
FROM transit_stops
WHERE status = 'ACTIVE'
ORDER BY stop_name
LIMIT 10;