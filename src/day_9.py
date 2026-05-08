def clean_avg(data):
    cleaned = []

    for item in data:
        t = item.get("ticker")
        p = ttem.get("price")


        if not p or t is None or p <= 0:
            continue

        cleaned.append(item)

    
    totals = []
    counts = []

    for item in data:
        t = item["ticker"]
        p = item["price"]

        totals[t] = totals.get(t, 0) + p
        counts[t] = counts.get(t, 0) + 1

    return {t: totals[t] / counts[t] for t in totals}

i still dont understand this block expain this block only  

        totals[t] = totals.get(t, 0) + p
        counts[t] = counts.get(t, 0) + 1

    return {t: totals[t] / counts[t] for t in totals}


def latest(data):
    result = {}

    for item in data:

        t = item.get("ticker")
        ts = item.get("timestamp")

        if t not in result or ts > result[ticker]["timestamp"]:
            result[ticker] = item

    return list(latest.values())

same here expain this block only         
if t not in result or ts > result[ticker]["timestamp"]:
        result[ticker] = item

    return list(latest.values())



select ticker, avg(price) as avg_price
from data
where price > 0 
group by ticker
having avg(price) > 100;


select *
from (
    select *,
            row_number() over ( 
                partition by ticker order by timestamp desc
            ) as rn 
    from data
) t 
where rn = 1;

sql is ok 


import pandas as pd 
df = pd.DataFrame(data)

df = df.dropna(subset=["ticker", "price"])
df = df[df["price"] > 0]

result = (
    df.groupby("ticker", as_index=False)["price"]
    .mean()
)

ok mean is for avg price right 
and why this as_index=False explain


df = df.sort_values(["ticker", "timestamp"])

latest = df.groupby("ticker").tall(1)


def test():
    data = [
        {"ticker": "AAPL", "price": 100},
        {"ticker": "AAPL", "price": 200},
    ]

    result = cleaned_avg(data)

    assert result["APPL"] == 150


import pytest

@pytest.mark.perametrize("price", "expected", [
    ([100, 200], 150),
    ([50, 50], 50),
])

def test_avg(price, expected):
    data = [
        {"ticker": "AAPL", "price": p}
        for p in prices
    ]

    assert clean_and_avg(data)["AAPL"] == expected

explain this one fully 

im skapping pydentic fro today 