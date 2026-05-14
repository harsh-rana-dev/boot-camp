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
                partition by ticker
                order by price desc
            ) as rn
    from trades
) t 
where rn <= 2;


select ticker,
       timestamp,
       price,
       sum(price) over (
           partition by ticker 
           order by timestamp
       ) as running_total
from trades;


select ticker,
        count(*) as total 
from trades
group by ticker
having count(*) > 1;


select c.ticker,
       m.price
from company c 
join market m 
on c.ticker =  m.ticker;


select c.ticker
from company c  
left join market m 
on c.ticker = m.ticker
where m.ticker is NULL;


select ticker, price,
       rank() over (
            partition by ticker
            order by price desc
       ) as rnk 
from trades;


select distinct on (ticker)
       ticker,
       price,
       timestamp
from trades
order by ticker, timestamp desc;


⚔️ SQL INTERVIEW QUESTIONS (THEORY)
1.

What is the difference between:

WHERE
HAVING

👉 When is each executed?

having comes after group by i know this much

2.

What does:

PARTITION BY ticker

actually do inside a window function?

it basicly group by ticker in a loop  

what is the difference between order by and group by ?

3.

Why do we need:

ORDER BY timestamp DESC

inside ROW_NUMBER()?

What breaks if we remove it?

i dont know 

4.

Difference between:

ROW_NUMBER()
RANK()
DENSE_RANK()

row_number is a loop 
rank is to rank the top output
DENSE_RANK i dont know

5.

What is a window function?

How is it different from GROUP BY?

it a loop of group by 

6.

Why would you use LEFT JOIN instead of JOIN?

to arange the tabel form the left 

7.

What problem does:

HAVING COUNT(*) > 1

solve in pipelines?

it counts the entire table with a loop 

8.

Why is SQL often preferred over Pandas for large aggregations?

becaus its faster for large aggregations and you can do complex tasks in sql faster 

9.

How would you safely re-run ingestion without creating duplicates?

(SQL/DataOps thinking question)

with sql upserts and on conflct insertst 

10.

If your SQL query is slow:

👉 what are 3 things you would check first?

how big is the table 

ami i printing the full output 

idk

currect my answers and explain the conseperts in breaf