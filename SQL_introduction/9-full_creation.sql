-- Script that creates a table as it is given in the required database with multiple rows, it wont fail if the table exists name will be passes as an argument in the command
CREATE TABLE IF NOT EXISTS second_table (
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(256),
	score INT
);

-- Inserting rows as required
INSERT INTO second_table
VALUES ("John", 10),
("Alex", 3)
("Bob", 14)
("George", 8);
