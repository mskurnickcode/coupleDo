-- In 12.sql, write a SQL query to list the titles of all movies in which both Johnny Depp and Helena Bonham Carter starred.

-- get names of movies
SELECT title FROM movies WHERE id IN
-- get movie ids with both person ids
(SELECT movie_id FROM stars WHERE person_id IN
-- Select ids for depp and carter
(SELECT id FROM people WHERE name == "Helena Bonham Carter"))
INTERSECT
SELECT title FROM movies WHERE id IN
-- get movie ids with both person ids
(SELECT movie_id FROM stars WHERE person_id IN
-- Select ids for depp and carter
(SELECT id FROM people WHERE name == "Johnny Depp"));