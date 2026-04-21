import pytest

@pytest.fixture
def sample_data():
    return [
        {"ticker": "AAPL", "price": 100},
        {"ticker": "AAPL", "price": 200},
    ]

def test_fix(sample_data):
    result = avg_price(sample_data)
    assert result["AAPL"] == 150

def test_normalize():
    data = [
        {"price": 100},
        {"price": 200},
    ]

    result = normalize_prices(data)

    assert result[0]["normalized"] == 0.0
    assert result[1]["normalized"] == 1.0
