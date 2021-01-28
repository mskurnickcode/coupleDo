-- In 9.sql, write a SQL query to list the names of all people who starred in a movie released in 2004, ordered by birth year.

-- get names from people
SELECT name FROM people WHERE id IN
-- get ids of people from movies
(SELECT person_id FROM stars WHERE movie_id IN
-- get ids of movies released in 2004 from movies
(SELECT id FROM movies WHERE year = 2004))
ORDER BY birth ASC;