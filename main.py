def validate_user(profile: dict) -> bool:
    if "name" not in profile:
        return False
    if "age" not in profile:
        return False
    if "eamil" not in profile:
        return False
    if  profile["age"] <= 0:
        return False
    if "@" in profile["email"]:
        return False
    return True



def get_active_users(users: list) -> list:
    active_users = []
    for user in users:
        if user.get("active") == True:
        active_users.append(user)

    return active_users



def sum_dict_values(data: dict) -> int:
    total = 0

    for num in data:
        total = total + data[num]
    return total


def to_upper(text: str) -> str:
    return text.upper()
def square(num: int) -> int:
    return num * num
def list_length(items: list) -> int:
    return len(items)

