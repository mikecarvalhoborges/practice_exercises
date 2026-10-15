#1
SELECT 
  trip_id, 
  start_time, 
  duration_minutes
FROM `bigquery-public-data.austin_bikeshare.bikeshare_trips` 
ORDER BY start_time DESC
LIMIT 20;

#2
SELECT 
  trip_id, 
  duration_minutes
FROM `bigquery-public-data.austin_bikeshare.bikeshare_trips` 
WHERE duration_minutes BETWEEN 5 and 20;

#3
SELECT 
  COUNT(trip_id)
FROM `bigquery-public-data.austin_bikeshare.bikeshare_trips` 
WHERE duration_minutes = 0;

#4
SELECT 
  start_station_name,
  MAX(duration_minutes) AS duracao_maxima
FROM `bigquery-public-data.austin_bikeshare.bikeshare_trips` 
GROUP BY start_station_name;

#5
SELECT 
  start_station_name,
  AVG(duration_minutes) AS media_duracao
FROM `bigquery-public-data.austin_bikeshare.bikeshare_trips` 
GROUP BY start_station_name
ORDER BY media_duracao ASC
LIMIT 5;

#6
SELECT 
  trip_id
FROM `bigquery-public-data.austin_bikeshare.bikeshare_trips` 
WHERE end_station_name != start_station_name;

#7
SELECT 
  COUNT(trip_id) AS total_viagens,
  bike_id
FROM `bigquery-public-data.austin_bikeshare.bikeshare_trips` 
GROUP BY bike_id
ORDER BY total_viagens DESC
LIMIT 10;

#8
SELECT 
  trip_id, 
  duration_minutes
FROM `bigquery-public-data.austin_bikeshare.bikeshare_trips` 
WHERE duration_minutes < (
  SELECT
    AVG(duration_minutes)
  FROM `bigquery-public-data.austin_bikeshare.bikeshare_trips` 
);

#9
SELECT 
  start_station_name, 
  COUNT(trip_id) AS total_viagens,
  AVG(duration_minutes) AS media_duracao
FROM `bigquery-public-data.austin_bikeshare.bikeshare_trips` 
GROUP BY start_station_name
HAVING total_viagens > 100;

#10
SELECT 
  COUNT(trip_id) AS total_viagens,
  AVG(duration_minutes) AS media_duracao
FROM `bigquery-public-data.austin_bikeshare.bikeshare_trips` 
WHERE duration_minutes > 0;