CREATE DATABASE my_rag_project1;
SHOW DATABASES;
USE my_rag_project1;

SHOW TABLES;

CREATE TABLE universities (
    university_id INT PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL,
    country VARCHAR(100) NOT NULL
);


CREATE TABLE cities (
    city_id INT PRIMARY KEY AUTO_INCREMENT,
    city_name VARCHAR(100) UNIQUE NOT NULL,
    country VARCHAR(100) NOT NULL
);


CREATE TABLE best_student_cities (
    city_rank INT PRIMARY KEY,
    city_id INT NOT NULL,
    overall_score FLOAT,
    student_view FLOAT,
    employer_activity FLOAT,
    affordability FLOAT,
    FOREIGN KEY (city_id) REFERENCES cities(city_id)
);


CREATE TABLE qs_ranking_details (
    university_id INT PRIMARY KEY,
    overall_score DECIMAL(5,2),
    academic_reputation DECIMAL(5,2),
    employer_reputation DECIMAL(5,2),
    faculty_student_ratio DECIMAL(5,2),
    citations_per_faculty DECIMAL(5,2),
    international_faculty_ratio DECIMAL(5,2),
    international_student_ratio DECIMAL(5,2),
    FOREIGN KEY (university_id) REFERENCES universities(university_id)
);


CREATE TABLE employability_rankings (
    university_id INT PRIMARY KEY,
    employability_rank INT,
    FOREIGN KEY (university_id) REFERENCES universities(university_id)
);


CREATE TABLE subjects (
    subject_id INT PRIMARY KEY,
    subject_name VARCHAR(255) UNIQUE NOT NULL
);


CREATE TABLE subject_rankings (
    id INT PRIMARY KEY AUTO_INCREMENT,
    subject_id INT NOT NULL,
    university_id INT NOT NULL,
    global_rank INT,
    country_rank INT,
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id),
    FOREIGN KEY (university_id) REFERENCES universities(university_id)
);



ALTER TABLE universities
ADD COLUMN global_rank INT;

ALTER TABLE universities
DROP COLUMN global_rank;

ALTER TABLE universities
ADD COLUMN rank_min INT,
ADD COLUMN rank_max INT;


SELECT * FROM universities;

SELECT COUNT(*) FROM universities;
SELECT * FROM cities;
SELECT * FROM qs_ranking_details;

ALTER TABLE qs_ranking_details 
MODIFY COLUMN overall_score FLOAT,
MODIFY COLUMN academic_reputation FLOAT,
MODIFY COLUMN employer_reputation FLOAT,
MODIFY COLUMN faculty_student_ratio FLOAT,
MODIFY COLUMN citations_per_faculty FLOAT;

CREATE TABLE countries (
    country_id INT PRIMARY KEY AUTO_INCREMENT,
    country_name VARCHAR(100) UNIQUE NOT NULL
);

SELECT * FROM countries;

ALTER TABLE universities ADD COLUMN country_id INT;
ALTER TABLE employability_rankings ADD COLUMN country_id INT;


ALTER TABLE universities ADD FOREIGN KEY (country_id) REFERENCES countries(country_id);
ALTER TABLE employability_rankings ADD FOREIGN KEY (country_id) REFERENCES countries(country_id);

ALTER TABLE cities ADD COLUMN country_id INT;
ALTER TABLE cities 
ADD FOREIGN KEY (country_id) REFERENCES countries(country_id) ON DELETE CASCADE;

DESC universities;

ALTER TABLE universities ADD COLUMN country_id INT;
ALTER TABLE universities 
ADD FOREIGN KEY (country_id) REFERENCES countries(country_id) ON DELETE CASCADE;

SELECT * FROM universities;

DESC cities;
SELECT * FROM cities;

SELECT * FROM countries;

DELETE FROM countries WHERE country_id = 108;

SELECT city_id, city_name, country, country_id 
FROM cities 
WHERE country = 'Turkey' OR country_id = 46;

DROP TABLE best_student_cities;

DROP TABLE IF EXISTS cities;

CREATE TABLE cities (
    city_id INT PRIMARY KEY AUTO_INCREMENT,
    city_name VARCHAR(100) NOT NULL,
    country_id INT NOT NULL,
    country VARCHAR(100) NOT NULL,
    FOREIGN KEY (country_id) REFERENCES countries(country_id) ON DELETE CASCADE
);

SELECT * FROM cities;
SHOW TABLES;
DESC universities;
DESC cities;
DESC best_student_cities;
DESC qs_ranking_details;

