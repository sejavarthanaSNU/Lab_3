def register(username, password):
    if username and password:
        print("Registration successful")
    else:
        print("Username and password are required")


register("user", "1234")