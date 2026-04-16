def uinque_ticker(data):
    seen = set()
    result = []

    for iten in data:
        ticker = item.get("ticker")
        if ticker and ticker not in seen:
            seen.add(ticker)
            result.append(item)

    return result
    
what is set and how is it working here 
explain the code 


def min_price(data):
    result = ()

    for item in data:
        t, p = item["ticker"], item["price"]

        result[t] = min(p,result.get(t, p))

    return result

how is it calcluting
explain the code 



def normalize_price(data):
    prices = [item["price"] for  item in data]
    min_p, max_p = min(prices), max(prices)

    for item in data:
        item["normalized"] = (item["price"] - min_p) / (max_p - min_p)

    return result

    explain this fully 
    
     