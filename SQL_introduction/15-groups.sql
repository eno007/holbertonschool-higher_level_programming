-- Script that lists the number of the records with the same score in the table given of the database given, it will deisplasy a specific field and the number of the records for that row with the label given
SELECT score, COUNT(score) AS "number"
FROM second_table
GROUP BY score
ORDER BY number DESC;
