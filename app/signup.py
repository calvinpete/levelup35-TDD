import re


class Signup(object):
    """
    This class holds the validations of user details
    """
    def __init__(self, *args, active=False):
        self.first_name = args[0]
        self.last_name = args[1]
        self.username = args[2]
        self.email_address = args[3]
        self.password = args[4]
        self.age = args[5]
        self.gender = args[6]
        self.active = active

    def full_name(self):
        """
        This combines the first and last name of a user into one name
        :return:
        """
        return "{} {}".format(self.first_name, self.last_name)

    def validate_password(self):
        """
        This method checks if the password matches the preferred pattern
        :return self.password:
        """
        pwd = re.compile("(^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*\W).{4,}$)")
        matcher1 = pwd.match(self.password)
        if matcher1:
            return True
        else:
            raise ValueError("The password should not be less than 4 characters and should "
                             "contain A capital letter, a small letter, a digit and a special character. ")

    def validate_username(self):
        """
        This checks if the username is not less than 4 characters and has no whitespace
        :return self.username:
        """
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
            return True

    def validate_email_address(self):
        """
        This checks for the validity of the email address
        :return self.email_address:
        """
        email = re.compile("(^[a-zA-Z0-9_-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
        email_matcher = email.match(self.email_address)
        if not email_matcher:
            raise ValueError("The email should follow the format of valid emails (johndoe@mail.com)")
        else:
            return True

    def validate_age(self):
        """
        This checks if the age provided is valid
        :return:
        """
        if not self.age.isdigit():
            raise ValueError("The age should not be a character nor should it be less than 0")
        if int(self.age) <= -1:
            raise ValueError("The age should not be a character nor should it be less than 0")
        else:
            return True
