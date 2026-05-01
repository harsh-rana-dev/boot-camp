 i wrote about 50 to 60 % by myself 
 and looked quite a few times but even to wite 50% i needed to look few times to know what comes next 

def clean_data(data):
    cleaned = []

    for item in data:
        t = item.get("ticker")
        p = item.get("price")

        if not t or p is None or p < 0:
            continue
        
        cleaned.append(item)

    totals = {}
    counts = {}

    for item in cleaned:
        t = item["ticker"]
        p = ["price"]

        totals[t] = totals.get(t, 0) + p 
        counts[t] = counts.get(t, 0) + 1

    return {t: totals[t] / counts[t] for t in totals}



select ticker, price, timestamp
from (
    select *,
            row_number() over (partition by ticker order by timestamp desc) as rn
    from trades
) t 
where rn = 1;


import pandas as pd 

df = pd.DataFrame(data)

df = df.dropna(subset=["ticker", "price"])
df = df[df["price"] > 0 ]

df = df.sort_value(['ticker', 'price'], ascending=[True, False])
top2 = df.groupby("ticker").head(2)


def test_p():
    data = [
        {"ticker": "AAPL", "price": 100},
        {"ticker": "AAPL", "price": -50},
        {"ticker": None, "price": 200},
    ]

    result = proces_data(data)

    assert result["AAPL"] == 100
    assert len(result) == 1


from pydantic import BaseModel, field_validator

class Trade (BaseModel):
    ticker: str 
    price: float

    @field_validator("price")
    def positive_price(cls, v):
        if v <= 0:
            raise ValueError("price must be posative")
        return v 


def validate_data(data):
    valid, error = [], []

    for item in data:
        try:
            valid.append(Trade(**item))
        except Exception as e:
            error.append({"data", item, "error": str(e)})

    return valid, error



from sqlalchemy import create_enginne, Column, String, Float, func
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Trade(Base):
    __tablename__ = "trades"
    ticker = Column(String, primary_key=True)
    price = Column(Float)

engine = create_engine("postgresql://user:pass@localhost/db")
Session = sessionmaker(bind=engine)
session = Session()

result = session.query(
    Trade.ticker,
    func.avg(Trade.price).label("avg_price")
).group_by(Trade.ticker).all()




FROM python:3.11-slim

WORKDIR /app

COPY requirment.txt .

RUN pip inatall --no-catch-dir -r requirment.txt

COPY . . 

CMD ["python", [app.py]]


version: '3.5'

services:
  db:
    image: postgresql
    ports:
      -"5432:5432"

  app:
    build: . 
    depends_on:
      - db

    environment:
      host: db

    command: sd -c "sleep 5 && python app.py"


  
import logging

logging,basicConfig(
    level=logging.INFO,
    fromat="%(asctime)s - %(levelname)s - %(message)s"
)

def run_p():
    logging.info("started")

    try:
        data = load_data()
        logging.info("lodding")
    except Exception as e:
        logging.error(error)



name: ci 

on: [push]

jobs:
   tests:
     runs-on: ubuntu-latest


     steps:
      - uses: actions/checkout@v3
      - run: pip install -r requirment.txt
      - run: pytest