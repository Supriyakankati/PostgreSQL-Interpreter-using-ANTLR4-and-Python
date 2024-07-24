-- Create the 'links' table
CREATE TABLE links (
    id SERIAL PRIMARY KEY,
    url VARCHAR(255) NOT NULL,
    name VARCHAR(255),
    last_update DATE
);

-- Inserting a date value
INSERT INTO links (url, name, last_update)
VALUES ('https://www.google.com', 'Google', '2013-06-01');

