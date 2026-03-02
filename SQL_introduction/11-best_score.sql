-- Lists all records with score >=10 in second table by score descending
SELECT score, name
FROM second_table
WHERE score >=10
ORDER BY score DESC;
