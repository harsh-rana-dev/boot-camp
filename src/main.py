i worte it by looking but i have started to catch the pattern for two to three words like i know what is next it still wrong sometimes

and import thing the explanations showil be detaled and tell what every line is doing

def clean data(data):
    return [
        item for item in data
        if item.get("ticker") and item.get("price") and item["price"] > 0
    ]

this code is fetching item from data safe load this way the code dosent crash  and insuring that the price is above 0 


from collection import defaultdict

def avg_price(data):
    totals = defaultdict(float) maybe makeing sure the output is floatand int by default
    counts = defaultdict(int)


    for item in data:
        totals[item["ticker"]] += item["price"]
        counts[item["ticker"]] += 

    return {t: totals[t] / counts[t] for t in totals}

    i dont know what is this doing explain this one


from collection import counter

def count_ticker(data):
    return counter(item["ticker"] for item in data if item.get("ticker"))

    here the counter fugntion is imported if this code found ticker it will be counted 


def max_price(data):
    result = {}

    for item in data:
        t, p = item["ticker"], item["price"]
        result[t] = max(p, result.get(t, p))
    return result


def min_price(data):
    result = {}
    for item in data:
        t, p = item["ticker"], item["price"]
        result[t] = min(p, result.get(t, p))
    return result

    what is these doing explain these i know there are geting the max price and min price in the data 


def unique_ticker(data):
    seen = set()
    result = []

    for item in data:
        t = item.get["ticker"]
        if t and t not in seen:
            seen.add(t)
            result.append(item)

    return result

    this code is for removing dublicates
    its adding the tickers in set becous set cont contanin dublicates 


def normalized_prices(data):
    prices = [item["price"] for item in data]
    min_p, max_p = min(prices), max(prices)

    for item in data:
        item["normalized"] = (item["price"] - min_p) / (max_p - min_p)

    return data

    what is this doing explain this one and what is normalized_prices
    i can see its getting the max and min but why 



def validate_trades(data):
    valid, error = [], []

    for itme in data:
        try:
            valid.append(Trade(**item))
        except Exception as e:
            errors.append({"data": item, "error": str(e)})

    return valid, error

    what is this doing explain this one in detail


select ticker, AVG(price) as avg_price
from data
group by ticker;

getting the avg of prices  and grouped by ticker


select ticker, count(*)
from data
group by ticker;

for finding out total and grouped by ticker

select ticker, AVG(price) as avg_price
from data
group by ticker
having AVG(price) > 100;

this the with the having filter for price to get what we want 

selet * 
from data
order by price DESC
limit 5;

this the getting the top 5 prices 
with the help of DESC and getting only 5 by limit


select c.ticker, m.price
from company c
join market m on c.ticker = m.ticker;

this is joining two tabels on ticker 


select c.ticker
from company c 
left join market m on c.ticker = m.ticker
where m.ticker is null;

i know its joing form the left but i still dont understand it 
so what is this doing explain left join 


select DISTINCT ON (ticker) *
from data
order by ticker, timestamp DESC;

with DISTINCT we skip duplacates and get the exact count for the data


SELECT *
FROM (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY ticker ORDER BY timestamp DESC) AS rn
    FROM data
) t
WHERE rn = 1;

SELECT ticker, price,
       RANK() OVER (PARTITION BY ticker ORDER BY price DESC) AS rnk
FROM data;

SELECT ticker, timestamp,
       SUM(price) OVER (PARTITION BY ticker ORDER BY timestamp) AS running_total
FROM data;

explain these three i dont understand any of these


import pandas as pd 

df = pd.DataFrame(data)
df = df.dropna(subset=["ticker", "price"])
df = df[df["price"] > 0]

its loading the data then clearing it 
and price should be above 100 but why after dropna ?


df.groupby("ticker", as_index=False)["price"].mean()

df.sort_values(by="price", ascending=False)

df.drop_duplicates(subset=["ticker"])

df.sort_values("timestamp").groupby("ticker").tail(1)

df["price_with_tax"] = df["price"].apply(lambda x: x * 1.1)


explain these four i dont understand any of these 


def test_avg():
    data = [
        {"ticker": "AAPL", "price": 100},
        {"ticker": "AAPL", "price": 200},   
    ]

    result = avg_price(data)
    assert result["AAPL"] == 150

    testing is the avg fugntion is working fine or not 
    if the main code return somthing like this (200) then the code is broken 


def test_empty():
    assert avg_price([]) == {}

    if somthing comes then the code is broken


def test_clean():
    data = [{"ticker": None, "price": 100}]
    assert clean_data(data) == []

    its for the cleaning fugntion working or not
    if the main code return somthing like this "ticker": None, "price": 100 then the code is broken 


import pytest 

def test_invalid_prices():
    with pytest.raises(ValueError):
        Trade(ticker="AAPL", price=-10)

    if somthing like this (ticker="AAPL", price=-10) came it will raise a ValueError 


import pytest

@pytest.mark.parametrize("prices, expected", [
    ([100, 200], 150),
    ([50, 50], 50),
])
def test_avg(prices, expected):
    data = [{"ticker": "AAPL", "price": p} for p in prices]
    assert avg_price(data)["AAPL"] == expected



def test_pipeline():
    data = [
        {"ticker": "AAPL", "price": 100},
        {"ticker": "AAPL", "price": -50},
    ]

    cleaned = clean_data(data)
    result = avg_price(cleaned)

    assert result["AAPL"] == 100