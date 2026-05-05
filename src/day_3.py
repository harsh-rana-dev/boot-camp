select * 
from (
    select *,
            row_number() over (partition by ticker order by timestamp desc) as rn 
    from data
) t 
where rn = 1;


select ticker, price
from (
    select ticker, price,
           row_number() over (partition by ticker order by price desc) as rn 
    from data
) t 
where rn <= 2;


select ticker, timestamp, price,
       sum(price) over (partition by ticker order by timestamp) as running_total 
from data;


select ticker, count(*) as cnt 
from data
group by ticker
having count(*) > 1;


import pandas as pd 

df = pd.DataFrame(data)

df = df.dropna(subset=["ticker", "price"])
df = df[df["price"] > 0]

result = df.groupby("ticker", as_index=False)["price"].mean()


df = df.sort_value("timestamp")
df = df.groupby("ticker").tall(1)


latest = df.loc(df.groupby("ticker")["timestamp"].idxmax()) the other method is better 


df = df.sort_value(['ticker', 'price'], ascending=[True, False])
top2 = df.groupby("ticker").head(2)

df = df.sort_value("timestamp")
df["running_total"] = df.groupby("ticker")["price"].cumsum()

