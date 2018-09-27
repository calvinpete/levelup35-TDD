import unittest
from account import Account
from signup import Signup


class TestUser(unittest.TestCase):
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
        self.user1_signup = Signup("Mark", "Ronald", "Mark", "markronald.com", "marky", "-6", "male")
        self.user2_signup = Signup("Lonah", "Jemah", "Jemah", "Jemah8lo@hotmail.com", "j9W>olgm", "hjh", "male")
        self.user2_signup = Signup("King", "David", "King David", "davidking@gmail.com", "psaLms198?", "124", "male")
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

    def test_full_name(self):
        """
        This tests if a full name is created
        :return:
        """
        self.assertEqual(self.user_signup.full_name(), "Calvin Peter")

    def test_validate_password(self):
        """
        This tests the password validation method
        :return:
        """
        self.assertEqual(self.user_signup.validate_password(), True)
        with self.assertRaises(ValueError):
            self.user1_signup.validate_password()

