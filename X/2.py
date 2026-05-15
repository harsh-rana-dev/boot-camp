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

pydantic prevents bad data and negetive and empty rows from entring the pipeline preventing crashes 

raw api data contanes negetive and empty rows if it is not cleaned it will defenetly crash the pipeline

2.

What is the difference between:

field validation
model validation

👉 When would you use each?

field_validator cheks a single field
and model_validator cheks multipal fields

3.

What does this do?

price: Optional[float] = None

👉 Why is this useful in real pipelines?

its for price if the price float or  none it will pass it is useful for missing data 

4.

What happens if invalid data is passed into a Pydantic model?

👉 How should pipelines handle this safely?

it should throug a value error instently and stop the pipeline 


5.

Why is schema validation important before inserting data into PostgreSQL?

👉 What failures can happen without it?

its important becous without validation a negetive value can brake the inserting

same without validation the db will crash in midle of the ingestiong

6.

What is the purpose of:

Trade(**item)

👉 What does ** do?

i dont know

7.

How would you validate thousands of records without stopping the pipeline when one record fails?

👉 Explain the pattern.

the validation will come soon in pipeline just after ingestin so its cleaned befor the further procesing 

8.

What is the benefit of automatic type conversion in Pydantic?

Example:

price="100"

👉 Why is this useful?

it very useful becous its automatic and it can manage small conversion like this "100"

9.

What is the difference between:

float

and

StrictFloat

👉 When would strict validation be important?

i dont know

10.

Why are nested models useful in APIs and DataOps pipelines?

i dont know