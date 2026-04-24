from sqlalchemy import create_engine, Column, String, Float, func what is func
from sqlalchemy.orm import declarative_base, sessionmaker 

Base = declarative_base()

Class Trade(Base):
    __tablenaem__ = "proft"
    ticker = Column(String, primary_key=True)
    price = Column(Float)

engine = create_engine("postgresql://user:pass@host/db")
Session = sessionmaker(bind=engine)
session = Session()

session.add_all([
    Trade(ticker="aapl", price=123),
    Trade(ticker="aapl", price=143),
])
session.commit()

result = session.query(
    Trade.ticker,
    func.avg(Trade.price)
).group_by(Trade.ticker).all()

is it calculating the avg and gouping it by ticker?
print(result)


trade = session.query(Trade).filter_by(ticker="appl").first()

if trade:
    trade.price = 150
else:
    session.add(Trade(ticker="appl", price=150))

session.commit()

what is it doing explain why is it used 


FROM python:3.11-slim

WORKDIR /app

COPY . . 

RUN pip install pandas psycopg2

CMD ["python", "app.py"]


docker run -e DB_host=localhost -e DB_port=5432 myapp
explain this command 


version: '3.5'
services:
  db:
    image: postgres
    environment:
      user=hada
      pass=132

  app:
    build: .
    depends_on:
      - db


services:
  pipeline:
    build: .
    command: python pipeline.py

  db:
    image: postgres
    ports:
      -'5432:5432'

      
import logging

logging.basicConfig(level=logging.INFO)

def run_pipeline():
    logging.info("starting the pipeline")

    try:
        data = load_data()
        logging.info(f"loaded {len(data)} records")
    except Exception as e:
        logging.error(f"failed: {e}")



logger = logging.getLogger(__name__)

def process_trade(trade):
    logger.info("processing trade", extra={"ticker": trade["ticker"]})


name: ci 

on: push

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v5
      - run: pip install -r requirment.txt
      - run: pytest


jobs:
  pipeline:
    runs-on: ubuntu-latest


    steps:
      - uses: actions/checkout@v3
      - run: pip install pandas pytest
      - run: python pipeline.py 
      - run: pytest
