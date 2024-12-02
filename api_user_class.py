import requests

class UserApi:
    def __init__(self):
        self.url = 'https://66e98b5187e417609449e408.mockapi.io/verduleria/clientes'
        self.users = self.getUser()
        
    def getUser(self):
        """
        La siguiente funcion toma los datos de la api Usuarios y crea un diccionario de todos los clientes de esa api
        """
        response = requests.get(self.url)
        items = response.json()
        
        if isinstance(items, list) and len(items) > 0:
            dictApi = items[0]  # Accedemos al primer objeto en el array
            diccionarioClientes = {}
            for i, (key, value) in enumerate(dictApi.items()):
                diccionarioClientes[f"Client{i+1}"] = {
                    "name": value["name"],
                    "money": value["money"],
                    "image": value["image"]
                }
            return diccionarioClientes
        else:
            print("No se encontraron productos.")
            return {}
