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

        def test_view_credentials(self):
            '''
            method to view user credentials
            '''

            self.assertEqual(Credentials.view_credentials(), Credentials.credential_list)
        def test_save_credentials(self):
            '''
            test to see if credential object is saved into the credential list
            '''

            self.new_credentials.save_credentials()

            self.assertEqual(len(Credentials.credential_list), 1)

        def test_save_user(self):
            '''
            test to see if contact object is saved into the credential list
            '''

            self.new_user.save_user()

            self.assertEqual(len(User.user_list), 1)


        def tearDown(self):
            '''
            Clean up for tests
            '''

            Credentials.credential_list = []

            User.user_list = []

        def test_save_mulltiple_credentials(self):
            '''
            test_save_multiple credentials to check if we can save multiple credentials object to our credentials_list
            '''

            self.new_credentials.save_credentials()
            test_credentials = Credentials("Ig", "32667843")
            test_credentials.save_credentials()

            self.assertEqual(len(Credentials.credential_list), 2)