class User:
    def __init__(self, id_account):
        self.__id = id_account
        self.name = None
        self.email = None
        self.password = None
        self.followers = []
        self.following = []
        self.posts = []

    def get_name(self):
        first_name = input("First name: ")
        family_name = input("Family name: ")

        self.name = first_name.capitalize() + " " + family_name.capitalize()

    def get_email(self):
        self.email = input("Email: ")

    def get_password(self):
        password_try_1 = None
        valid = False

        while not valid:
            password_try_1 = input("Enter password: ")
            password_try_2 = input("Re-enter password: ")
            if password_try_1 == password_try_2:
                valid = True
            else:
                print("Passwords do not match, please try again!")

        self.password = password_try_1

    @property
    def id(self):
        return self.__id

    @property
    def secret_password(self):
        return self.password