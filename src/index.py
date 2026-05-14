from sqlalcamy import create_engine, String, Column, Float, Integer func
from sqlalcamy.orm import declarative_base, sessionmaker

Base = declarative_base()

class socity(Base):
    __tablename__ = "people"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

engine = create_engine("postgresql://user:pass@localhost/db")
Session = sessionmaker(bind=engine)
session = Session()


session.add_all([
    socity(name="hada", age="10")
    socity(name="ad", age="20")
    socity(name="Aky", age="30")
    socity(name="pk", age="40")
    socity(name="yoo", age="50")
])
session.commit()

result = session.query(
    socity.name
    func.avg(socity.age).label("avg_age_group")
).group_by(socity.id).all()

i tried with few changes


def upsert_socity(session, name, age):
    socity = session.query(socity).filter_by(name=name).first()

    if socity:
        socity.age = age
    else:
        session.add(socity(name=name, age=age))

    session.commit()


def upsert_society(session, name, age):
    record = session.query(Society).filter_by(name=name).first()

    if record:
        record.age = age
    else:
        session.add(Society(name=name, age=age))

    session.commit()


FROM python:3.11-slim

WORKDIR /app

COPY . . 

RUN pip install --no-cache-dir -r requirment.txt

CMD ["python", "app.py"]

now i can almost write it without looking this much



name: ci 

on: push

job:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4
      - run: pip install -r requirment.txt
      - run: pytest




version: '3.5'
services:
  db:
    image: postgres
    environment:
      - user: hada005
      - pass: 3456787654

  app:
    build: .
    depends_on:
      - db


services:
  db:
    image: postgres
    ports:
      -"5432:5432"
    volumes:
      - db_data:/var/lib/postgresql/data 

volumes:
  db_data:



services:
  app:
  build: .
  command: sh -c "sleep 5 && python pipeline.py"

explain this one is this makeing the command to triger diley?


import logging

logging.basicconfig(level=logging.INFO)

def run():
    logging.info("started")
    try:
        data = loud_data()
        logging.info(f"loaded {len(data)} records")
    except Exception as e:
        logging.error(f"fail: {e}")



logging.basicconfig(
    filename="log.log",
    level=logging.INFO,
    fromat="%(asctime)s - %(levelname)s - %(message)s"
)


import logging

logger = logging.getLogger(__name__)

def process_trade(trade):
    logger.info("process trade", extra={"ticker": trade["ticker"]})

explain this one 
