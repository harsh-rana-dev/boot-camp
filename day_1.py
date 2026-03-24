def clean_and_avg(data):
    totals = {}
    counts = {}

    for item in data:
        ticker = item.get("ticker")
        price = item.get("price")

        if ticker is None or price is None or price <= 0:
            continue

        if ticker not in totals:
            totals[ticker] = 0
            counts[ticker] = 0

        totals[ticker] += price
        counts[ticker] += 1

    result = {}
    for ticker in totals:
        result[ticker] = totals[ticker] / counts[ticker]

    return result 

