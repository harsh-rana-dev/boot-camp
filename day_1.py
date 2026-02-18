from typing import Dict, List


def validate(users: List[Dict]) -> List[Dict]:
    valid_users: List[Dict] = []

    for user in users:
        user_id = user.get("id")
        email = user.get("email")
        age = user.get("age")

        if not isinstance(user_id, int) or user_id <= 0:
            continue

        if not isinstance(email, str) or not email.strip():
            continue

        if not isinstance(age, int) or age < 0 or age > 120:
            continue

        valid_users.append(user)

    return valid_users


def validate_users_split(users: List[Dict]) -> Dict[str, List[Dict]]:

    result = {
        "valid": [],
        "invalid": []
    }

    for user in users:
        user_id = user.get("id")
        email = user.get("email")
        age = user.get("age")

        is_valid = True

        if not isinstance(user_id, int) or user_id <= 0:
            is_valid = False

        if not isinstance(email, str) or not email.strip():
            is_valid = False

        if not isinstance(age, int) or age < 0 or age > 120:
            is_valid = False

        if is_valid:
            result["valid"].append(user)
        else:
            result["invalid"].append(user)

    return result


def summarize_users(valid_users: List[Dict]) -> Dict:

    total_valid = len(valid_users)

    if total_valid == 0:
        return {
            "total_valid": 0,
            "average_age": 0
        }

    total_age = sum(user["age"] for user in valid_users)

    return {
        "total_valid": total_valid,
        "average_age": total_age / total_valid
    }
