select ticker, avg(price) as avg_price
from trades
group by ticker
where avg(price) > 0;


🔥 SECTION 3 — DEBUGGING


SELECT ticker, AVG(price)
FROM trades
GROUP BY ticker
WHERE AVG(price) > 100;

SELECT *
FROM trades
GROUP BY ticker;
it should probably be order by i guess



🔥 SECTION 4 — THEORY
9.

Difference between:

WHERE
HAVING

having comes after order by

10.

Difference between:

ROW_NUMBER()
RANK()
DENSE_RANK()

i dont know


🔥 SECTION 5 — REAL INTERVIEW STYLE
11.

A pipeline re-runs every hour and inserts duplicate records.

How would you prevent duplicates in PostgreSQL?

by using unique values and upserts 


12.

Why is ORDER BY important inside window functions?

What breaks if removed?

its to complete the loop if the window functions if we remove it the data might not be aranged 