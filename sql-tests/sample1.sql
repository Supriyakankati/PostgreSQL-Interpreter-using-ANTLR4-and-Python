-- Create a table
CREATE TABLE Student (
    id INT,
    data TEXT
);

-- Inserting data into a non-existent table
INSERT INTO NonExistent (id, data)
VALUES
    (1, 'test'),
    (2, 'example');

-- Selecting data from a non-existent table
SELECT data FROM NonExistent;
