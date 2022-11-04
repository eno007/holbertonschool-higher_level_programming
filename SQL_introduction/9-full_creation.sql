-- Script that creates a table as it is given in the required database with multiple rows, it wont fail if the table exists name will be passes as an argument in the command
CREATE TABLE IF NOT EXISTS second_table (
	id INT,
	name VARCHAR(256),
	score INT
);

-- Inserting rows as required
INSERT INTO second_table
VALUES (1, "John", 10),
(2, "Alex", 3)
(3, "Bob", 14)
(4, "George", 8);
