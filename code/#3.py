df.drop_duplicates(subset=["ticker"])

df.sort_values("timestamp").groupby("ticker").tail(1)

df["price_with_tax"] = df["price"].apply(lambda x: x * 1.1)

explain these too 

