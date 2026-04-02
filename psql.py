from sqlalchemy import create_engine, MetaData, String, Integer, Column, Table

# Create engine
engine = create_engine("postgresql://user:password@localhost/db", echo=True)

# Metadata
meta = MetaData()

# Define table
bots = Table(
    "bots",
    meta,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('age', Integer, nullable=False)
)

# Create table
meta.create_all(engine)

# Insert data using transaction
with engine.begin() as conn:
    insert_stmt = bots.insert().values(name='mik', age=45)
    conn.execute(insert_stmt)

    