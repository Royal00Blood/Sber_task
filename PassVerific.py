from FExchange import FExchange


class PassVerification:
    def __init__(self):
        self.__pass = ''
        self.__name = ''

    def __setName(self):
        self.__name = input("Please enter your name")

    def __setPass(self):
        self.__pass = input("Please enter your name")

    def newUser(self):
        self.__setName()
        self.__setPass()

    def logIn(self):
        while True:
            UsName = input(f"Enter your user name: ")
            for i in range(4):
                passUs = input(f"Enter your password{UsName}:")
                if  str.lower(passUs) == str.lower(self.__pass):
                    FExchange()
                else:
                    print(f"You have a mistake! You have {i} attempts left.")



