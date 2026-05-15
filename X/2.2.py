i wrote the code by looking but its getting less day by day 
import pandas as pd 

df = pd.DataFrame(data)

df = df.dropna(subset=["ticker", "price"])
df = df[df["price"] > 0 ]


return = (
    df.groupby("ticker", as_index=False)["price"]
    .mean()
)
what is as_index False dose 


df = df.sort_v(["ticker", "timestamp"])
latest = df.groupby("ticker").tail(1)


df = df.sort_v(
    ["ticker", "price"]
    ascending=[True, False]
)

top2 = df.groupby("ticker").head(2)


df = df.sort_v(["ticker", "timestamp"])

df["running_t"] = (
    df.groupby("ticker")["price"]
    .cumsum()
)
what is this one doing 

df = df.drop_dup(
    subset=["ticker", "timestamp"]
)
its deleting the ticker nad timestamp right 


count = (
    df.groupby("ticker")
    .size()
    .reset_index(name="total")
)
what is this one doing 


avg_df = (
    df.groupby("ticker", as_index=False)["price"]
    .mean()
)

result = avg_df[avg_df["price"] > 100 ]
why this avg_df[avg_df


merged = pd.merge(
    company,
    trade,
    on="ticker",
    how="left"
)

df["trade_day"] = pd.to_datetime(
    df["timestamp"]
).dt.date

daily = (
    df.groupby(["ticker", "trade_day"])["price"]
    .mean()
    .reset_index()
)
what is this one doing 



⚔️ PANDAS — 10 INTERVIEW QUESTIONS
1.

How is:

groupby()

similar to SQL GROUP BY?

👉 What are the key differences?

2.

What does this do?

df.dropna(subset=["ticker", "price"])

👉 Why is it important in pipelines?

3.

What is the difference between:

head()

and

tail()

👉 When would you use each?

4.

Why do we sort before using:

groupby().tail(1)

👉 What breaks if we skip sorting?

5.

What does:

as_index=False

do inside groupby()?

👉 Why is it useful?

6.

What problem does:

drop_duplicates()

solve in DataOps pipelines?

👉 Why is duplicate handling critical?

7.

What is a running total?

👉 How does:

cumsum()

work?

8.

Why is Pandas sometimes slow on large datasets?

👉 Give 3 practical optimization strategies.

9.

When would you choose:

Pandas
SQL

for aggregations and transformations?

👉 Explain trade-offs.

10.

What problems can happen if you load huge datasets fully into memory?

👉 How would you handle this safely in production?