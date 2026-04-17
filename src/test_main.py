import pytest
from main import get_weather

def test_get_weather():
    assert get_weather(45) == "hot"
    assert get_weather(15) == "cold"



def test_invalid_prices():
    data = [{"ticker": "AAPL", "price": "123"}]

    result = clean_data(data)

    assert result == [{"ticker": "AAPL", "price": 123.45}]

