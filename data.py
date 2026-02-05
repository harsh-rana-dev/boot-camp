def get_active_users(users: list) -> list:
    active_users = []

    for user in users:
        if user.get("active") == True:
            active_users.append(user)
    
    return active_users
