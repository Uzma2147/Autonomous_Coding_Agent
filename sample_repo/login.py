def login(username, password):
    if password == "":
        raise ValueError("Password cannot be empty")
    return True