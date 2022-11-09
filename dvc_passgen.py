# Password Generator by Daniel Villarroel Chanlopkova
# passgen v.1.0

from io import open
import random, re

pass_chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz"
pass_chars_len=len(pass_chars)
pass_len = random.randint(9, 16)

def password_generator():
    password=""
    for i in range(pass_len):
        password += pass_chars[random.randint(0, pass_chars_len-1)]

    if not re.search(r'[0-9][A-Z][a-z]', password):
        password_generator()

    return password

password_list={}

def create_account_password(account_name):
    if not password_list.get(account_name):
        print(f"\nThe password for \"{account_name}\" account, was generated successfully.")
        password_list[account_name] = password_generator()
    else:
        while (True):
            account_name_choice = input("""\nThe account name you entered already exist.
            \tWhat do you want to do?
            \t1) Update existing password
            \t2) New account and password
            \t3) Back to Main Menu
            Please, select an option:_ """)

            if account_name_choice == '1':
                print(f"\nThe password for \"{account_name}\" account, was updated successfully.")
                password_list[account_name] = password_generator()

            elif account_name_choice == '2':
                print("\n2) New account and password.\nPlease enter the name of the account to generate the password:_ ")
                account_name = input("\n2) New account and password.\nPlease enter the name of the account to generate the password: ")
                create_account_password(account_name)
            elif account_name_choice == '3':
                break
            else:
                print("Back to menu...")

#print(password_generator())

while (True):
    print("\n" + "-"*20)
    print("Password Generator by DVC")
    print("-"*20 + "\n")
    print("""\tMain Menu:
    \t1) Generate password
    \t2) Get generated password
    \t3) Exit""")
    main_menu_option = input("Please, select an option:_ ")
    if main_menu_option == '1':
        account_name = input("\n1) Generate password.\nPlease enter the name of the account to generate the password or type 'back()' to back to previous menu: ")
        
        if account_name.lower() == "back()".lower() or not account_name:
            print("Back to menu...")
        else:
            create_account_password(account_name)
 
    elif main_menu_option == '2':
        get_password = input("\n2) Get generated password.\nPlease enter the name of the account to display the password: ")

        if get_password and password_list.get(get_password) and password_list: 
            print(f"\nThe password for {get_password} is {password_list.get(get_password)}")
        else:
            print(f"\nThe account \"{get_password}\" does not exist.")


    elif main_menu_option =='3':
        print("\nYour passwords list is beeing saved to a password.txt file.\nThanks for using this software. Bye!\n\n")
        password_file=open("password.txt","w")
        password_file.write(str(password_list))
        password_file.close()

        break
    else:
        print("\nInvalid option. Please provide a number between 1 and 3.\n")    