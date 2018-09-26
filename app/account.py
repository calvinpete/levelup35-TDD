class Account:
    """
    This class holds the functionality of managing a user account
    """
    def __init__(self):
        self.accounts = []  # A data structure to store user accounts

    def register(self, user):
        """
        This saves an account created by a user
        :param user:
        :return:
        """
        self.accounts.append(user)
        print("You've been successfully registered")

    def login(self, username, password):
        """
        This allows a user to sign in to his or her account
        :param username:
        :param password:
        :return:
        """
        for i in self.accounts:
            if i.__getattribute__("username") != username:
                print("Please input the right username")
                return False

            if i.__getattribute__("password") != password:
                print("Please enter the correct password")
                return False
            else:
                i.__dict__["active"] = True
                return True
