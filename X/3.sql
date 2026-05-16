select ticker, avg(price) as avg_price
from trades
where price > 0
group by ticker;

select * 
from (
    select *,
            row_number() over (
                partition by ticker order by timestamp desc
            ) as rn 
    from trades
) t 
where rn = 1;

select ticker,
       price
from (
    select ticker,
           price,
           row_number() over (
            partition by ticker order by price desc
           ) as rn 
    from trades
) t 
where rn <= 3;

select ticker,
       timestamp,
       price,
       sum(price) over (
           partition by ticker 
           order by timestamp
       ) as running_total
from trades;

select ticker,
       timestamp,
       count(*) as total 
from trades
group by ticker, timestamp
having count(*) > 1;



⚔️ SQL — 5 INTERVIEW QUESTIONS
1.

What is the difference between:

GROUP BY

and

PARTITION BY

👉 When would you use each?

2.

Why do we need:

ORDER BY timestamp DESC

inside:

ROW_NUMBER()

👉 What happens if we remove it?

3.

What problem does this solve in pipelines?

HAVING COUNT(*) > 1
4.

What is a running total?

👉 Why are window functions useful for this?

5.

Difference between:

ROW_NUMBER()
RANK()
DENSE_RANK()

👉 When would you use each?