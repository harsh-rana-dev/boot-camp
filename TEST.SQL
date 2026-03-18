select ticker, sum(price) as total_price
from data
group by ticker;

select ticker, AVG(price) as avg_price
from data
group by ticker;

select ticker
from data
group by ticker
having AVG(price) > 150;

select ticker
from data
group by ticker
having SUM(price) > 550;

select * 
from data 
order by price DESC # explain DESC to me 
limit 5;

select ticker, count(*) as total_records
from data
group by ticker;