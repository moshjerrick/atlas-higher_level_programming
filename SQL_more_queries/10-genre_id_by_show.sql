-- import database dump from hbtn_0d_tvshows
SELECT tv_shows.title, tv_shows_genres.genre_id
    FROM tv_shows
    LEFT JOIN tv_shows_genres
    ON tv_shows.id = tv_shows_genres.show_id
    ORDER BY tv_shows.title, tv_shows_genres.genre_id;