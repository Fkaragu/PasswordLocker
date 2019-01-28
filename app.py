#!/usr/bin/env python3.6
from user import User

from credential import Credential

def create_user(fname,lname,phone,email):

    new_user = User(fname,lname,phone,email)
    return new_user

def create_credential(email,platform,password):

    new_credential = Credential(email,platform,password)
    return new_credential

def save_users(user):

    user.save_user()

def save_credential(credential):

    credential.save_credential()

def del_user(user):

    user.delete_user()

def delete_credential(user):

    user.delete_credential()

def find_user(number):

    return User.find_by_number(number)

def find_credential(number):

    return Credential.find_by_email(number)

def check_existing_users(number):

    return User.user_exist(number)

def check_existing_credential(number):

    return Credential.credential_exist(number)

def display_users():

    return User.display_users()

def display_credential():

    return Credential.display_credential()

def test_copy_email():

    return User.copy_email()

def test_copy_email():

    return Credential.copy_email()

def main():

    print("Hello Welcome to your user list. What is your name?")

    user_name = input()

    print(f"Hello {user_name}. what would you like to do")

    print('\n')

    while True:

        print("Use these short codes : ")
        print("CU - Create a New User")
        print("DU - Display Users")
        print("FU - Find a User")
        print("CA - Create Social Account")
        print("DA - Display Social Account")
        print("DE - Delete Social Account")
        print("EX - Exit the list")

        short_code = input().lower()

        if short_code   == 'cu':

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

        elif short_code == 'du':

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

        elif short_code == 'fu':

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

        elif short_code == 'ca':

            print("Do you want password to auto-generate.. Use below options")
            print("Option 1: YY -- Yes")
            print("Option 2: NN -- No")
            print("Option 3: EX -- Exit the Social Accounts")

            pass_auto = input().lower()

            if pass_auto == 'yy':
                print("Password will be auto generated")

            elif pass_auto =='nn':

                print ("Enter Email Address (Username)....")
                e_mail = input()

                print("Platform Account (Social Account)...")
                p_account = input()

                print("Enter Password ...")
                p_word = input()

                save_credential(create_credential(e_mail,p_account,p_word))

                print ('\n')

                print(f" New Credential for {e_mail} {p_account} created")

                print ('\n')

            elif pass_auto == "ex":

                print("Bye .......")


            else:
                print("Wrong option try again")

                print("Do you want password to auto-generate.. Use below options")
                print("Option 1: YY -- Yes")
                print("Option 2: NN -- No")
                print("Option 3: EX -- Exit the Social Accounts")

                pass_auto = input().lower()

        elif short_code == 'da':

            if display_credential():
                print("Here is a list of all your credential")

                print('\n')

                for credential in display_credential():

                        print(f"{credential.email} {credential.platform} .....{credential.password}")

                        print('\n')

            else:

                print('\n')

                print("You don't seem to have any credentials saved yet")

                print('\n')

        elif short_code == "ex":

            print("Bye .......")

            break

        else:

            print("I really didn't get that. Please use the short codes")


if __name__ == '__main__':

    main()
