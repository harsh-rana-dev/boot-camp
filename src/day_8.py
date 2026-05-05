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


def latest(data):
    result = {}

    for item in data:
        t = item.get("ticker")
        ts = item.get("timestamp")

        if t not in result or ts > result[t]["timestamp"]:
            result[t] = item

    return list(result.values())



select ticker, price, timestamp,
from (
    select *,
            row_number() over (partition by ticker order by timestamp desc) as rn 
    from trades
) t 
where rn = 1;


select ticker, price
from (
    select ticker, price,
            row_number() over (partition by ticker order by price as desc) as rn 
    from trades
) t 
where rn <= 2;


latest = df.loc[df.groupby("ticker")["timestamp"].idmax()]

df = df.sort_values(["ticker", "price"], ascending=[True, False])
top2 = df.groupby("ticler").head(2)


def test_empty():
    assert avg_price([]) == {}


import pytest

@pytest.mark.parametrize("price, expected",[
    ([100, 200], 150),
    ([50, 50], 50),
])

def test_avg(price, expected):
    data = [{"ticker": "aapl", "price": p} fpr p in prices]
    assert avg_price(data)["aapl"] == expected


version: "3.4"

services:
   db:
     image: postgres

   app:
     build: . 
     depends_on:
      - db


services:
    app:
        build: . 
        environment:
           db_host: db 


from pydantic import BaseModel, field_validator

class Trade(BaseModel):
    ticker: str
    price: float

    @field_validator("price")
    def valid_price(cls, v):
        if v <= 0:
            raise ValueError("invalid price")
        return v


def validate_trades(data):
    valid, errors = [], []

    for item in data:
        try:
            valid.append(Trade(**item))
        except Exception as e:
            errors.append({"data": item, "error": str(e)})

    return valid, errors

from sqlalchemy import func

result = session.query(
    Trade.ticker,
    func.avg(Trade.price).label("avg_price")
).group_by(Trade.ticker).all()

trade = session.query(Trade).filter_by(ticker="AAPL").first()

if trade:
    trade.price = 150
else:
    session.add(Trade(ticker="AAPL", price=150))

session.commit()


import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


logger = logging.getLogger(__name__)

def run_pipeline():
    logger.info("pipeline started")

    try:
        data = load_data()
        logger.info(f"loaded {len(data)} records")
    except Exception as e:
        logger.error(f"failed: {e}")