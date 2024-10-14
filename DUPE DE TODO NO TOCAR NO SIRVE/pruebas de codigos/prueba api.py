import requests

class Users:
    def _init_(self):
        self.url = 'https://66e98b5187e417609449e408.mockapi.io/verduleria/clientes'

    def get_users(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            print(response.json())
            return response.json() 
        else:
            return {"error": "No se pudieron obtener los usuarios"}

class Products:
    def _init_(self):
        self.url = 'https://66e98b5187e417609449e408.mockapi.io/verduleria/verduleria'

    def get_products(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "No se pudieron obtener los productos"}


item = Products.get_products
print(item)