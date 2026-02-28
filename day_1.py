def count_tickers(data):
    counts = {}

    for item in data:
        ticker = item.get("ticker")

        if ticker is None:
            continue

        if ticker not in counts:
            counts[ticker] = 0

        counts[ticker] += 1

    return counts


def total_valid_prices(data):
    total = 0

    for item in data:
        price = safe_price(item)

        if price is None:
            continue

        total += price


    return total
    