import random
def log_in():
    print("Login Dashboard")
    print("-"*30)
    login =int(input(" log In = 1 or Crate account = 2 or To See Report = 3 : "))
    if login == 1:
        print("Asia Bank")
        breakpoint()
    elif login == 2:
        print("Create Account ")

        def bank_server():
            def super_user():
                print("Creating Username and Password for Super User: ")
                print("-" * 30)
                username = input("Enter Your Username : ")
                password = input("Enter Your Password : ")
                print("Default Super User Account created successfully.")
                print("------THANK YOU FOR CREATING------")
                print("Default Super users Username : ", username)
                print("Default Super users Password : ", password)
                print("-" * 30)
                return username, password

            super_user()

        def admin_account():
            print("Crate Admin Account")
            print("-" * 30)
            admin_username = input("Enter admin username: ")
            admin_password = input("Enter admin password: ")
            print("Administrative Staff Account created successfully.")
            print("_" * 30)
            print("Admin Username is :", admin_username)
            print("Admin Password is :", admin_password)
            print("_" * 30)
            return admin_username, admin_password

        admin_account()
    def register_customer():
        name = input("Enter customer name: ")
        address = input("Enter customer address: ")
        account_type = input("Enter account type (Saving or Current): ")
        account_number = random.randint(1000000000000000, 9999999999999999)
        password = input("Enter a password : ")
        print("-" * 30)
        print("Customer registered successfully.")
        print("-" * 30)
        print("Thank You For Creating Account In Our Bank.")
        '''print("-" * 30)
        print("Customer Name Is :", name)
        print("Costumers Address Is : ", address)
        print("Your Account Number Is :", account_number)
        print("Your Password is : ", password)
        print(f"You Create {account_type} Account.")
        print("-" * 30)'''
        return account_number, password
    register_customer()


log_in()