i worte it by looking 
select *
from (
    select *, 
            row_number() over (partition by ticker order by timestamp desc) as rn
    from Trades
) t 
where rn = 1;

i know these wagly explain again in breaf
why ROW_NUMBER()
why PARTITION BY
why ORDER BY DESC

select ticker, price
from (
    select ticker, price, 
            row_number() over (partition by ticker order by price DESC) as rn 
    from data
) t 
where rn <= 2;


select ticker, timestamp, price,
        sum(price) over (partition by ticker order by timestamp DESC) as running_total
from data;
what is a running_total



import pandas as pd 

df = pd.DataFrame(data)

df df.dropna(subset=["ticker", "price"])
df = df[df["price"] > 0]

result = df.groupby("ticker", as_index=False)["price"].mean()


df = df.sort_values("timestamp")
latest = df.groupby('ticker').tail(1)


latest = df.loc[df.groupby("ticker")["timestamp"].idxmax()]
what is it doing 


df = df.sort_values(["ticker", "price"], ascending=[True,False])
what is this line doing 
top2 = df.groupby("ticker").head(2)


import pytest

@pytest.mark.parametrize("price, expected", [
    ([100, 200], 150),
    ([50, 50], 50),
])
def test_avg(price, expected):
    data = [{"ticker": "aapl", "price": p} for p in prices]
    assert avg_price(data)["aapl"] == expected



def test_empty():
    assert data([]) == {}


import pytest

def test_invalid():
    with pytest.raise(ValueError):
        Trade(ticker="aapl", price=-23)

