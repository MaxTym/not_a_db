import csv
import os
import sys
from data_base import NotDataBase


def login(db):
    while True:
        user_login = input("Enter your user name or 'q' to quit: ")
        if user_login == 'q':
            sys.exit()
        else:
            for i in db.data:
                if i.split(',')[0] == user_login:
                    password = input("Enter a password: ")
                    if i.split(',')[1] == password:
                        return user_login
                        break
            else:
                print("Wrong username/password")

def check_user_list(user_login, db):
    for i in db.data:
        if i.split(',')[0] == user_login:
            return True


def add_new_user(db):
    new_user = ''
    while True:
        add_user_name = input("Enter a user_name or 'q' to quit: ")
        if check_user_list(add_user_name, db):
            print("User name {} already exist".format(add_user_name))
            continue
        else:
            new_user += add_user_name + ','
            break
    add_password = input("Enter a password: ")
    new_user += add_password + ','
    add_full_name = input("Enter a full name: ")
    new_user += add_full_name + ','
    add_pn = input("Enter a phone number: ")
    new_user += add_pn + ','
    while True:
        add_more = (input("Want to add more data?\n 'Y'/'n' ")).lower()
        if add_more == 'y':
            more_data = input("Enter additional info: ")
            new_user += more_data + ','
        elif add_more == 'n':
            break
    return new_user


def main_menu(db, user_login):
    os.system('clear')
    choice = input("To see my info -- '1'\nTo add new user -- '2'\nTo update my info -- '3'\nTo log out -- '4'\nTo quit -- 'q'")
    if choice == '1':
        show_data(db, user_login)
        navigate(db, user_login)
    elif choice == '3':
        new_user = update_my_info(db, user_login)
        db.add(new_user)
        print("Your info was successfully updated")
        navigate(db, user_login)
    elif choice == '2':
        new_user = add_new_user(db)
        db.add(new_user)
        print("User '{}' was successfully added".format(new_user.split(',')[0]))
        navigate(db, user_login)
    elif choice == '4':
        main()
    elif choice == 'q':
        sys.exit()


def update_my_info(db, user_login):
    new_user = ''
    new_user += user_login + ','
    for i in db.data:
        if i.split(',')[0] == user_login:
            to_remove = (db.data.index(i))
            password = i.split(',')[1]
    while True:
        password_change = input("Would you like to change a password?\n 'Y'/'n'").lower()
        if password_change == 'y':
            verify_password = input("Verify your password: ")
            if verify_password == password:
                new_password = input("Enter a new password: ")
                new_password_verify = input("Confirm a new password: ")
                if new_password == new_password_verify:
                    password = new_password
                    new_user += password + ','
                    break
        else:
            break
    add_full_name = input("Enter a full name: ")
    new_user += add_full_name + ','
    add_pn = input("Enter a phone number: ")
    new_user += add_pn + ','
    while True:
        add_more = (input("Want to add more data?\n 'Y'/'n' ")).lower()
        if add_more == 'y':
            more_data = input("Enter additional info: ")
            new_user += more_data + ','
        elif add_more == 'n':
            break
    db.remove(to_remove)
    return new_user



def show_data(db, user_login):
    for k, v in enumerate(db):
        if (v.split(',')[0]) == user_login:
            print(v.split(',')[2:])


def navigate(db, user_login):
    while True:
        navigate = input("Go to main menu - enter '1'\nLog out - enter '2'\nQuit - enter 'q'")
        if navigate == '1':
            main_menu(db, user_login)
        elif navigate == '2':
            main()
        elif navigate == 'q':
            exit()


def main():
    os.system('clear')
    db = NotDataBase()
    user_login = login(db)
    main_menu(db, user_login)


if __name__ == "__main__":
    main()
