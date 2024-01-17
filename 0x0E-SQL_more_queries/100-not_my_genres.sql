-- Write a script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
-- You can use a maximum of two SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT DISTINCT tv_genres.name
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
LEFT JOIN (
    SELECT tv_shows.title, tv_genres.name
    FROM tv_genres
    INNER JOIN tv_show_genres
    ON tv_genres.id = tv_show_genres.genre_id
    INNER JOIN tv_shows
    ON tv_show_genres.show_id = tv_shows.id
    WHERE title = 'Dexter'
) AS combo
ON tv_genres.name = combo.name
WHERE combo.name IS NULL
ORDER BY tv_genres.name ASC;