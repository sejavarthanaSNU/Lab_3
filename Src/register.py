def register(username, email, password):
    if username and email and password:
        print("User registration successful")
        print("Welcome,", username)
    else:
        print("All registration fields are required")


register("student", "student@example.com", "1234")