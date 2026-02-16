SELECT id,
       user_name,
       SUM(amount) AS total_amount
FROM profile
WHERE amount > 0
GROUP BY id, user_name;
