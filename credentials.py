class Credentials:
    """
    Class that generates new instances of credentials
    """

    credential_list = []


    def __init__(self, account_name, password):
    
        self.account_name = account_name
        self.password = password
