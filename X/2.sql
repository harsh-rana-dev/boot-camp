i wrote the code by looking but its getting less day by day 
select ticker, avg(price) as avg_price
from trades
group by ticker;

select ticker, avg(price) as avg_price
from trades
group by ticker
having avg(price) > 100;

select *
from (
    select *,
            row_number() over (
                partition by ticker order by timestamp desc
            ) as rn 
    from trades
) t 
where rn = 1;

select ticker, price
from (
    select ticker, price,
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

select c.ticker
from companies c 
left join trades t 
on c.ticker = t.ticker
where t.ticker is NULL;

INSERT INTO trades (
    ticker,
    timestamp,
    price
)
VALUES (
    'AAPL',
    NOW(),
    200
)
on conflict (ticker, timestamp)
do update
set price = excluded.price;

select ticker,
       price,
       rank() over (
        partition by ticker order by price desc 
       ) as rank_p
from trades;


select ticker,
       date(timestamp) as t_day,
       avg(price) as avg_price,
       sum(price) as total_p
from trades
group by ticker, date(timestamp);



⚔️ SQL INTERVIEW QUESTIONS (INTERVIEW LEVEL)
1.

What is the difference between:

WHERE
HAVING

👉 When is each executed?

2.

What does:

PARTITION BY ticker

actually do inside a window function?

👉 How is it different from GROUP BY?

3.

Why do we need:

ORDER BY timestamp DESC

inside ROW_NUMBER()?

👉 What breaks if we remove it?

4.

What is the difference between:

ROW_NUMBER()
RANK()
DENSE_RANK()

👉 When would you use each?

5.

What is a window function?

👉 Why is it powerful in DataOps pipelines?

6.

Why would you use LEFT JOIN instead of INNER JOIN?

👉 Give a real DataOps example.

7.

What problem does this solve?

HAVING COUNT(*) > 1

👉 Why is duplicate detection important?

8.

Why is SQL often preferred over Pandas for large aggregations?

👉 What trade-offs exist?

9.

How would you safely re-run ingestion jobs without creating duplicate rows?

👉 Explain the SQL/DataOps strategy.

10.

If a SQL query becomes very slow in production:

👉 what are 3 things you would check first?