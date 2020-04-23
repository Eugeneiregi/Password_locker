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

        def test_init(self):
            '''
            test_init for testing object initialization
            '''

            self.assertEqual(self.new_credentials.account_name, "Facebook")

            self.assertEqual(self.new_credentials.password, "1234567")

            self.assertEqual(self.new_user.first_name, "Eugene")

            self.assertEqual(self.new_user.last_name, "peter")

            self.assertEqual(self.new_user.username, "Iregi")

        def test_view_user(self):
            '''
            method that shows a list of users saved
            '''

            self.assertEqual(User.view_users(), User.user_list)