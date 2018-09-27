import unittest
from signup import Signup
from account import Account


class TestUser(unittest.TestCase):
    """
    This class holds a setup method that creates the demo data to be used to test the program
    """

    def setUp(self):
        """
        This method runs before each test by creating object sample data
        :return:
        """
        self.user_signup = Signup("Calvin", "Peter", "calvinpete", "tinkacalvin@gmail.com", "<!Mario8Funke/>", 26,
                                  "male")
        self.user_account = Account()
        # user_account.register(user_signup)
        # user_account.login("calvinpete", "<!Mario8Funke/>")
        # user_account.user_profile("calvinpete", "<!Mario8Funke/>")
        # user_account.edit_user_details("YossiFunke", "Rejo78!ce", "calvinpete", "<!Mario8Funke/>")

    def test_creation(self):
        """
        This tests instance of a class
        :return:
        """
        self.assertIsInstance(self.user_signup, Signup)
