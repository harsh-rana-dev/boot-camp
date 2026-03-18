import pandas as pd 

def avg_price(data):
    df = pd.DataFrame(data)

    df = df.dropna(subset=["ticker", "price"])
    df = df[df["price"] > 0]

    result = df.groupby("ticker")["price"].mean()

    return result.to_dict()

    