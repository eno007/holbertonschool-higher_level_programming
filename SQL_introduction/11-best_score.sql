-- Script that lists all the records with a specific data from a selected table on the required database, it will show all the required and specified datas, will be ordered by a specific row
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
