import pyperclip
class Credential:
    """
    Class that generates new instances of credentials.
    """
    pass

    credential_list = [] # Empty credential lists

    def save_credential(self):

        Credential.credential_list.append(self)

    def delete_credential(self):

        Credential.credential_list.remove(self)

    @classmethod
    def find_by_email(cls,number):

        for credential in cls.credential_list:
            if credential.email == number:
                return credential

    @classmethod
    def credential_exist(cls,number):

        for credential in cls.credential_list:
            if credential.email == number:
                    return True

        return False

    @classmethod
    def display_credentials(cls):

        return cls.credential_list

    @classmethod
    def copy_email(cls,number):
        credential_found = Credential.find_by_email(number)
        pyperclip.copy(credential_found.email)




    def __init__(self,email,platform,password):

      # docstring removed for simplicity

        self.email = email
        self.platform = platform
        self.password = password
