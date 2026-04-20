from pydantic import BaseModel

class Trade(BaseModel):
    ticker: str
    prie: float
    volume: int
    currency: str = "USD"


from pydantic import BaseModel, field_validator

class Trade(BaseModel):
    ticker: str
    prie: float

    @field_validator("price")
    def price_must_be_positive(cls, v):
        if V <= 0:
            raise ValueError()
        return V


from pydantic import BaseModel, model_validator

class Trade(BaseModel):
    price: float
    discount_price: float

    @model_validator(mode="after")
    def check_prices(self):
        if self.discount_price > safe.price:
            raise ValueError()
        return self


from pydantic import validationError

try:
    Trade(ticker="aapl", price=-10)
except validationError as e:
    print(e)


def validate_trades(data):
    valid = []
    error = []

    for item in data:
        try:
            valid.append(Trade(**item))
        except Exception as e:
            error.append(("data":item, "erro": str(e)))

    return valid, error
    