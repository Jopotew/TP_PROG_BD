from abc import ABC, abstractmethod

class userABC(ABC):
    def __init__(self, name,username, password, mail, image, accessKey = None ,managerAccess = False):
        self.name = name
        self.password = password
        self.username = username
        self.image = image
        self.mail = mail
        self.managerAccess = managerAccess
        self.accessKey = accessKey
              
    @property
    def password(self):
        return self.password2
    
    @password.setter
    def password(self, password):
        if len(password) < 8:
            raise ValueError("La contraseña debe tener al menos 8 caracteres.")
        self.password2 = password
    
    @abstractmethod    
    def getUsername(self):
        return self.username
    
    @abstractmethod
    def createUser():
        pass

    @abstractmethod
    def checkPw():
        pass