import hashlib
from uuid import uuid4

class User:

    datauser = {}

    def __init__(self, username, password, phone_number=None):
        self.username = username
        self.password = password
        self.phone_number = phone_number
        self.id = uuid4()

    @classmethod
    def signup(cls, username, password, phone_number):
        if username not in cls.datauser:
            password_valid = cls.password_controller(password)
            if password_valid:
                print("Registration successful")
                password = cls.password_maker(password)
                data_dict = cls(username, password, phone_number)
                cls.datauser[username] = data_dict
            else:
                print("Password rules not followed")
        else:
            print("This username is already in use ")

    @classmethod
    def login(cls, username, password):
        if username in cls.datauser:
            if cls.datauser[username].password == cls.password_maker(password):
                print(f'welcome {username}')
                return True
            else:
                print("The password is wrong")
        else:
            print("The username is wrong")

    @classmethod
    def edit_phone_number(cls, phone_number, username):
        if username in cls.datauser:
            cls.datauser[username].phone_number = phone_number
            print("Phone number updated successfully")
        else:
            print("The username is wrong")

    @classmethod
    def edit_password(cls, password, username):
        if username in cls.datauser:
            if cls.password_controller(password):
                hashed_password = cls.password_maker(password)
                cls.datauser[username].password = hashed_password
                print("Password updated successfully")
            else:
                print("Password rules not followed")
        else:
            print("The username is wrong")

    @staticmethod
    def password_controller(password):
        if len(password) >= 4:
            return True
        else:
            return False

    @staticmethod
    def password_maker(password):
        hash_password = hashlib.sha256(password.encode())
        return hash_password.hexdigest()

    def __str__(self):
        return f'{self.username}, {self.phone_number}'

