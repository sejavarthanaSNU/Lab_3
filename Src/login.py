def login(username, password):
    if username == "admin" and password == "1234":
        print("Login successful")
    else:
        print("Invalid credentials")


login("admin", "1234")