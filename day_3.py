def clean_data(data):
    cleaned = []

    for item in data:
        ticker = item.get("ticker")
        price = item.get("price")
        field = item.get("field")

        if ticker is None or price is None or field is None or price <= 0:
            continue


        cleaned.append(item)

    return cleaned




