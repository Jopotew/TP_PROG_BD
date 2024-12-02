from userABC_class import userABC
from data_base_class import DataBase
import random
import string
import hashlib

class Manager(userABC):
    def __init__(self, name, username, password, mail, image):
        super().__init__(name, username, password, mail, image)
    
    def getUsername(self):
        return self.username
    
    def createUser(password, name, username, mail, image):
        """
        Se crea un usuario nuevo obteniendo los datos desde los Entry de la ventana y se escriben todos
        los datos en la tabla correspondiente.
        """
        db = DataBase()
        hash = hashlib.new("SHA256")
        hash.update(password.encode())
        hashPword = hash.hexdigest()
        accessKey = generateAccessKey(5)
        #print(f"Your access key is {accessKey}")
        hash.update(accessKey.encode())
        hashKey = hash.hexdigest()
        userData = {'NAME': name, 'USERNAME': username, 'PASSWORD': hashPword, 'MAIL': mail, 'IMAGE': image, 'ACCESS_KEY': hashKey}
        db.insertProduct('MANAGER', userData)
        return accessKey

    def checkPw(pswrd, username, hashKey):
        """
        Compara el hash de la contraseña y la access key ingresada por el usuario con el 
        hash almacenado en la base de datos.
        """
        hash2 = hashlib.new("SHA256")
        hash2.update(pswrd.encode())
        password = hash2.hexdigest()
        hash2.update(hashKey.encode())
        hashedKey = hash2.hexdigest()
        #print(password)
        access = checkUserCredentials('MANAGER', password, username, hashedKey)
        return access

def generateAccessKey(keyLength):
    """
    Genera automáticamente una access key para el manager, de 5 caracteres entre la "A" y la "Z".
    """
    letters = string.ascii_lowercase
    key = ''.join(random.choice(letters) for i in range(keyLength))
    return key
        
def checkUserCredentials(table, password, username, hashKey):
    """
    Función que permite o no el acceso del usuario ingresado chequeando el password y la access key.
    Ambas son comparadas en base a su hash que se obtiene desde la Base de Datos.
    """
    db = DataBase()
    userInfo = db.searchUsername(table, username)
    if not userInfo:
        print("Usuario no encontrado.")
        return False
    storedPswrd = userInfo[0]['PASSWORD']
    storedManKey = userInfo[0]['ACCESS_KEY']
    if storedPswrd == password and hashKey == storedManKey:
        #print("Credenciales correctas.")
        return True
    else:
        #print("Credenciales incorrectas.")
        return False
