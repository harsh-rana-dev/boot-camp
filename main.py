def validate_user(profile: dict) -> bool:

    if "name" not in profile:
        return False

    if "age" not in profile:
        return False

    if  profile["age"] <= 0:
        return False

    if "email" not in profile:
        return False

    if "@" not in profile["email"]:
        return False

    return True