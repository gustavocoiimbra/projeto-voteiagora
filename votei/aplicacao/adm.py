from user import User

class Adm(User):

    def __init__(self, first, last, usr, pwd, birth, email, gender, state):
        self.__permit = permit
        super().__init__(first, last, usr, pwd, birth, email, gender, state)

    @property
    def permit(self):
        return permit
    
    @permit.setter
    def permit(self, permit):
        self.__permit = permit