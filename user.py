
class User:
    """
    Class that generates new instances of users
    """

    user_list = []

    def __init__(self, first_name, last_name, username):
    
        self.first_name = first_name
        self.last_name = last_name
        self.username = username 