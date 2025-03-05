
USE study_abroad_assitant;

SHOW Tables;

CREATE TABLE City_Data (
    City_ID INT PRIMARY KEY AUTO_INCREMENT,
    City_Name VARCHAR(100) NOT NULL,
    Country VARCHAR(100) NOT NULL,
    Overall_Score FLOAT,
    Student_View FLOAT,
    Student_Mix FLOAT,
    Employer_Activity FLOAT,
    Desirability FLOAT,
    Affordability FLOAT,
    Rankings FLOAT,
    Last_Updated DATETIME DEFAULT CURRENT_TIMESTAMP
);

SELECT * FROM City_Data;

ALTER TABLE City_Data
CHANGE COLUMN City_Name City VARCHAR(100) NOT NULL;

SELECT * FROM City_Data;
