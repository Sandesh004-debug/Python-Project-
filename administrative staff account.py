def admin_account():
    admin_username = input("Enter admin username: ")
    admin_password = input("Enter admin password: ")
    with open("sandesh.txt", 'w') as f:
        f.write(admin_username + "\n")
        f.write(admin_password)
    print("Administrative Staff Account created successfully.")
    print("_" * 30)
    print("Admin Username is :", admin_username)
    print("Admin Password is :", admin_password)
    print("_" * 30)

admin_account()