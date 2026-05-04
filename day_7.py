def avg_price(data):
    totals, counts = {}, {}

    for item in data:
        t = item.get("ticker")
        p = item.get("price")

        if not t or p is None or p <= 0:
            continue 

        
        totals[t] = totals.get(t, 0) + p 
        counts[t] = counts.get(t, 0) + 1

    return {t: totals[t] / counts[t] for t in totals}

    