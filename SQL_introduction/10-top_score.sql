-- Script that lists all records of the table required of the database required in the server, it will display all the data inside the structure, ordered from a specific row, database name will be passed as an argument
SELECT score, name
FROM second_table
ORDERED BY score DESC;
