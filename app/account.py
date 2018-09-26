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