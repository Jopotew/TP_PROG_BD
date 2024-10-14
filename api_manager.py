import requests

class User:
    def __init__(self):
        self.url = 'https://66e98b5187e417609449e408.mockapi.io/verduleria/clientes'
        self.users = self.getUser()
        
    def getUser(self):
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


class Product:
    def __init__(self):
        self.url = 'https://66e98b5187e417609449e408.mockapi.io/verduleria/verduleria'
        self.products = self.getProduct()  # Llama a initialize al inicializar

    def getProduct(self):
        response = requests.get(self.url)
        items = response.json()
        
        if isinstance(items, list) and len(items) > 0:
            dictApi = items[0]  # Accedemos al primer objeto en el array
            diccionarioProductos = {}
            for i, (key, value) in enumerate(dictApi.items()):
                diccionarioProductos[f"Item{i+1}"] = {
                    "name": value["name"],
                    "price": value["price"],
                    "image": value["image"]
                }
            return diccionarioProductos
        else:
            print("No se encontraron productos.")
            return {}
