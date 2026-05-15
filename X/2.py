i wrote the code by looking but its getting less day by day 
from pydantic import BaseModel

class Trade(BaseModel):
    ticker: str
    price: float

from pydantic import BaseModel, field_validator

class Trade(BaseModel):
    ticker: str
    price: float

    @field_validator("price")
    def p_price(cls, v):
        if v <= 0:
            raise ValueError("must be p")
        return v 


from pydantic import Optional
from pydantic import BaseModel

class Trade(BaseModel):
    ticker: str
    price: float
    exchange: Optional[str] = None


from pydantic import BaseModel

class Trade(BaseModel):
    ticker: str
    price: float

def valid_data(data):
    valid = []
    errors = []

    for item in data:
        try:
            valid.append(Trade(**item))
        except Exception as e:
            errors.append({
                "data": item,
                "error": str(e)
            })

    return valid, errors
explain this one 


from pydantic import BaseModel

class Trade(BaseModel):
    ticker: str
    price: float


trade = Trade(
    ticker="aapl",
    price="123"
)

price(trade.price)

from pydantic import BaseModel, model_validator

class Trade(BaseModel):
    buy_price: float
    sell_price: float

    @model_validator(mode="after")
    def validate_prices(self):
        if self.sell_price < self.buy_price:
            raise ValueError("sell_price must be >= buy_price")
        return self
explain this one 

from pydantic import BaseModel

class Company(BaseModel):
    name: str
    country: str

class Trade(BaseModel):
    ticker: str 
    price: float
    company: Company
explain this one 

from pydantic import BaseModel

class Trade(BaseModel):
    ticker: str
    price: float

trade = Trade(
    ticker="aapl",
    price=1234
)

print(trade.model_dump)
explain this one 

from pydantic import BaseModel, StrictFloat

class Trade(BaseModel):
    ticker: str
    price: StrictFloat

what is StrictFloat 



⚔️ PYDANTIC — 10 INTERVIEW QUESTIONS
1.

What problem does Pydantic solve in data pipelines?

👉 Why not trust raw API data?



2.

What is the difference between:

field validation
model validation

👉 When would you use each?

3.

What does this do?

price: Optional[float] = None

👉 Why is this useful in real pipelines?

4.

What happens if invalid data is passed into a Pydantic model?

👉 How should pipelines handle this safely?

5.

Why is schema validation important before inserting data into PostgreSQL?

👉 What failures can happen without it?

6.

What is the purpose of:

Trade(**item)

👉 What does ** do?

7.

How would you validate thousands of records without stopping the pipeline when one record fails?

👉 Explain the pattern.

8.

What is the benefit of automatic type conversion in Pydantic?

Example:

price="100"

👉 Why is this useful?

9.

What is the difference between:

float

and

StrictFloat

👉 When would strict validation be important?

10.

Why are nested models useful in APIs and DataOps pipelines?