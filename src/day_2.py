select ticker, count(*)
from data
group by ticker;

select c.ticker
from company c
left join market m on c.ticker = m.ticker
where m.ticker is null;

select distinct on (ticker) *
from data
order by ticker, timestamp DESC;

select *
from (
    select*,
            row_number() over (partition by ticker order by timestamp DESC) as rn 
    from data
) t 
where rn = 1;

select 
    ticker,
    timestamp,
    avg(price) over(
        partition by ticker
        order by timestamp
        rows between 2 preceding and current row 
    ) as moving_avg

select 
    ticker,
    price,
    case
        when price > 100 then 'high'
        when price > 50 then 'medium'
        else 'low'
    end as category
from data;

select *
from data
where price > (
    select avg(price) from data
);

select * 
from data d1
where price = (
    select max(price)
    from data d2
    where d1.ticker = d2.ticker
)

insert into data(tiker, price)
values('aapl', 123)
on conflict (ticker)
do update set price = excluded.price;

select ticker, count(*)
from data
group by ticker
having count(*) > 1;

select *
from data
where ticker is null or price is null;

