def clean_data(data):
    cleaned = []

    for item in data:
        ticker = item.get("ticker")
        price = item.get("price")

        try:
            if isinstance(price, str):
                price = float(price)
        except ValueError:
            continue

        if ticker is None or price is None or price <= 0:
            continue

        cleaned.append({"ticker": ticker, "price": price})

    return cleaned
