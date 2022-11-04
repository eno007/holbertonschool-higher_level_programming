-- Script that displays the average temperature by city ordered by temperature
SE4LECT city, AVG(value)
AS avg_temperature
FROM temperatures
GROUP BY city
ORDER BY avg_temperatures DESC;
