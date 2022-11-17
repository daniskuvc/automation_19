# Password Generator by DVC

import random, re, os
from io import open

PATH_FILE = os.path.join(os.getcwd(), 'passlist.txt')

def password_generator(): #Returns a string with a randonmly generated password
    pass_chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz"
    pass_chars_len=len(pass_chars)
    pass_len = random.randint(9, 16)
    password=""
    
    for i in range(pass_len):
        password += pass_chars[random.randint(0, pass_chars_len-1)]

    if not re.search(r'[0-9][A-Z][a-z]', password):
        password = password_generator()

    return password


def main_menu(): #Displays main menu options and returns selected option

    return input("""\n
    ---------------------------------
    Password Generator v2.0
    ---------------------------------
    1) Generate password
    2) Get generated password
    3) Exit
    
    Please, select an option: """)
    
def passfile_save(text_to_save):
    file = open(PATH_FILE,'a+')
    #save_pass = account_name + ':' + password_generator() + "\n"
    #file.write(save_pass)
    file.write(text_to_save)
    file.close()

def passfile_read():
    #print(os.getcwd(),os.path.exists(PATH_FILE),PATH_FILE)
    if not os.path.exists(PATH_FILE):
        return ""
    else:
        file = open(PATH_FILE,'r+')
        password_list = file.read()
        file.close()
    #print(password_list, "check")

    return password_list

def passfile_overwrite(account_name, overwrite):
    print(os.path.exists(PATH_FILE))
    if not os.path.exists(PATH_FILE):
        return ""
    else:
        file = open(PATH_FILE,'r+')
        pass_lines = file.readlines()
        
        for line, account in enumerate(pass_lines):
            if account_name in account:
                if overwrite:
                    print(pass_lines[line].split(':')[1])
                    pass_lines[line].split(':')[1] = password_generator() + '\n'
                    break
                else:
                    return account
                
            else:
                return False
        file.seek(0)
        file.writelines(pass_lines) 
        file.close()


def password_exist(account_name):
    get_password = passfile_read()
    if get_password:
        if account_name in get_password:
            for p in get_password.splitlines():
                if account_name in p:
                    return p.split(":")[1]
                    break
    else:
        return False

def account_manager(account_name):
    #print(password_exist(account_name))
    password = password_exist(account_name)
    if password: # existe password
        account_overwrite = input("\n-- The account name you entered already exist. --\nDo you want to overwrite the password? (y/n): ")
        if account_overwrite.lower() == 'y':
            print(f"\n-- The password for \"{account_name}\" account, was updated successfully. --")
        else:
            print("-- Back to menu... --")    
    else:
        passfile_save(account_name + ':' + password_generator() + "\n")
        print(f"\n-- The password for \"{account_name}\" account, was generated successfully. --") 


while (True):

    main_menu_option = main_menu()
    
    if main_menu_option == '1':
        account_name = input("\n-- Generating password. --\nEnter account name: ")
        
        if not account_name:
            print("\nNothing entered.")
        else:
            account_manager(account_name)
 
    elif main_menu_option == '2':
        account_name = input("\n-- Get generated password. --\nPlease enter the name of the account to display the password: ")
        password = password_exist(account_name)
        if password:
            print(f"\nThe password for '{account_name}' account {password}")
        else:
            print(f"\nThe account \"{account_name}\" is not registered.")

    elif main_menu_option =='3':
        print("\n-- Thanks for using this software. Bye! --\n\n")
        break
    else:
        print("\n-- Invalid option. Please provide a number between 1 and 3. --\n")    