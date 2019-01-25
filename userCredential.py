class Credential:
    """
    Class that generates new instances of credential.
    """

    credential_list = [] # Empty credential list

    def __init__(self,platform,account_name,password):

      # docstring removed for simplicity

        self.platform = platform
        self.account_name = account_name
        self.password = password