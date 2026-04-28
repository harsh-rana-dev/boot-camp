def clean_normal(data):
    cleaned = []

    for item in data:
        ticker = item.get("ticker")
        price = item.get("price")

        if not ticker or price is None or price <= 0:
            continue

        cleaned.append({"ticker": ticker, "price": price})

    prices = [x["price"]for x in cleaned]
    min_p, max_p = min(prices), max(prices)

    for item in cleaned:
        item["normalized"] = (item["price"] - min_p) / (max_p - min_p)
    
    return cleaned

what dose normalized do and why 



from collections import defaultdict

def latest_avg_p(data):
    latest = {}

    for item in data:
        t = item["ticker"]
        ts = item["timestamp"]

        if t not in latest or ts > latest[t]["timestamp"]:
            latest[t] = item

    totales = defaultdict(float)
    counts = defaultdict(int)

    for item in latest.values():
        t = item["ticker"]
        p = item["price"]
        totales[t] +=p 
        counts[t] +=1

    return {t: totales[t]/ counts[t] for t in totales}

what is this code doing and why and explain each line



select ticker, price
from (
    select ticker, price,
           row_number() over (partition by ticker order by price desc) as rn 
    from data
) t this t 
where rn <= 2;

why is the t here and row_number is a function right as rn and is this a limiter also
where rn <= 2;


select ticker, timestamp, price,
        sum(price) over (partition by ticker order by timestamp) as running_total
from data;

what is this one doing


import pandas as pd 

df = pd.DataFrame(data)
df = df.dropna(subset=["ticker", "price"])
droping the missing value rows but how? with subset or dropna

df = df[df["price"] > 0]
price has t obe above 0 

result = df.groupby("ticker", as_index=False)["price"].mean()
what is the as_index and mean doing?


df = df.sort_values("timestamp")
latest = df.groupby("ticker").tall(5)

tall means lemit ?

def test_p():
    data = [
        {"ticker": "AAPL", "price": 100},
        {"ticker": "AAPL", "price": -50},
    ]

    cleaned = clean_normal(data)

    assert len(cleaned) == 1

    assert cleaned[0]["price"] == 100
what is this assert doing 

def test_empty():
    assert = data([]) == {}


from pydantic import BaseModel, field_validator

class Trade(BaseModel):
    ticker: str 
    price: float

    @field_validator("price")
    def check_p(cls, v):
        if v <= 0:
            raise ValueError("negetive")
        return v 



def validate_trades(data):
    valid, error = [], []

    for item in data:
        try:
            valid.append(Trade(**item))
        except Exception as e:
            error.append({"data": item, "error": str(e)})

    return valid, errors

    what is this one ding explain line by line