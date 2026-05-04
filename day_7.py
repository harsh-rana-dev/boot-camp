def avg_price(data):
    totals, counts = {}, {}

    for item in data:
        t = item.get("ticker")
        p = item.get("price")

        if not t or p is None or p <= 0:
            continue 

        
        totals[t] = totals.get(t, 0) + p 
        counts[t] = counts.get(t, 0) + 1

    return {t: totals[t] / counts[t] for t in totals}

    


def latest_records(data):
    result = {}

    for item in data:
        t = item["ticker"]
        ts = item["timestamp"]

        if t not in result or ts > result[t]["timestamp"]:
            result[t] = item


    return list(result.values())


select ticker, price, timestamp
from (
    select *,
            row_number() over (partition by ticker order by timestamp desc) as rn 
    from trades
) t 
where rn = 1;


select ticker, timestamp,
        sum(price) over (partition by ticker order by timestamp) as running_total
from trades;


SELECT ticker, price, timestamp
FROM (
    select *,
            ROW_NUMBER() OVER (PARTITION BY ticker ORDER BY price DESC) as rn 
    from trades
) t 
where rn = 1;


SELECT ticker, timestamp,
        sum(price) over (partition by ticker order by timestamp) as running_total
FROM trades;









result = session.query(
    trade.ticker,
    func.avg(trade.price)
).group_by(trade.ticker).all()

trade = session.query(Trade).filter_by(ticker="AAPL").first()


trade = session.query(Trade).filter_by(ticker="AAPL")
trade.price = 100

session.add(Trade)
session.commit()

i dont understand these how to debug


services:
    db:
      image: postgres

    app:
        build: . 
        depends_on:
          - db

environment:
    host: db


environment:
    host: localhost

depends_on:
   - db


import logging 

logging.basicConfig(level=logging.INFO)

logging.info("pipeline started")


import logging
logging.basicConfig(level=logging.INFO)

logging.error("pipeline false")


from pydantic import BaseModel

class Trade(BaseModel):
    ticker: str 
    price: float


from pydantic import BaseModel, field_validator

class Trade(BaseModel):
    ticker: str
    price: float

    @field_validator("price")
    def check(cls, v):
        if v <= 0:
            raise ValueError("fahhhh")
        return v 



from pydantic import BaseModel, field_validator


class Trade(BaseModel):
    ticker: str
    price: float

    @field_validator("price")
    def check_price(v):
        if v <= 0:
            raise ValueError("fahhhh")
        return v


Trade(ticker="AAPL", price="abc")
what to fix here 