SELECT TABLE_NAME, COLUMN_NAME, CONSTRAINT_NAME, REFERENCED_TABLE_NAME 
FROM information_schema.KEY_COLUMN_USAGE 
WHERE TABLE_NAME = 'cities';

SELECT TABLE_NAME, COLUMN_NAME, CONSTRAINT_NAME, REFERENCED_TABLE_NAME 
FROM information_schema.KEY_COLUMN_USAGE 
WHERE TABLE_NAME = 'universities';

SELECT TABLE_NAME, COLUMN_NAME, CONSTRAINT_NAME, REFERENCED_TABLE_NAME 
FROM information_schema.KEY_COLUMN_USAGE 
WHERE TABLE_NAME = 'best_student_cities';

SELECT u.university_id, u.name, u.country_id, c.country_name
FROM universities u
JOIN countries c ON u.country_id = c.country_id
LIMIT 10;

SELECT * FROM subjects;
SELECT * FROM subject_rankings;
SELECT COUNT(*) FROM subject_rankings;

DROP TABLE employability_rankings;


CREATE TABLE employability_rankings (
    university_id INT PRIMARY KEY,
    employability_rank INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (university_id) REFERENCES universities(university_id) ON DELETE CASCADE
);
SELECT * FROM employability_rankings;
SELECT COUNT(*) FROM employability_rankings;

DROP TABLE best_student_cities;
DROP TABLE IF EXISTS cities;
-- 先不放入city資訊

CREATE DATABASE my_rag_project1;
SHOW DATABASES;
USE my_rag_project1;

SHOW TABLES;

CREATE TABLE universities (
    university_id INT PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL,
    country VARCHAR(100) NOT NULL
);


CREATE TABLE cities (
    city_id INT PRIMARY KEY AUTO_INCREMENT,
    city_name VARCHAR(100) UNIQUE NOT NULL,
    country VARCHAR(100) NOT NULL
);


CREATE TABLE best_student_cities (
    city_rank INT PRIMARY KEY,
    city_id INT NOT NULL,
    overall_score FLOAT,
    student_view FLOAT,
    employer_activity FLOAT,
    affordability FLOAT,
    FOREIGN KEY (city_id) REFERENCES cities(city_id)
);


CREATE TABLE qs_ranking_details (
    university_id INT PRIMARY KEY,
    overall_score DECIMAL(5,2),
    academic_reputation DECIMAL(5,2),
    employer_reputation DECIMAL(5,2),
    faculty_student_ratio DECIMAL(5,2),
    citations_per_faculty DECIMAL(5,2),
    international_faculty_ratio DECIMAL(5,2),
    international_student_ratio DECIMAL(5,2),
    FOREIGN KEY (university_id) REFERENCES universities(university_id)
);


CREATE TABLE employability_rankings (
    university_id INT PRIMARY KEY,
    employability_rank INT,
    FOREIGN KEY (university_id) REFERENCES universities(university_id)
);


CREATE TABLE subjects (
    subject_id INT PRIMARY KEY,
    subject_name VARCHAR(255) UNIQUE NOT NULL
);


CREATE TABLE subject_rankings (
    id INT PRIMARY KEY AUTO_INCREMENT,
    subject_id INT NOT NULL,
    university_id INT NOT NULL,
    global_rank INT,
    country_rank INT,
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id),
    FOREIGN KEY (university_id) REFERENCES universities(university_id)
);



ALTER TABLE universities
ADD COLUMN global_rank INT;

ALTER TABLE universities
DROP COLUMN global_rank;

ALTER TABLE universities
ADD COLUMN rank_min INT,
ADD COLUMN rank_max INT;


SELECT * FROM universities;

SELECT COUNT(*) FROM universities;
SELECT * FROM cities;
SELECT * FROM qs_ranking_details;

ALTER TABLE qs_ranking_details 
MODIFY COLUMN overall_score FLOAT,
MODIFY COLUMN academic_reputation FLOAT,
MODIFY COLUMN employer_reputation FLOAT,
MODIFY COLUMN faculty_student_ratio FLOAT,
MODIFY COLUMN citations_per_faculty FLOAT;

CREATE TABLE countries (
    country_id INT PRIMARY KEY AUTO_INCREMENT,
    country_name VARCHAR(100) UNIQUE NOT NULL
);

SELECT * FROM countries;

ALTER TABLE universities ADD COLUMN country_id INT;
ALTER TABLE employability_rankings ADD COLUMN country_id INT;


