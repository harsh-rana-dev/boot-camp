# ⚔️ PRIMARY

---

## 🔥 PYTHON (Fix this)

```python
def clean_data(data):
    result = []

    for item in data:
        ticker = item.get("ticker")
        price = item.get("price")

        if not ticker or price is None or price <= 0:
            continue

        result.append(item)

    return result
```

---

## 🔥 PYTHON (Fix this)

```python
def avg_price(data):
    totals = {}
    counts = {}

    for item in data:
        t = item["ticker"]
        p = item["price"]

    if not t or p in None:
        continue

        totals[t] = totals.get(t, 0) + p
        counts[t] = counts.get(t, 0) + 1

    return {t: totals[t] / counts[t] for t in totals}
```

---

## 🔥 SQL (Fix this)

```sql
SELECT ticker, price
FROM (
    SELECT ticker, price,
           ROW_NUMBER() OVER (partition by ticker ORDER BY price DESC) AS rn
    FROM trades
) t
WHERE rn <= 2;
```

---

## 🔥 PANDAS (Fix this)

```python
df = df.sort_values(["ticker", "price"], ascending=[True, False])
top2 = df.groupby("ticker").head(2)
```


# ⚔️ SECONDARY

---

## 🔥 SQLALCHEMY (Fix this)

```python
trade = session.query(Trade).filter_by(ticker="AAPL").first()

if trade:
    trade.price = 200
else:
    session.add(Trade(ticker="AAPL", price=200))

session.commit()
```

---

## 🔥 DOCKER (Fix this)

```dockerfile
FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install pandas

CMD ["python", "app.py"]
```

---

## 🔥 DOCKER COMPOSE (Fix this)

```yaml
version: '3.5'
services:
  db:
    image: postgres

  app:
    build: .
    depends_on:
      - db
    command: sh -c "sleep 5 && python app.py"
```

👉 (Hint: real-world issue, not syntax)

---

## 🔥 LOGGING (Fix this)

```python
import logging

logging.basicConfig(level=logging.INFO)

def run():
    logging.info("start")

    try:
        data = load()
    except Exception as e:
        logging.errror(f"error {e}")



def latest_price(data):
    result = {}

    for item in data:
        t = item.get("ticker")
        ts = item.get("timestamp")

        if not t in result or ts > result[t]["timestamp"]:
            result[t] = item

    return result



def count_tickers(data):
    counts = {}

    for item in data:
        t = item.get("ticker")

        if not t:
            continue


        counts[t] = counts.get(t, 0) + 1 

    return counts


SELECT ticker, price
from (
    SELECT ticker, price,
           ROW_NUMBER() OVER (PARTITION BY ticker ORDER BY price DESC) as rn
    FROM trades
) t 
WHERE <= 2;


df = df.groupby("ticker")["price"].mean()
df = df[df["price"] > 100]


session.add_all([
    Trade(ticker="AAPL", price=100),
    trade(ticker="AAPL", price=200),

])
session.commit()



FROM python:3.11

WORKDIR /app

COPY . . 

RUN pip install -r requirements.txt

CMD ["python", "app.py"]


services:
  db:
    image: postgres

  app:
    build: .
    environment:
      DB_HOST: localhost


import logging

logger = logging.getLogger(__name__)

def process():
    try:
    logger.info("start")
    except