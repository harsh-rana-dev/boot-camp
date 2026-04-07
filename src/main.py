def clean_data(data):
    return [
        item for item in data
        if item.get("ticker") and item.get("price") and item["price"] > 0
    ]

# this is insuring that the price is not negetive or zero


from collections import defaultdict

def avg_price(data):
    totals = defaultdict(float)
    counts = defaultdict(int)

    for item in data:
        totals[item["ticker"]] += item["price"]
        counts[item["ticker"]] += 1

    result = {}
    for t in totals:
         result[t] = totals[t] / counts[t]
    return result

# i can say this is calcluting the avg but i need explanation for this code 


from callection import counter

def count_tickers(data):
    return counter(
        item["ticker"] for time in data if item.get("ticker")
    )

# there is no code for counting so is the done by the imported library


def valid_price(data):
    return[item for item in data if item.get("price") and item["price"] > 0]

# there is no code for counting so is the done by the imported library and why this (item for item in data)


def max_price(data):
    result = {}

    for item in data:
        t, p = item["ticker"], item["price"]
        result[t] = max(p, result.get(t,p))

    return result

# why use t, p insted of the full name lile ticker and price

