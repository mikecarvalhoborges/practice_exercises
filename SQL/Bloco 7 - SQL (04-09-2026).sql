#1
SELECT 
  trip_id,
  duration_minutes,
  ROUND(duration_minutes / 60, 2) AS duracao_horas
FROM `bigquery-public-data.austin_bikeshare.bikeshare_trips`;

#2
SELECT 
  COUNT(DISTINCT start_station_name)
FROM `bigquery-public-data.austin_bikeshare.bikeshare_trips`;

#3
SELECT 
  CASE 
    WHEN duration_minutes < 15 THEN "curta"
    WHEN duration_minutes BETWEEN 15 AND 60 THEN "média"
    ELSE "longa"
  END AS faixa_duracao
FROM `bigquery-public-data.austin_bikeshare.bikeshare_trips`;

#4
SELECT 
  start_station_name,
  COUNT(trip_id) AS total_viagens,
  ROUND(AVG(duration_minutes), 2) AS duracao_media
FROM `bigquery-public-data.austin_bikeshare.bikeshare_trips`
WHERE start_station_name LIKE '%Congress%'
GROUP BY start_station_name;

#5
SELECT 
  EXTRACT(YEAR FROM start_time) AS ano_viagem,
  COUNT(EXTRACT(YEAR FROM start_time)) AS total_viagens_ano,
FROM `bigquery-public-data.austin_bikeshare.bikeshare_trips`
GROUP BY ano_viagem
ORDER BY ano_viagem ASC;

#6
SELECT 
  DISTINCT TRIM(start_station_name) AS estacoes,
FROM `bigquery-public-data.austin_bikeshare.bikeshare_trips`
WHERE duration_minutes < 500 OR duration_minutes = 0;

#7
SELECT 
  start_station_name,
  end_station_name,
  COUNT(*) AS total_viagens
FROM `bigquery-public-data.austin_bikeshare.bikeshare_trips`
GROUP BY start_station_name, end_station_name
ORDER BY total_viagens DESC
LIMIT 10;

#8
SELECT 
  start_station_name,
  ROUND(AVG(duration_minutes), 2) AS maior_duracao_media
FROM `bigquery-public-data.austin_bikeshare.bikeshare_trips`
GROUP BY start_station_name
ORDER BY maior_duracao_media DESC
LIMIT 1;

#9
SELECT 
  trip_id, 
  duration_minutes,
  start_station_name,
FROM `bigquery-public-data.austin_bikeshare.bikeshare_trips`
WHERE start_station_name NOT IN ('Riverside @ S. Lamar', '2nd & Congress')
GROUP BY trip_id, duration_minutes, start_station_name;

#10
SELECT 
  start_station_name,
  COUNT(trip_id) AS total_viagens,
  ROUND(AVG(duration_minutes), 1) AS duracao_media,
  CASE 
    WHEN COUNT(trip_id) > 500 THEN "movimentada"
    ELSE "pouco movimentada"
  END AS classificacao_estacao  
FROM `bigquery-public-data.austin_bikeshare.bikeshare_trips`
GROUP BY start_station_name
HAVING COUNT(trip_id) > 50
ORDER BY total_viagens DESC;