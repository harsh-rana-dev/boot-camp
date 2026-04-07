import pandas as pd 

df = pd.DataFrame(data)
df = df.dropna(subset=["ticker", "price"])
df = df[df["price"] > 0]
# i need a explanating for this one what is it doing 


df.groupby("ticker", as_index=False)["price"].mean()
# i need a explanating for this one what is it doing 


df.sort_values(by="price", ascending=False)
# is it sorting the price from the higest to lowest 


def test_avg_price():
    data = [
        {"ticker": "AAPL", "price": 100},
        {"ticker": "AAPL", "price": 200},
    ]

    result = avg_price(data)

    assert result["AAPL"] == 150


def test_clean_data():
    data = [{"ticker": None, "price": 100}]

    result = clean_data(data)

    assert result == []


def test_pipeline():
    data = [
        {"ticker": "AAPL", "price": 100},
        {"ticker": "AAPL", "price": -50},
    ]

    cleaned = clean_data(data)
    result = avg_price(cleaned)

    assert result["AAPL"] == 100