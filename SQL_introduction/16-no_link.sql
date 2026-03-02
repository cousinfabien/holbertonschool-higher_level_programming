-- Lists all records of second table where name is not empty, showing score and name ordered by score descending
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