ALTER TABLE universities ADD FOREIGN KEY (country_id) REFERENCES countries(country_id);
ALTER TABLE employability_rankings ADD FOREIGN KEY (country_id) REFERENCES countries(country_id);

ALTER TABLE cities ADD COLUMN country_id INT;
ALTER TABLE cities 
ADD FOREIGN KEY (country_id) REFERENCES countries(country_id) ON DELETE CASCADE;

DESC universities;

ALTER TABLE universities ADD COLUMN country_id INT;
ALTER TABLE universities 
ADD FOREIGN KEY (country_id) REFERENCES countries(country_id) ON DELETE CASCADE;

SELECT * FROM universities;

DESC cities;
SELECT * FROM cities;

SELECT * FROM countries;

DELETE FROM countries WHERE country_id = 108;

SELECT city_id, city_name, country, country_id 
FROM cities 
WHERE country = 'Turkey' OR country_id = 46;

DROP TABLE best_student_cities;

DROP TABLE IF EXISTS cities;

CREATE TABLE cities (
    city_id INT PRIMARY KEY AUTO_INCREMENT,
    city_name VARCHAR(100) NOT NULL,
    country_id INT NOT NULL,
    country VARCHAR(100) NOT NULL,
    FOREIGN KEY (country_id) REFERENCES countries(country_id) ON DELETE CASCADE
);

SELECT * FROM cities;
SHOW TABLES;
DESC universities;
DESC cities;
DESC best_student_cities;
DESC qs_ranking_details;

SELECT TABLE_NAME, COLUMN_NAME, CONSTRAINT_NAME, REFERENCED_TABLE_NAME 
FROM information_schema.KEY_COLUMN_USAGE 
WHERE TABLE_NAME = 'cities';

SELECT TABLE_NAME, COLUMN_NAME, CONSTRAINT_NAME, REFERENCED_TABLE_NAME 
FROM information_schema.KEY_COLUMN_USAGE 
WHERE TABLE_NAME = 'universities';

SELECT TABLE_NAME, COLUMN_NAME, CONSTRAINT_NAME, REFERENCED_TABLE_NAME 
FROM information_schema.KEY_COLUMN_USAGE 
WHERE TABLE_NAME = 'best_student_cities';

SELECT u.university_id, u.name, u.country_id, c.country_name
FROM universities u
JOIN countries c ON u.country_id = c.country_id
LIMIT 10;

SELECT * FROM subjects;
SELECT * FROM subject_rankings;
SELECT COUNT(*) FROM subject_rankings;

DROP TABLE employability_rankings;


CREATE TABLE employability_rankings (
    university_id INT PRIMARY KEY,
    employability_rank INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (university_id) REFERENCES universities(university_id) ON DELETE CASCADE
);
SELECT * FROM employability_rankings;
SELECT COUNT(*) FROM employability_rankings;

DROP TABLE best_student_cities;
DROP TABLE IF EXISTS cities;
-- 先不放入city資訊



CREATE DATABASE my_rag_project1;
SHOW DATABASES;
USE my_rag_project1;

SHOW TABLES;

CREATE TABLE universities (
    university_id INT PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL,
    country VARCHAR(100) NOT NULL
);


CREATE TABLE cities (
    city_id INT PRIMARY KEY AUTO_INCREMENT,
    city_name VARCHAR(100) UNIQUE NOT NULL,
    country VARCHAR(100) NOT NULL
);


CREATE TABLE best_student_cities (
    city_rank INT PRIMARY KEY,
    city_id INT NOT NULL,
    overall_score FLOAT,
    student_view FLOAT,
    employer_activity FLOAT,
    affordability FLOAT,
    FOREIGN KEY (city_id) REFERENCES cities(city_id)
);


CREATE TABLE qs_ranking_details (
    university_id INT PRIMARY KEY,
    overall_score DECIMAL(5,2),
    academic_reputation DECIMAL(5,2),
    employer_reputation DECIMAL(5,2),
    faculty_student_ratio DECIMAL(5,2),
    citations_per_faculty DECIMAL(5,2),
    international_faculty_ratio DECIMAL(5,2),
    international_student_ratio DECIMAL(5,2),
    FOREIGN KEY (university_id) REFERENCES universities(university_id)
);


CREATE TABLE employability_rankings (
    university_id INT PRIMARY KEY,
    employability_rank INT,
    FOREIGN KEY (university_id) REFERENCES universities(university_id)
);


CREATE TABLE subjects (
    subject_id INT PRIMARY KEY,
    subject_name VARCHAR(255) UNIQUE NOT NULL
);


