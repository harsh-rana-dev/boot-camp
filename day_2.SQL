SELECT id,
       SUM(amount) AS total
FROM profile
GROUP BY id;
