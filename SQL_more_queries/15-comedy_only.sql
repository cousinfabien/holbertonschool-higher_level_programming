-- Lists all shows that are categorized under the 'Comedy' genre
-- Uses two joins to link genres back to their specific shows
SELECT tv_shows.title
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;