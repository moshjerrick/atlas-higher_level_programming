-- Lists all cities in california found in hbtn_0d_usa
SELECT id, city FROM cites WHERE state_id IN (SELECT id FROM states WHERE name = 'California') ORDER BY id;
