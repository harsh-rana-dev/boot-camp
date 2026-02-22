# here are al the imports i can understand why they are present but i dont know what to add when in big imports like these
import logging
import time
from typing import List
import requests
from requests.exceptions import RequestException
from pydantic import BaseModel, ValidationError
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

# ------------------ Logging ------------------

# this the the logging setup its recording the execution first will be the date and time the level name then the error or pass messege 

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ------------------ Pydantic Model ------------------

# indecation that the values datatypes 

class StockRecord(BaseModel):
    ticker: str
    price: float
    timestamp: str

# ------------------ Retry Fetch ------------------

# its fetching the data with the try and exept so that it tryes 3 times before falling.

def fetch_with_retry(url: str, retries: int = 3, backoff: int = 2) -> List[dict]:
    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            logging.info("Data fetched successfully")
            return response.json()
        except RequestException as e:
            logging.warning(f"Attempt {attempt+1} failed: {e}")
            if attempt < retries - 1:
                time.sleep(backoff ** attempt)
            else:
                logging.error("All retries failed")
                raise

# ------------------ Database Insert ------------------

# is block is insertiong the feched records to db and creating the table in db also have the try and exept to use logger

def insert_records(records: List[StockRecord]) -> None:
    engine = create_engine("postgresql://user:password@localhost:5432/stocks")
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        for record in records:
            stmt = text("""
                INSERT INTO stocks (ticker, price, timestamp)
                VALUES (:ticker, :price, :timestamp)
                ON CONFLICT (ticker, timestamp)
                DO UPDATE SET
                    price = EXCLUDED.price
            """)
            session.execute(stmt, record.dict())
        session.commit()
        logging.info("Records inserted successfully")
    except Exception as e:
        session.rollback()
        logging.error(f"DB insert failed: {e}")
        raise
    finally:
        session.close()

# ------------------ Main Flow ------------------

# here we have the str url and the final commit steps for the whole code 

def main():
    url = "https://api.example.com/stocks"

    raw_data = fetch_with_retry(url)

    valid_records = []
    for item in raw_data:
        try:
            record = StockRecord(**item)
            valid_records.append(record)
        except ValidationError as e:
            logging.warning(f"Invalid record skipped: {e}")

    insert_records(valid_records)

if __name__ == "__main__":
    main()

# this is for compution the avg price from data

from typing import List, Dict

# defining the varibals 
def compute_average_price(data: List[dict]) -> Dict[str, float]:
    totals = {}
    counts = {}

    #starting the for loop over data 

    for item in data: # has to be str to contnue 
        ticker = item["ticker"]
        price = item["price"]

        if ticker not in totals: # test to chest if the data is right 
            totals[ticker] = 0
            counts[ticker] = 0
#dontunderstand this part
        totals[ticker] += price
        counts[ticker] += 1
#final fungution for agv by devesion
    averages = {}
    for ticker in totals:
        averages[ticker] = totals[ticker] / counts[ticker]

    return averages


# this is a  sql block to creat the table with unique value and peremeters
CREATE TABLE stocks (
    id SERIAL PRIMARY KEY,
    ticker VARCHAR(10) NOT NULL,
    price NUMERIC NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    UNIQUE (ticker, timestamp)
);

# the is is a insert block for the table if the ticker and time is same even then atlest update the price it specal fungution 
INSERT INTO stocks (ticker, price, timestamp)
VALUES ('AAPL', 190.5, '2026-02-21 10:00:00')
ON CONFLICT (ticker, timestamp)
DO UPDATE SET
    price = EXCLUDED.price;



# a small py test for avg price block to check the code is it working properly or not 

import pytest
from my_module import compute_average_price #getting the fungution

def test_compute_average_price(): # dummy data to calclute if it passes the code is currect 
    data = [
        {"ticker": "AAPL", "price": 100},
        {"ticker": "AAPL", "price": 200},
    ]

    result = compute_average_price(data) 

    assert result["AAPL"] == 150 # the output should be exactly this if not the code has bug 