select ticker, max(price) as max_p
from trades
group by ticker;

select ticker, min(price) as min_p 
from trades
group by ticker;

select ticker, count(*) as total_records
from trades
group by ticker;

select ticker,
       sum(price) as total_p
from trades
group by ticker;

select ticker, avg(price) as avg_price
from trades 
where price > 0 
group by ticker;

select * 
from (
    select *,
            row_number() over(
                partition by ticker order by timestamp desc
            ) as rn 
    from trades
) t 
where rn = 1;

select ticker,
        price,
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
       sum(price) over (
            partition by ticker
            order by timestamp
       ) as running_total
from trades;

select ticker,
       price,
       rank() over (
            partition by ticker
            order by price desc
       ) as rnk
from trades;

select ticker,
       price,
       dense_rank() over (
            partition by ticker
            order by price desc 
       ) as dense_rnk 
from trades; 
explain this again dense_rank rank and row_number

select ticker,
       timestamp,
       count(*) as total 
from trades
group by ticker, timestamp
having count(*) > 1;

what is this doing 
having count(*) > 1;

select c.ticker
from company c 
left join  trades t 
on c.ticker = t.ticker
where t.ticker is null;

what is this doing 
where t.ticker is null;

select date(timestamp) as trade_day,
       sum(price) as total_p
from trades
group by date(timestamp);

select count(distinct ticker) as total_ticker
from trades;

insert info trades (ticker, timestamp, prcie)
values ("aapl", now(), 200)
on conflict (ticker, timestamp)
do update
set price = excluded.price;
what is this doing explain

delete from trades
where price <= 0
    or ticker is null;

create index idx_ticker
on trades(ticker);
what is this doing explain

select ticker,
       date(timestamp) as day,
       avg(price) as avg_price
from trades
group by ticker, date(timestamp);
what is this doing explain

select ticker, 
        max(timestamp) as latest_time
from trades
group by ticker;
what is this doing explain

select * 
from trades
where timestamp >= now() - interval "7 days";
what is this doing explain