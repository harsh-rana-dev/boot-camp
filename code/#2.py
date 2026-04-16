def test_min_p():
    data = [
        {"ticker": "AAPL", "price": 100},
        {"ticker": "AAPL", "price": 50},
    ]

    result = min_price(data)

    assert result["AAPL"] == 50


def test_empty_data():
    data = []

    result = avg_price(data)

    assert result == {}


explain this one only ==
def test_normalize_prices():
    data = [
        {"ticker": "AAPL", "price": 100},
        {"ticker": "AAPL", "price": 200},
    ]

    result = normalize_prices(data)

    assert result[0]["normalized"] == 0.0
    assert result[1]["normalized"] == 1.0