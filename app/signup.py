class Signup:
    """
    This class registers to user
    """
    def __init__(self, first_name, last_name, username, email_address,
                 phone_number, password, age, postal_address, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email_address = email_address
        self.phone_number = phone_number
        self.password = password
        self.age = age
        self.postal_address = postal_address
        self.gender = gender

    def full_name(self):
        """
        This combines the first and last name of a user into one name
        :return:
        """
        return "{} {}".format(self.first_name, self.last_name)
