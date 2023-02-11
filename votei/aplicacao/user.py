#from aplicacao import db

class User():
#class User(db.Model):
    """    Classe usuário, projeto votei   """

    counter = 0

    def __init__(self, first, last, usr, pwd, birth, email, gender, state):
        User.counter += 1
        self.__id = User.counter
        self.__firstName = first
        self.__lastName = last
        self.__userName = usr
        self.__password = pwd
        self.__dateOfBirth = birth
        self.__email = email
        self.__gender = gender
        self.__state = state

    @property
    def id(self):
        return self.__id

    @property
    def firstName(self):
        return self.__firstName

    @firstName.setter
    def firstName(self, first):
        self.__firstName = first

    @property
    def lastName(self):
        return self.__lastName

    @lastName.setter
    def lastName(self, last):
        self.__lastName = last

    @property
    def userName(self):
        return self.__userName

    @userName.setter
    def userName(self, usr):
        self.__userName = usr

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, pwd):
        self.__pwd = pwd

    @property
    def dateOfBirth(self):
        return self.__dateOfBirth

    @dateOfBirth.setter
    def dateOfBirth(self, birth):
        self.__dateOfBirth = birth

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender):
        self.__gender = gender

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, st):
        self.__state = st