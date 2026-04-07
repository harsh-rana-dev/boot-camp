select ticker, avg(price) as avg_price
from data
group by ticker;

select ticker, sum(price) as total_price
from data
group by ticker;

select * 
from data
order by price desc
limit 5;

select *
from data
where price > 100;

select ticker, avg(price) as avg_price
from data
group by ticker
having avg(price) > 100;

select ticker, count(*) as count
from data
group by ticker;

select c.ticker , c.sector, m.price
from compney c
left join market m 
on c.ticker = m.ticker
# i need a explanating for this one and what is a left join and all typs of join

insert into data (ticker, price)
value ('aapl', 100)
on conflict (ticker)
do update set price = excluded.price;
# i need a explanating for this one

