import pyperclip
class User:
    """
    Class that generates new instances of user.
    """

    user_list = [] # Empty user list

    def save_user(self):
    User.user_list.append(self)

    def delete_user(self):
    User.user_list.remove(self)

    @classmethod
        def find_by_number(cls,number):

            for contact in cls.user_list:
                if contact.phone_number == number:
                    return contact
    @classmethod
        def contact_exist(cls,number):

            for contact in cls.user_list:
                if contact.phone_number == number:
                    return True

                    return False

    def __init__(self,first_name,last_name,number,email):

      # docstring removed for simplicity

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = number
        self.email = email
