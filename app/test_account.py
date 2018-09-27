import unittest
from account import Account
from signup import Signup


class TestAccount(unittest.TestCase):
    """
    This class holds a setup method that creates the demo data to be used to test the program
    """

    def setUp(self):
        """
        This method runs before each test by creating object sample data
        :return:
        """
        self.user_signup = Signup("Calvin", "Peter", "calvinpete", "tinkacalvin@gmail.com", "<!Mario8Funke/>", "26",
                                  "male")
        self.user1_signup = Signup("Calvin", "Peter", "YossiFunke", "tinkacalvin@gmail.com", "Rejo78!ce", "26", "male")
        self.user_account = Account()

    def test_creation(self):
        """
        This tests for an instance of the Account class
        :return:
        """
        self.assertIsInstance(self.user_account, Account)

    def test_register(self):
        """
        This tests the register method of the Account class
        :return:
        """
        self.assertEqual(self.user_account.register(self.user_signup), "You've been successfully registered")

    def test_login(self):
        """
        This tests the login method of the Account class
        :return:
        """
        self.user_account.register(self.user_signup)
        self.assertEqual(self.user_account.login("calvinpete", "<!Mario8Funke/>"), True)
        self.assertEqual(self.user_account.login("AnointedKing", "psaLms><198?"), False)
        self.assertEqual(self.user_account.login("calvinpete", "psaLms><198?"), False)

    def test_user_profile(self):
        """
        This tests the user_profile method
        :return:
        """
        self.user_account.register(self.user_signup)
        self.assertDictEqual(self.user_account.user_profile("calvinpete", "<!Mario8Funke/>"),
                             self.user_signup.__dict__
                             )

    def test_edit_user_profile(self):
        """
        This tests the edit_user_profile method
        :return:
        """
        self.user_account.register(self.user_signup)
        self.assertDictEqual(
            self.user_account.edit_user_details("YossiFunke", "Rejo78!ce", "calvinpete", "<!Mario8Funke/>"),
            self.user1_signup.__dict__
        )


if __name__ == "__main__":
    unittest.main()
