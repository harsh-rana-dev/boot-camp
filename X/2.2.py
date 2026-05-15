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

the pd groupby works in memory and the sql group works in the db 


2.

What does this do?

df.dropna(subset=["ticker", "price"])

👉 Why is it important in pipelines?

it delets the the ticker and price from the table 

3.

What is the difference between:

head()

and

tail()

👉 When would you use each?

its like i want the the price of each ticker then i will use the tail to decide how many i wnat and head is for like printing the latest records 

4.

Why do we sort before using:

groupby().tail(1)

👉 What breaks if we skip sorting?

i dont know 

5.

What does:

as_index=False

do inside groupby()?

👉 Why is it useful?

i dont know

6.

What problem does:

drop_duplicates()

solve in DataOps pipelines?

👉 Why is duplicate handling critical?

duplicates are a critical issue  for the sql table i can creat alot of problems thats why we use on conflict on sql inserts

7.

What is a running total?

👉 How does:

cumsum()

work?

i dont know 

8.

Why is Pandas sometimes slow on large datasets?

👉 Give 3 practical optimization strategies.

i dont know 

9.

When would you choose:

Pandas
SQL

for aggregations and transformations?

👉 Explain trade-offs.

sql for large and complex tasks 

and pandas for small and fast once

10.

What problems can happen if you load huge datasets fully into memory?

👉 How would you handle this safely in production?

with batch inserts 