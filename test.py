import pytest
from day_3 import clean_data

def test_data():
    data = [
        {"ticker": "AAPL", "price": 100},
        {"ticker": "AAPL", "price": -50},
        {"ticker": "MSFT", "price": 200},
        {"ticker": "MSFT", "price": None},
        {"ticker": None, "price": 300},
    ]

    result = clean_data(data)

    expected = [
        {"ticker": "AAPL", "price": 100},
        {"ticker": "MSFT", "price": 200},
    ]

    assert result == expected
