-- script that creates table `unique_id` on MySQL server
CREATE TABLE IF NOT EXISTS UNIQUE_ID (
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
)
