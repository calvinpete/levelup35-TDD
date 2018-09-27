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
        self.user1_signup = Signup("King", "David", "AnointedKing", "davidking@gmail.com", "psaLms><198?", "124", "male")
        self.user_account = Account()
        self.user_account.register(self.user_signup)
        self.user_account.login("calvinpete", "<!Mario8Funke/>")
        self.user_account.user_profile("calvinpete", "<!Mario8Funke/>")
        self.user_account.edit_user_details("YossiFunke", "Rejo78!ce", "calvinpete", "<!Mario8Funke/>")
