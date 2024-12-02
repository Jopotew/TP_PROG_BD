from userABC_class import userABC
from data_base_class import DataBase
import hashlib

class Client(userABC):
    def __init__(self, name, username, password, mail, image):
        super().__init__(name, username, password, mail, image)
        self.isPaying: bool = False
        
    def getUsername(self):
        return self.username
    
    def createUser(password, name, username, mail, image):
        """
        Función que crea el usuario y lo almacena en la base de datos.
        """
        db = DataBase()
        hashObj = hashlib.new("SHA256")
        hashObj.update(password.encode())
        hashPword = hashObj.hexdigest()
        userData = {"NAME": name, "USERNAME": username, "PASSWORD": hashPword, "MAIL": mail, "IMAGE": image}
        db.insertProduct("CLIENT", userData)
        print(hashObj.hexdigest())
        
    def checkPw(pswrd, username):
        """
        Compara el hash de la contraseña ingresada por el usuario con el hash almacenado en la 
        base de datos.
        """
        db = DataBase()
        hashObj = hashlib.new("SHA256")
        hashObj.update(pswrd.encode())
        password = hashObj.hexdigest()
        print(password)
        table = "CLIENT"
        access: bool = checkUserCredentials(table, password, username)
        return access
        
def checkUserCredentials(table, password, username):
    """
    Función que chequea el hash del password ingresado en el inicio de sesión con el hash creado en 
    el registro de usuario.
    """
    db = DataBase()
    userInfo = db.searchUsername(table, username)
    if not userInfo:
        print("Usuario no encontrado.")
        return False
    storedPswrd = userInfo[0]['PASSWORD']
    if storedPswrd == password:  # Comparar ambos hashes
        print("Credenciales correctas.")
        return True
    else:
        print("Credenciales incorrectas.")
        return False
