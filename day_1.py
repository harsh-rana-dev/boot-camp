im writing it by looking but my patern recogenetion is better
def clean_data(data):
    result = []
    for item in data:
        ticker = item.get("ticker")
        price = item.get("price")

        if not ticker or price in None or price <= 0:
            continue    why continue
 
        result.append({"ticker": ticker, "price": price})

    return result

        
from collections import defaultdict


def avg_price(data):
    totals = defaultdict(float)
    counts = defaultdict(int)

    for itme in data:
        t = item.get["ticker"]
        p = item.get["price"]

explain this one this lines 
        totals[t] += p 
        counts[t] += 1

    return {t: totals[t] / counts[t] for t in totals}


def latest_records(data):
    result = {}

    for item in data:
        t = item["ticker"]
        ts = item["timestamp"]

        if t not in result or ts > result[t]["timestamp"]:
            result[t] = item

    return list(result.values())

explain this one fully 


select ticker, avg(price) as avg_price
from data
group by ticker;



select *
from (
    select *,
            row_number() over (partition by ticker order by timestamp DESC) as rn
    from trades
) t 
where rn = 1;

explain this one fully what is it doing 


select ticker, timestamp,
       sum(price) over (partition by ticker order by timestamp) as running_total
from trades;

explain this one fully what is it doing 


import pandas as pd

df = pd.DataFrame(data)
df = df.dropna(subset=["ticker", "price"])
df = df[df["price"] > 0]

df.groupby("ticker", as_index=False)["price"].mean()

df.sort_values("timestamp").groupby("ticker").tail(1)

explain these three fully word by word what is it doing and why 


def test_avg():
    data = [
        {"ticker": "aapl", "price": 100},
        {"ticker": "aapl", "price": 200},
    ]
    result = avg_price(data)
    assert result["aapl"] == 150

def clean_data():
    data = [{"ticker": None, "price": -100}]
    assert clean_data(data) == []


import pytest

@pytest.mark.perametrize("prices, expected",[
    ([100, 200], 150),
    ([50, 50], 50),
])

def test_avg(price, expected):
    data = [{"ticker": "aapl", "price": p} for p in prices]
    assert avg_price(data)["appl"] == expected


 


from pydantic import BaseModal

class data(BaseModal):
    ticker: str
    price: float


from pydantic import field_validator

class Trade(BaseModal):
    ticker: str
    price: float

    @field_validator("price")
    def price_p(cls, v):
        if v <= 0:
            raise ValueError("price must be +")
        return v 

cls is class and vais value right 


def validate_trades(data):
    valid, errors = [], []

    for item in data:
        try:
            valid.append(trade(**item))
        except Exception as e:
            error.append({"data": item, "error": str(e)})

    return valid, errors

    explain this one fully what is it doing 