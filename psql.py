from sqlalchemy import create_engine, MetaData, String, Integer, Column, Table, Float, ForeignKey

engine = create_engine("postgresql://user:password@localhost/db", echo=True)

meta = MetaData()

bots = Table(
    "bots",
    meta,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('age', Integer, nullable=False)
)

things = Table(
    "things",
    meta,
    Column('id', Integer, primary_key=True),
    Column("des", String, nullable=False),
    Column("value", Float),
    Column("owner", Integer, ForeignKey("bots.id"))
)

meta.create_all(engine)

with engine.begin() as conn:

    conn.execute(bots.insert(), [
        {'name': 'a', 'age': 10},
        {'name': 'b', 'age': 20},
        {'name': 'c', 'age': 30},
        {'name': 'd', 'age': 40},
        {'name': 'e', 'age': 50}
    ])

    conn.execute(things.insert(), [
        {'owner': 1, 'des': 'something i dont know', 'value': 456},
        {'owner': 2, 'des': 'something i dont know', 'value': 556},
        {'owner': 3, 'des': 'something i dont know', 'value': 656},
        {'owner': 4, 'des': 'something i dont know', 'value': 47556},
        {'owner': 5, 'des': 'something i dont know', 'value': 456874}
    ])
