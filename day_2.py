from typing import List, Dict


def summarize_purchases(purchases: List[Dict]) -> Dict:

    total_revenue = 0
    purchase_count = 0
    revenue_by_user: Dict[int, float] = {}

    top_user = None
    top_revenue = 0

    for purchase in purchases:
        user_id = purchase.get("user_id")
        amount = purchase.get("amount")

        if not isinstance(user_id, int):
            continue

        if not isinstance(amount, (int, float)) or amount <= 0:
            continue

        purchase_count += 1
        total_revenue += amount

        if user_id not in revenue_by_user:
            revenue_by_user[user_id] = 0

        revenue_by_user[user_id] += amount

        if revenue_by_user[user_id] > top_revenue:
            top_revenue = revenue_by_user[user_id]
            top_user = user_id

    return {
        "total_revenue": total_revenue,
        "purchase_count": purchase_count,
        "revenue_by_user": revenue_by_user,
        "top_user": top_user
    }
