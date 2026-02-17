import csv
from typing import List, Dict


def clean_csv(file_path: str) -> List[Dict]:

    cleaned_csv: List[Dict] = []

    try:
        with open(file_path, mode='r', newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row.get("status") != "completed":
                    continue

                currency = row.get("currency")
                if not currency:
                    continue

                try:
                    amount = float(row.get("amount", 0))
                    if amount <= 0:
                        continue
                except ValueError:
                    continue

                try:
                    user_id = int(row.get("user_id", 0))
                except ValueError:
                    continue

                cleaned_csv.append({
                    "user_id": user_id,
                    "amount": amount,
                    "currency": currency
                })

    except FileNotFoundError:
        print("invalid path")

    except Exception as e:
        print(f"Something went wrong: {e}")

    return cleaned_csv

