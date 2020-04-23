import unittest
from user import User
from credentials import Credentials

class TestUser(unittest.TestCase):
    '''
    Test class for user class
    '''

if __name__== '__main__':
    unittest.main()

    def setUp(self):
        '''
        test to run before each test cases
        '''

        self.new_credentials = Credentials("Facebook", "1234567")
        self.new_user = User("Eugene", "peter", "Iregi")