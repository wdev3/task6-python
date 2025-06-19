import os
import time
import generator

password_list = []
username_list = []
file_username_list = []
file_password_list = []
logged_in = False

class Account:
    def __init__(self, owner, balance):
        self.__balance = balance
        self.owner = owner

    def get_balance(self):
        return self.__balance
    
    def show_balance(self):
        print(f"Your current balance is {self.__balance}")

    def add_balance(self):
        self.__balance += amount_add

    def withdraw_balance(self):
       if p > self.__balance:
          print("Insufficient balance")
       else:
          self.__balance -= amount_withdraw


# Create or generate password
def create_password():
    while True:
        print("Create - 1")
        print("Generate - 2")
        try:
            option = int(input("Create or generate a password? \n"))
            os.system("cls")
        except ValueError:
            print("Enter only 1 or 2")
            time.sleep(1)
            os.system("cls")
            continue
        except KeyboardInterrupt:
            print("Copy using your mouse")
            time.sleep(1)
            os.system("cls")
            continue

        if option == 2:
            generated = generator.password_generator()
            print(generated)
            password_list.append(generated)
            print("Copy this password")
            with open("account.txt", "a") as file:
                file.write(generated + "\n")
            time.sleep(4)
            os.system("cls")
            break

        elif option == 1:
            os.system("cls")
            print("Password must be between 6 and 15 characters")
            custom_password = input("")
            if len(custom_password) < 6:
                print("Password too short")
                time.sleep(1)
                os.system("cls")
            elif len(custom_password) > 15:
                print("Password too long")
                time.sleep(1)
                os.system("cls")
            else:
                password_list.append(custom_password)
                os.system("cls")
                print("Password created")
                time.sleep(1)
                os.system("cls")
                with open("account.txt", "a") as file:
                    file.write(custom_password + "\n")
                break
        else:
            print("Enter only 1 or 2")
            time.sleep(1)
            os.system("cls")


# Create username
def create_username():
    user = input("Enter your username:\n")
    username_list.append(user)
    with open("account.txt", "a") as file:
        file.write(user + "\n")
    time.sleep(1)
    os.system("cls")


def menu():
    print("1 - Check balance")
    print("2 - Deposit")
    print("3 - Withdraw")
    print("4 - Change password")
    print("0 - Exit")


# Check if account exists
def account_exists():
    global logged_in
    question = input("Do you already have an account? \n")
    if question.lower() == "yes":
        os.system("cls")
        if os.path.exists("account.txt"):
            with open("account.txt", "r") as file:
                lines = file.readlines()
                if len(lines) >= 2:
                    username = lines[0].strip()
                    password = lines[1].strip()

                    file_username_list.append(username)
                    file_password_list.append(password)

                    print("Do you want to login with this account?")
                    print(username)
                    print(password)

                    confirm = input("")
                    if confirm.lower() == "no":
                        logged_in = False
                        os.system("cls")
                    if confirm.lower() == "yes":
                        logged_in = True
                    return True
                else:
                    print("File incomplete. Create a new account.")
                    return False
        else:
            print("No account found")
            return False
    elif question.lower() == "no":
        os.system("cls")
        print("Let's create a new account")
        time.sleep(2)
        os.system("cls")
        return False
    else:
        print("Invalid answer. Type 'yes' or 'no'.")
        return False


bank = Account("User", 0)

account_exists()

if not logged_in:
    create_username()
    create_password()

if not logged_in:
    while True:
        user1 = input("Enter your username (1 of 3)\n")
        if user1 in username_list or user1 in file_username_list:
            os.system("cls")
            break
        else:
            time.sleep(1)
            os.system("cls")
            print("Incorrect username!")
            user2 = input("Enter your username (2 of 3)\n")
            if user2 in username_list or user2 in file_username_list:
                os.system("cls")
                break
            else:
                time.sleep(1)
                os.system("cls")
                print("Incorrect username!")
                user3 = input("Enter your username (3 of 3)\n")
                if user3 in username_list or user3 in file_username_list:
                    os.system("cls")
                    break
                else:
                    print("Incorrect username!")
                    print("You have been blocked")
                    exit()

    while True:
        pass1 = input("Enter your password (1 of 3)\n")
        if pass1 in password_list or pass1 in file_password_list:
            os.system("cls")
            menu()
            break
        else:
            os.system("cls")
            print("Incorrect password!")
            pass2 = input("Enter your password (2 of 3)\n")
            if pass2 in password_list or pass2 in file_password_list:
                os.system("cls")
                menu()
                break
            else:
                os.system("cls")
                print("Incorrect password!")
                pass3 = input("Enter your password (3 of 3)\n")
                if pass3 in password_list or pass3 in file_password_list:
                    os.system("cls")
                    menu()
                    break
                else:
                    os.system("cls")
                    print("Incorrect password!")
                    print("You have been blocked")
                    exit()
else:
    menu()


while True:
    try:
        p = int(input())
    except ValueError:
        os.system("cls")
        print("Enter a valid number")
        time.sleep(1)
        os.system("cls")
        menu()
        continue

    if p == 1:
        bank.show_balance()
        time.sleep(1)
        os.system("cls")
        menu()

    elif p == 2:
        os.system("cls")
        try:
            amount_add = int(input("How much do you want to deposit?\n"))
        except ValueError:
            print("Enter a valid number")
            time.sleep(1)
            os.system("cls")
            menu()
            continue

        print(f"You added {amount_add} to your account")
        bank.add_balance()
        time.sleep(2)
        os.system("cls")
        menu()

    elif p == 3:
        pass_withdraw = input("Enter your password\n")
        os.system("cls")
        if pass_withdraw in password_list or pass_withdraw in file_password_list:
            try:
                amount_withdraw = int(input("How much do you want to withdraw?\n"))
            except ValueError:
                print("Enter a valid number")
                time.sleep(1)
                os.system("cls")
                menu()
                continue

            print(f"You withdrew {amount_withdraw} from your account")
            time.sleep(2)
            os.system("cls")
            bank.withdraw_balance()
            os.system("cls")
            menu()
        else:
            print("Incorrect password!")
            time.sleep(2)
            os.system("cls")
            menu()

    elif p == 4:
        current_pass = input("Enter your current password (1 of 3)\n")
        if current_pass in password_list or current_pass in file_password_list:
            new_pass = input("Enter your new password\n")
            password_list.clear()
            password_list.append(new_pass)
            os.system("cls")
            menu()
        else:
            print("Wrong password (1)")
            time.sleep(2)
            os.system("cls")
            menu()

    elif p == 0:
        print("Closing...")
        time.sleep(3)
        os.system("cls")
        break

    else:
        os.system('cls')
        print("Invalid option")
        time.sleep(1)
        os.system("cls")
        menu()
