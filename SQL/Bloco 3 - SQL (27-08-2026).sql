# Exercício 3.1 — GROUP BY
SELECT 
  start_station_name,
  COUNT(trip_id) AS total_viagens,
  AVG(duration_minutes) AS media_duracao
FROM `bigquery-public-data.austin_bikeshare.bikeshare_trips` 
GROUP BY start_station_name
ORDER BY total_viagens DESC
LIMIT 10;

# Exercício 3.2 — Subquery simples
SELECT 
  trip_id,
  duration_minutes
FROM `bigquery-public-data.austin_bikeshare.bikeshare_trips` 
WHERE duration_minutes > (
  SELECT
    AVG(duration_minutes)
  FROM `bigquery-public-data.austin_bikeshare.bikeshare_trips` 
)
ORDER BY duration_minutes ASC