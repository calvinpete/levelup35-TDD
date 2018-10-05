import unittest
from app.account import Account
from app.signup import Signup


class BaseTestCase(unittest.TestCase):
    """
    This class holds a setup method that creates the demo data to be used to test the program
    """

    def setUp(self):
        """
        This method runs before each test by creating object sample data
        :return:
        """
        self.user_signup = Signup(
            "Calvin", "Peter", "calvinpete", "tinkacalvin@gmail.com", "<!Mario8Funke/>", "26", "male"
        )
        self.user1_signup = Signup("Mark", "Ronald", "Mark", "markronald.com", "marky", "-6", "male")
        self.user2_signup = Signup("Lonah", "Jemah", "Jemah", "Jemah8lo@hotmail.com", "j9W>olgm", "hjh", "male")
        self.user3_signup = Signup(
            "King", "David", "King David", "davidking@gmail.com", "psaLms198?", "124", "male"
        )
        self.user4_signup = Signup("Harvey", "Moses", "M H", "MH@gmail.com", "suQ3?kdright", "34", "male")
        self.user5_signup = Signup(
            "Calvin", "Peter", "YossiFunke", "tinkacalvin@gmail.com", "Rejo78!ce", "26", "male"
        )
        self.user_account = Account()

    def test_account_creation(self):
        """
        This tests for an instance of the Account class
        :return:
        """
        self.assertIsInstance(self.user_account, Account)

    def test_signup_creation(self):
        """
        This tests instance of a class
        :return:
        """
        self.assertIsInstance(self.user_signup, Signup)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
