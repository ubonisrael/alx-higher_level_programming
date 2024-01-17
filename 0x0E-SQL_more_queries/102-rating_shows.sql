-- Write a script that lists all shows from hbtn_0d_tvshows_rate by their rating.
-- Each record should display: tv_shows.title - rating sum
-- Results must be sorted in descending order by the rating
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT shows.title, combo.rating
FROM tv_shows AS shows
INNER JOIN (
    SELECT ratings.show_id, SUM(ratings.rate) as rating
    FROM tv_show_ratings as ratings
    GROUP BY ratings.show_id
) AS combo
ON shows.id = combo.show_id
ORDER BY combo.rating DESC
;
