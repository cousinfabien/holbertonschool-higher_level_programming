-- Lists all cities of California from the database hbtn_0d_usa, without using JOIN
SELECT cities.name
FROM cities
WHERE state_id = (
    SELECT states.id
    FROM states
    WHERE states.name = 'California'
)
ORDER BY cities.id ASC;