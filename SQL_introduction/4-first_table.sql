-- Command that creates a table in the current database, database name will be passed as an argument of the mysql command, script will not fail if the table exists
CREATE TABLE IF NOT EXISTS first_table (
	id INT,
	name VARCHAR(256)
);
