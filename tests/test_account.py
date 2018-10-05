import unittest
from tests.basetest import BaseTestCase


class TestAccount(BaseTestCase):
    """
    This class holds a setup method that creates the demo data to be used to test the program
    """

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
            self.user5_signup.__dict__
        )


if __name__ == "__main__":
    unittest.main()
