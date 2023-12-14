-- Get the id of the Comedy genre
SET @comedy_genre_id := (SELECT id FROM tv_genres WHERE name = 'Comedy');

SELECT title
FROM tv_shows
WHERE id NOT IN (SELECT DISTINCT show_id FROM tv_show_genres WHERE genre_id = @comedy_genre_id)
ORDER BY title ASC;

