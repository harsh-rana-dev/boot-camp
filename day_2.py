from collection import defaultdict

def group_price_by_ticker(data):
    grouped = defaultdict(list)

    for item in data:
        ticker = item.get("ticker")
        price = safe_price(item)

        if ticker is None or price is None:
            continue

        grouped[ticker].append(price)


        return dict(grouped)