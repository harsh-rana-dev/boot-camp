from typing import List, Dict

def safe_price(item):
    price = item.get("price")

    if price is None:
        return None

    if isinstance(price, str):
        price = price.strip()

    try:
        price = float(price)
    except (TypeError, ValueError):
        return None

    if price <= 0:
        return None

    return price