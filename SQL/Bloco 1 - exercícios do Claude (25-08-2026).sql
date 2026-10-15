# Exercício 1.1 — SELECT e LIMIT

SELECT 
  * 
FROM `bigquery-public-data.austin_bikeshare.bikeshare_trips` 
LIMIT 10;

# Exercício 1.2 — Selecionando colunas específicas

SELECT 
  trip_id,
  duration_minutes,
  start_station_name
FROM `bigquery-public-data.austin_bikeshare.bikeshare_trips` 
LIMIT 15;

# Exercício 1.3 — Filtro com WHERE

SELECT 
  trip_id,
  duration_minutes
FROM `bigquery-public-data.austin_bikeshare.bikeshare_trips` 
WHERE duration_minutes > 60