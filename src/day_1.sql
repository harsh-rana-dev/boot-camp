select ticker, AVG(price) as avg_price
from data
group by ticker;

select ticker, count(*)
from data
group by ticker;

select ticker, AVG(price) as avg_price
from data
group by ticker
having AVG(price) > 100;
what is wrong here and why explain

select *
from data
order by price DESC
limit 10;

select *
from data
order by price ASc
limit 10;

select *
from data
where price between 200 and 2000;

select c.ticker, m.price
from company c 
join market m on c.ticker = m.ticker;
so what will be the new table name and ticker will join right 

select c.ticker, m.price
from company c 
left join market m on c.ticker = m.ticker
where m.ticker is null;
what is the diffrence and explain 

select c.sector, avg(m.price) why is this not here {as avg_price}
from company c 
join market m on c.ticker = m.ticker
group by c.sector;

select distinct ticker
from data;

select distinct on (ticker) * 
from data
order by ticker, timestamp desc;

select 
    ticker, 
    price,
    rank() over (partition by ticker order by price DESC) as rnk
from data;
what is it doing explain

select * 
from (
    select *, 
            row_num() over (partition by ticker order by timestamp DESC) as rn
    from data
) t 
where rn = 1;
what is it doing explain

select 
    ticker,
    timestamp,
    sum(price) over (partition by ticker order by timestamp) as running_total
from data;
what is it doing explain

select 
    ticker,
    timestamp,
    avg(price) over(
        (partition by ticker order by timestamp
        rows between 2 preceding and current row
    ) as moving_avg

from data;
what is it doing explain

select 
    ticker,
    price,
    case
        where price > 100 then 'high'
        where price > 50 then 'medium'
        else 'low'
    end as category
from data;
i can tell what it is doing but explain as well

select *
from data
where price > (
    select avg(price) for data
);
what is it doing explain

select * 
from data d1
where price = (
    select max(price)
    from data d2
    where  d1.ticker = d2.ticker
);
what is it doing explain

insert into data (ticker, price)
values ('aapl', 123)
on conflict (ticker)
do update set price = excluded.price;
what is it doing explain

select ticker, count(*)
from data
group by ticker
having count(*) > 1;
what is it doing explain

select *
from data
where ticker is null or price is null;