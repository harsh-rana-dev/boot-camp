def clean_data(data):
    cleaned = []

    for item in data:
        t = item.get("ticker")
        p = item.get("price")

        if not p or t is None or price <= 0:
            continue 

        cleaned.append(item)

    return cleaned


def avg_price(data):
    totals = {}
    counts = {}

    for item in data:
        t = item["ticker"]
        p = item["price"]

        totals[t] = totals.get(t, 0) + p 
        counts[t] = counts.get(t, 0) + 1 
    
    return {
        t: totals[t] / counts[t]
        for t in totals
    }


def latest(data):
    result = {}

    for item in data:
         t = item["ticker"]
         ts = item["timestamp"]

         if t not in result or ts > result[t]["timestamp"]:
            result[t] = item

    return list(result.values())


def count_t(data):
    counts = {}

    for item in data:
        t = item.get("ticker")

        if not t:
            continue 
        
        counts[t] = counts.get(t, 0) + 1 
    
    return counts


from pydantic import BaseModel 

class Trade(BaseModel):
    ticker: str
    price: float


from pydantic import BaseModel, field_validator 

class Trade(BaseModel):
    ticker: str
    price: float

    @field_validator("price")
    def p_price(cls, v):
        if v <= 0:
            raise ValueError("must be posative")
        return v 


def validate_data(data):
    valid = []
    errors = []

    for item in data:
        try:
            valid.append(Trade(**item))
        except Exception as e:
            errors.append({
                "data": item,
                "error": str(e)
            })

    return valid, errors


from typing import Optional
from pydantic import BaseModel

class Trade(BaseModel):
    ticker: str
    price: float 
    exchange: Optional[str] = None 
explain this one 


def test_avg():
    data = [
        {"ticker": "AAPL", "price": 100},
        {"ticker": "AAPL", "price": 200},  
    ]

    result = avg_price(data)

    assert result["AAPL"] == 150


def test_clean():
    data = [
        {"ticker": None, "price": 100},
        {"ticker": "AAPL", "price": -50},
        {"ticker": "TSLA", "price": 300},
    ]

    result = clean_data(data)

    assert len(result) == 1


import pytest

@pytest.mark.parametrize("prices, expected", [
    ([100, 200], 150),
    ([50, 50], 50),
])

def test_avg(prices, expected):
    data = [
        {"ticker": "AAPL", "price": p}
        for p in prices
    ]

    assert avg_price(data)["AAPL"] == expected
explain this one 


import pytest

def test_invalid():
    with pytest.raise(ValueError):
        Trade(ticker="AAPL", price=-100)


import pandas as pd 

df = pd.DataFrame(data)

df = df.dropna(subset=["ticker", "price"])
df = df[df["price"] > 0]


result = (
    df.groupby("ticker", as_index=False)["price"]
    .mean()
)

df = df.sort_values(["ticker", "timestamp"])

latest = df.groupby("ticker").tail(1)

df = df.sort_values(
    ["ticker", "price"],
    ascending=(True, False)
)

top2 = df.groupby("ticker").head(2)