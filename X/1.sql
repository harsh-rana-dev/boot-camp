select ticker, avg(price) as avg_price
from trades
group by ticker;

tell me the diffrence betweem group by and order by 

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
where rn = 3;

select ticker,
       timestamp,
       price,
       sum(price) over (
        partition by ticker order by timestamp desc
       ) as running_total
from trades;

select ticker,
       timestamp,
       count(*) as total
from trades
group by ticker, timestamp
having count(*) > 1;
how is it deleting the duplacets 

select count(distinct ticker) as total_ticker
from trades; 

select date(timestamp) as t_day,
       sum(price) as total_p,
       avg(price) as avg_price
from trades
group by date(timestamp);

explain the line 
group by date(timestamp);

select c.ticker
from companies c 
left join trades t 
on c.ticker = t.ticker
where t.ticker is NULL;

insert into trades (ticker, timestamp, price)
values ("aapl", NOW(), 123)

ON CONFLICT (ticker, timestamp)
do update
set price = excluded.price;

select ticker, price,
       rank() over (
            partition by ticker order by price desc
       ) as price_rank 
from trades;
