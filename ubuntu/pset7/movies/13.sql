--In 13.sql, write a SQL query to list the names of all people who starred in a movie in which Kevin Bacon also starred.


SELECT name FROM people WHERE id IN
-- Select all the people from his movies
(SELECT person_id FROM stars WHERE movie_id IN
-- Select movies with kevin bacon
(SELECT movie_id FROM stars WHERE person_id ==
-- select correct Kevin Bacon
(SELECT id FROM people WHERE name == "Kevin Bacon" AND birth == 1958))) AND name != "Kevin Bacon";