CREATE TABLE subject_rankings (
    id INT PRIMARY KEY AUTO_INCREMENT,
    subject_id INT NOT NULL,
    university_id INT NOT NULL,
    global_rank INT,
    country_rank INT,
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id),
    FOREIGN KEY (university_id) REFERENCES universities(university_id)
);



ALTER TABLE universities
ADD COLUMN global_rank INT;

ALTER TABLE universities
DROP COLUMN global_rank;

ALTER TABLE universities
ADD COLUMN rank_min INT,
ADD COLUMN rank_max INT;


SELECT * FROM universities;

SELECT COUNT(*) FROM universities;
SELECT * FROM cities;
SELECT * FROM qs_ranking_details;

ALTER TABLE qs_ranking_details 
MODIFY COLUMN overall_score FLOAT,
MODIFY COLUMN academic_reputation FLOAT,
MODIFY COLUMN employer_reputation FLOAT,
MODIFY COLUMN faculty_student_ratio FLOAT,
MODIFY COLUMN citations_per_faculty FLOAT;

CREATE TABLE countries (
    country_id INT PRIMARY KEY AUTO_INCREMENT,
    country_name VARCHAR(100) UNIQUE NOT NULL
);

SELECT * FROM countries;

ALTER TABLE universities ADD COLUMN country_id INT;
ALTER TABLE employability_rankings ADD COLUMN country_id INT;


ALTER TABLE universities ADD FOREIGN KEY (country_id) REFERENCES countries(country_id);
ALTER TABLE employability_rankings ADD FOREIGN KEY (country_id) REFERENCES countries(country_id);

ALTER TABLE cities ADD COLUMN country_id INT;
ALTER TABLE cities 
ADD FOREIGN KEY (country_id) REFERENCES countries(country_id) ON DELETE CASCADE;

DESC universities;

ALTER TABLE universities ADD COLUMN country_id INT;
ALTER TABLE universities 
ADD FOREIGN KEY (country_id) REFERENCES countries(country_id) ON DELETE CASCADE;

SELECT * FROM universities;

DESC cities;
SELECT * FROM cities;

SELECT * FROM countries;

DELETE FROM countries WHERE country_id = 108;

SELECT city_id, city_name, country, country_id 
FROM cities 
WHERE country = 'Turkey' OR country_id = 46;

DROP TABLE best_student_cities;

DROP TABLE IF EXISTS cities;

CREATE TABLE cities (
    city_id INT PRIMARY KEY AUTO_INCREMENT,
    city_name VARCHAR(100) NOT NULL,
    country_id INT NOT NULL,
    country VARCHAR(100) NOT NULL,
    FOREIGN KEY (country_id) REFERENCES countries(country_id) ON DELETE CASCADE
);

SELECT * FROM cities;
SHOW TABLES;
DESC universities;
DESC cities;
DESC best_student_cities;
DESC qs_ranking_details;

SELECT TABLE_NAME, COLUMN_NAME, CONSTRAINT_NAME, REFERENCED_TABLE_NAME 
FROM information_schema.KEY_COLUMN_USAGE 
WHERE TABLE_NAME = 'cities';

SELECT TABLE_NAME, COLUMN_NAME, CONSTRAINT_NAME, REFERENCED_TABLE_NAME 
FROM information_schema.KEY_COLUMN_USAGE 
WHERE TABLE_NAME = 'universities';

SELECT TABLE_NAME, COLUMN_NAME, CONSTRAINT_NAME, REFERENCED_TABLE_NAME 
FROM information_schema.KEY_COLUMN_USAGE 
WHERE TABLE_NAME = 'best_student_cities';

SELECT u.university_id, u.name, u.country_id, c.country_name
FROM universities u
JOIN countries c ON u.country_id = c.country_id
LIMIT 10;

SELECT * FROM subjects;
SELECT * FROM subject_rankings;
SELECT COUNT(*) FROM subject_rankings;

DROP TABLE employability_rankings;


CREATE TABLE employability_rankings (
    university_id INT PRIMARY KEY,
    employability_rank INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (university_id) REFERENCES universities(university_id) ON DELETE CASCADE
);
SELECT * FROM employability_rankings;
SELECT COUNT(*) FROM employability_rankings;

DROP TABLE best_student_cities;
DROP TABLE IF EXISTS cities;
-- 先不放入city資訊



SELECT u.university_id, u.name, c.country_name
FROM universities u
JOIN countries c ON u.country_id = c.country_id
WHERE c.country_name = 'United States';


