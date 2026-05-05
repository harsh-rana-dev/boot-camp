i wrote it by the looking few times but not entirly for every code but i feel it better then to just copy 


def clean_data(data):
    cleaned = []

    for item in data:
        t = item.get("ticker")
        p = item.get("price")

        if not t or p is None or p <= 0:
            continue
        

        cleaned.append(item)

    totals = {}
    counts = {}


    for item in cleaned:
        t = item["ticker"]
        p = item["price"]


        totals[t] = totals.get(t, 0) + p 
        counts[t] = counts.get(t, 0) + 1 

    return {t: totals[t] / counts[t] for t in totals}



select * 
from (
    select *,
            row_number() over (partition by ticker order by timestamp desc) as rn 
    from data
) t 
where rn = 1;

df = df.sort_value(["ticker", "price"], ascending=[True, False])
top2 = df.groupby("ticker").head(2)
why is this line ascending=[True, False]


def lates_ticker(data):
    result = {}

    for item in data:
        t = item["ticker"]
        ts = item["timestamp"]

        if t not in result or ts > result[t]["timestamp"]:
            result[t] = item

    return list(result.values())


select ticker, timestamp, price,
        sum(price) over (partition by ticker order by timestamp ) as running_total
from data;


df = df.dropna(subset=["ticker", "price"])
df = df[df["price"] > 0 ]

cleaned = clean_data(data)

import pandas as pd 

df = pd.DataFrame(cleaned)

result = df.groupby("ticker")["price"].mean()

insert into result (ticker, avg_price) values ()




def avg_price(data):
    total = 0
    count = 0

    for item in data:
        if "price" not in item or item["price"] is None:
            continue
        


        total += item['price']
        count += 1

    return total / count if count > 0 else 0 

    is this a secliton code 