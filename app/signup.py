import re

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

    def validate_password(self):
        pwd = re.compile("(^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*\W).{4,}$)")
        matcher1 = pwd.match(self.password)
        if matcher1:
            return self.password
        else:
            raise ValueError("The password should not be less than 4 characters and should "
                             "contain A capital letter, a small letter, a digit and a special character. ")

    def validate_username(self):
        usr_name = re.compile("(^\S{4,}$)")
        matcher2 = usr_name.match(self.username)
        if not matcher2:
            raise ValueError("The username should not be less than 4 characters and have no whitespaces")
        if self.username == self.first_name:
            raise ValueError("The username should not be your first name")
        if self.username == self.last_name:
            raise ValueError("The username should not be your last name")
        if self.username == self.full_name():
            raise ValueError("The username should not be your full name")
        else:
            return self.username


# if __name__ == "__main__":
#     calvin = Signup("Calvin", "Peter", "Calvin", "tinkacalvin@gmail.com",
#                     0-773-548-160, "<#HOLY!spirit@17>", 26, "P.O Box 3080", "male")
#     calvin.validate_username()
