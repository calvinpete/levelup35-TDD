import unittest
from tests.basetest import BaseTestCase


class TestUser(BaseTestCase):
    """
    This class holds a setup method that creates the demo data to be used to test the program
    """

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

    def test_invalid_password(self):
        with self.assertRaises(ValueError):
            self.user1_signup.validate_password()

    def test_validate_username(self):
        """
        This tests the username validation method
        :return:
        """
        self.assertEqual(self.user_signup.validate_username(), True)
        with self.assertRaises(ValueError):
            self.user4_signup.validate_username()
        with self.assertRaises(ValueError):
            self.user3_signup.validate_username()
        with self.assertRaises(ValueError):
            self.user2_signup.validate_username()
        with self.assertRaises(ValueError):
            self.user1_signup.validate_username()

    def test_validate_email_address(self):
        """
        This tests the email address validation method
        :return:
        """
        self.assertEqual(self.user_signup.validate_email_address(), True)
        with self.assertRaises(ValueError):
            self.user1_signup.validate_email_address()

    def test_validate_age(self):
        """
        This tests the age validation method
        :return:
        """
        self.assertEqual(self.user_signup.validate_age(), True)
        with self.assertRaises(ValueError):
            self.user1_signup.validate_age()
        with self.assertRaises(ValueError):
            self.user2_signup.validate_age()


if __name__ == "__main__":
    unittest.main()
