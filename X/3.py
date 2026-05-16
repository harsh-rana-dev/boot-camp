from pydantic import BaseModel

class Trade(BaseModel):
    ticker: str 
    price: float 


from pydantic import BaseModel, field_validator 
 
class Trade(BaseModel):
    ticker: str 
    price: float 

    @field_validator("price")
    def positive_p(cls, v):
        if v <=0:
            raise ValueError("price must be posative")
        return v 


from typing import Optional
from pydantic import BaseModel

class Trade(BaseModel):
    ticker: str 
    price: float
    exchange: Optional[str] = None 


from pydantic import BaseModel

class Trade(BaseModel):
    ticker: str
    price: float


what is this block doing (
def validate_data(data):
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

    return valid, errors )


from pydantic import BaseModel, model_validator

class Trade(BaseModel):
    buy_price: float
    sell_price: float

    @model_validator(mode="after")
    def validate_prices(self):
        if self.sell_price < self.buy_price:
            raise ValueError(
                "sell_price must be >= buy_price"
            )
        return self

what is this code doing 



⚔️ PYDANTIC — 5 INTERVIEW QUESTIONS
1.

What problem does Pydantic solve in data pipelines?

👉 Why not trust raw API data?

2.

What is the difference between:

field_validator

and

model_validator

👉 When would you use each?

3.

What does this mean?

price: Optional[float] = None

👉 Why is this useful in production pipelines?




4.

What does this do?

Trade(**item)

👉 What is ** doing?

5.

What is the difference between:

float

and

StrictFloat

👉 When would strict validation matter?