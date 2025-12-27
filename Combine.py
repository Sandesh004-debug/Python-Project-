import random
def bank_server():
    def super_user():
        print("Creating Username and Password for Super User: ")
        print("-"*30)
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
        print("Admin Account")
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

    def report():
        print("Making customer's statement by customer:")
        print("_" * 30)
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")
        print("")
        print("Generating customer's statement of account report by admin staff:")
        print("-"*30)
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")
        return start_date
        return end_date

    report()
    def money():
        total_deposit = 0
        total_withdraw = 0
        x = input("What you want deposit or withdraw the money  :")
        if x == "deposit":
            deposit = float(input("How many money you want to deposit : "))
            total_deposit = deposit + total_deposit
            print(f"You deposit {deposit} money.")
            return total_deposit
        else:
            withdraw = float(input("How many money you want to withdraw : "))
            total_withdraw = withdraw + total_withdraw
            print(f"You deposit {withdraw} money.")
            return total_withdraw
    money()
    def display(start_date, end_date, total_deposit, total_withdraw):
        # report()
        # money()
        print("Statement of Account Report:")
        print("Start Date:", start_date)
        print("End Date:", end_date)
        print("Total Deposits:", total_deposit)
        print("Total Withdrawals:", total_withdraw)
    display(start_date, end_date, total_deposit, total_withdraw)

bank_server()
