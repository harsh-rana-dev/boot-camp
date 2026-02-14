from typing import List, Dict

def clean_transactions(transactions: List[Dict]) -> List[Dict]:

    if not isinstance(transactions, list):
        raise TypeError("transaction must be a list")

    cleaned = []

    for tx in transactions:
        if not isinstance(tx, dict):
            continue

        user_id = tx.get("user_id")
        amount = tx.get("amount")
        currency = tx.get("currency")


        if user_id is None or currency is None:

            continue        
    
        try:
            amount = float(amount)
        except (ValueError, TypeError):
            continue

        if amount < 0:
            continue


        cleaned.append({
            "user_id": user_id,
            "amount": amount,
            "currency": currency
        })

    return cleaned