-- In 8.sql, write a SQL query to list the names of all people who starred in Toy Story.

-- Select names
SELECT name FROM people WHERE id IN
-- SELECT person ID
(SELECT person_id FROM stars WHERE movie_id IN
-- SELECT movie ID
(SELECT id FROM movies WHERE title = "Toy Story"));