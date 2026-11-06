-- Database schema for the CGPA Management System (MySQL 5.7+)
-- view_students.html expects 20 columns: id, name, 8 x (cgpa, credit),
-- total_credit and average_cgpa. The last two are calculated by MySQL.

CREATE DATABASE IF NOT EXISTS cgpa_management;
USE cgpa_management;

CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    sem1_cgpa DECIMAL(3,2), sem1_credit INT,
    sem2_cgpa DECIMAL(3,2), sem2_credit INT,
    sem3_cgpa DECIMAL(3,2), sem3_credit INT,
    sem4_cgpa DECIMAL(3,2), sem4_credit INT,
    sem5_cgpa DECIMAL(3,2), sem5_credit INT,
    sem6_cgpa DECIMAL(3,2), sem6_credit INT,
    sem7_cgpa DECIMAL(3,2), sem7_credit INT,
    sem8_cgpa DECIMAL(3,2), sem8_credit INT,
    total_credit INT GENERATED ALWAYS AS (
        sem1_credit + sem2_credit + sem3_credit + sem4_credit +
        sem5_credit + sem6_credit + sem7_credit + sem8_credit
    ) STORED,
    average_cgpa DECIMAL(4,2) GENERATED ALWAYS AS (
        (sem1_cgpa * sem1_credit + sem2_cgpa * sem2_credit +
         sem3_cgpa * sem3_credit + sem4_cgpa * sem4_credit +
         sem5_cgpa * sem5_credit + sem6_cgpa * sem6_credit +
         sem7_cgpa * sem7_credit + sem8_cgpa * sem8_credit)
        / NULLIF(sem1_credit + sem2_credit + sem3_credit + sem4_credit +
                 sem5_credit + sem6_credit + sem7_credit + sem8_credit, 0)
    ) STORED
);
