-- Create a table named "Student" with columns "name" (string) and "age" (integer)
CREATE TABLE Student (
    name VARCHAR(255),
    age INT
);

-- Insert multiple rows into the "Student" table
INSERT INTO Student (name, age)
VALUES
    ('alice', 12),
    ('bob', 15),
    ('cindy', 16);

-- Select rows from the "Student" table where name is not 'alice' or age is 16
SELECT name, age FROM Student
WHERE name != 'alice' OR age = 16;