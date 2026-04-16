select distinct on (ticker) ticker, price, timestamp
from data
order by ticker, timestamp desc;
explain this one 

select 
    ticker,
    price,
    rank() over (partition by ticker order by price desc) as rank
from data;
explain this one 

select
    ticker,
    timestamp,
    sum(price) over (partition by ticker order by timestamp) as running_total
from data;
explain this one too


select ticker, count(*)
from data
group by ticker
having count(*) > 1;
explain this one too



