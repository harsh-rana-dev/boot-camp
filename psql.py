from sqlalchemy import create_engine, MetaData, String, Integer, Column, Table

engine = create_engine("postgresql://user:password@localhost/db", echo=True)

meta = MetaData()

bots = Table(
    "bots",
    meta,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('age', Integer, nullable=False)
)

meta.create_all(engine)


with engine.begin() as conn:
    insert_stmt = bots.insert().values(name='milk', age=1)
    conn.execute(insert_stmt)