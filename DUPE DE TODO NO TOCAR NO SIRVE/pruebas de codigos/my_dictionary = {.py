my_dictionary = {
    "nombre": " Hola",
    "Termotanque": "Chau",
    "Loca": True,
    "otro" :  {
        "otra_clave": "otra_valor",
        "ddd": "ddd",
        }
}


 
items_dict = {
    "item1": {"name": "Laptop", "price": 1200.00, "stock": 10},
    "item2": {"name": "Smartphone", "price": 800.00, "stock": 25},
    "item3": {"name": "Headphones", "price": 150.00, "stock": 50},
    "item4": {"name": "Keyboard", "price": 50.00, "stock": 30},
    "item5": {"name": "Mouse", "price": 25.00, "stock": 45}
}


valor1 = my_dictionary["nombre"]
valor3 = my_dictionary["Loca"]
valor4 = my_dictionary["otro"]["otra_clave"]

my_dictionary.keys()
my_dictionary.values()
print(my_dictionary.items())

item_list = []

class Item:
    """ Items del supermercado """
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name}: ${self.price}"

for key, value in items_dict.items():
   name = value["name"]
   price = value["price"]
   stock = value["stock"]
   item = Item(name, price, stock)
   item_list.append(item)

print(item_list[0])

