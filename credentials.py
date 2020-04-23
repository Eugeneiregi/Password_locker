class Credentials:
    """
    Class that generates new instances of credentials
    """

    credential_list = []


    def __init__(self, account_name, password):
    
        self.account_name = account_name
        self.password = password


    def __repr__(self):
        return "accountname: %s password: %s" %(self.account_name,self.password)
