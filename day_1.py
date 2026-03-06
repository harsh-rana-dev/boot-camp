def group_price_by_ticker(data):
    grouped = {}

    for item in data:
        ticker = item.get("ticker")
        price = safe_price(item)

        if ticker is None or price is None:
            continue

        if ticker not in grouped:
            grouped[ticker] = []

        grouped[ticker].append(price)

    return grouped


