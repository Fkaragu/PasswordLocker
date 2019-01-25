import unittest # Importing the unittest module
from userClass import User # Importing the User class

class TestContact(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.user_list = User("Francis","Karagu","0712345678","fkaragu@gmail.com") # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.user_list.first_name,"Francis")
        self.assertEqual(self.user_list.last_name,"Karagu")
        self.assertEqual(self.user_list.phone_number,"0712345678")
        self.assertEqual(self.user_list.email,"fkaragu@gmail.com")


if __name__ == '__main__':
    unittest.main()
