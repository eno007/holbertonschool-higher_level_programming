-- Script that converts specific database to UTF8
ALTER DATABASE hbtn_0c_0
CHARACTER SET = utf8mb4
COLLATE utf8mb4_unicode_ci;

--Code that converts the table
ALTER TABLE hbtn_0c_0.first_table
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
