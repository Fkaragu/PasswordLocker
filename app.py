#!/usr/bin/env python3.6
from user import User

def create_user(fname,lname,phone,email):

    new_user = User(fname,lname,phone,email)
    return new_user

def save_users(user):

    user.save_user()

def del_user(user):

    user.delete_user()

def find_user(number):

    return User.find_by_number(number)

def check_existing_users(number):

    return User.user_exist(number)

def display_users():

    return User.display_users()

def test_copy_email():

    return User.copy_email()

def main():

    print("Hello Welcome to your user list. What is your name?")

    user_name = input()

    print(f"Hello {user_name}. what would you like to do")

    print('\n')

    while True:

        print("Use these short codes : cc - create a new user, dc - display users, fc -find a user, ex -exit the user list ")

        short_code = input().lower()

        if short_code == 'cc':

            print("New User")
            print("-"*10)

            print ("First name ....")
            f_name = input()

            print("Last name ...")
            l_name = input()

            print("Phone number ...")
            p_number = input()

            print("Email address ...")
            e_address = input()

            save_users(create_user(f_name,l_name,p_number,e_address))

            print ('\n')

            print(f"New User {f_name} {l_name} created")

            print ('\n')

        elif short_code == 'dc':

            if display_users():

                print("Here is a list of all your users")

                print('\n')

                for user in display_users():

                    print(f"{user.first_name} {user.last_name} .....{user.phone_number}")

                print('\n')

            else:

                print('\n')

                print("You dont seem to have any users saved yet")

                print('\n')

        elif short_code == 'fc':

            print("Enter the number you want to search for")

            search_number = input()

            if check_existing_users(search_number):

                search_user = find_user(search_number)

                print(f"{search_user.first_name} {search_user.last_name}")

                print('-' * 20)


                print(f"Phone number.......{search_user.phone_number}")

                print(f"Email address.......{search_user.email}")

            else:

                 print("That user does not exist")

        elif short_code == "ex":

            print("Bye .......")

            break

        else:

            print("I really didn't get that. Please use the short codes")


if __name__ == '__main__':

    main()
