-- Script that lists all records of the table given of the database required, with specified rows and datas
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
