def clean_record(data):
    return [
        item for item in data
         if item.get("ticker") and item.get("price") and if item["price"] > 0
    ]

this code is a gatekeeper it prevents bad data to come in like negetive prices and somthing which is not ticker or price

and if price = 0 drop it becouse no valid data will come in 


from collections import defaultdict

def avg_price(data):
    totals = defaultdict(float)
    counts = defaultdict(int)

    for item in data:
        totals[item["ticker"]] += item["price"]
        counts[item["ticker"]] += 

    return {t:totals[t] / counts[t] for t in totals}

i need an explanetion for this 

and for this What if data is empty? then i have to check the records to see if they match the logic or not 



from collections import counter

def count_records(data):
    return counter(item["ticker"] for item in data if item.get("ticker"))

its just counting the records with the help of counter 


def max_price(data):
    result = {}
    for item in data:
        t, p = item["ticker"], item["price"]
        result[t] = max(p, result.get(t, p))
    return result

its for finding out the max price in the records

    What if ticker missing? it probably crashes 


def unique(data):
    seen = set()
    result = []

    for item in data:
        t = item.get("ticker")
        if t and t not in seen:
            seen.add(t)
            result.append(item)

    return result

def normalize_prices(data):
    prices = [item["price"] for item in data]
    min_p, max_p = min(prices), max(prices)

    for item in data:
        item["normalized"] = (item["price"] - min_p) / (max_p - min_p)

    return data

What if all prices same? i cant but if it is answer will be the same 

