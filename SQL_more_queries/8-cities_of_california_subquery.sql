-- Lists all cities in california found in hbtn_0d_usa
SELECT id, city
FROM cities
WHERE state_id = (
    SELECT id
    FROM states
    WHERE name = 'California'
);