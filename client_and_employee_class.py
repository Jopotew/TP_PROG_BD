import random
import string
import hashlib
from data_base_class import DataBase


db = DataBase()


class User():
    def __init__(self, name,username, password, mail, image, access_key = None ,manager_access = False):
        self.name = name
        self.password = password
        self.username = username
        self.image = image
        self.mail = mail
        self.manager_access = manager_access
        self.access_key = access_key
        self.create_user_hash()
    """
    HACER QUE GUARDE LA HASH EN UN ARCHIVO PARA DESP BUSCARLA
    """
    def get_username(self):
        return self.username
    
    def create_user_hash(self): #crea el hash y lo guarda en bd
        """
        CUANDO SE CREA EL USER, CREA UN HASH DE TODO LO NECESARIO Y LO GUARDA
        EN LA BASE DE DATOS DIRECTO.
        """
        hash = hashlib.new("SHA256")
        hash.update(self.password.encode())
        hash_pword = (hash.hexdigest())
        if self.manager_access is False:
            user_data = {"NAME": self.name, "USERNAME": self.username, "PASSWORD": hash_pword, "MAIL":self.mail, "IMAGE" : self.image}
            db.insert_product("CLIENT",user_data)
            print(hash.hexdigest())
        elif self.manager_access is True:
            hash.update(self.access_key.encode())
            hash_key = (hash.hexdigest())
            user_data = {"NAME": self.name, "USERNAME": self.username, "PASSWORD": hash_pword, "MAIL":self.mail, "IMAGE" : self.image, "ACCESS_KEY": hash_key, "MANAGER_STATUS": self.manager_access}
            db.insert_product("MANAGER", user_data)
            print(hash.hexdigest())


        
  #HACER PROXIMO
    def check_pw(self): #busca el hash, acorde a la contra, guardado
        pass
    def check_access_key(self):
        pass
    
class Client(User):
    def __init__(self, name , money, username, password, mail, image):
        super().__init__(name, username, password, mail, image)
        self.money: int = money
        self.is_paying: bool = False

class MarketManager(User):
    def __init__(self, name, username, password, mail, image):
        super().__init__(name, username, password, mail, image, access_key = self.generate_access_key(5), manager_access = True)
           
        print(f"Your access key is {self.access_key}") 

    def __str__(self):
        return f"Your access key is {self.access_key}"

    def generate_access_key(self, key_length):# crea una key para el manager
        letters = string.ascii_lowercase
        key = ''.join(random.choice(letters) for i in range(key_length))
        return key

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#             Testing             #

migue = Client("jorge", 99999, "21213131", "2132143425145", "juan@mail.com","imagen.png")
manafer = MarketManager("2312313123","MANAGER_USER", "PASSWORD", "JSJSJSJJS@KDMNKDNK", "ddddd") 
#SOY UNA BESTIA


ddddd= "SOY UNA BESTIAAAAAAAAAAAA"
