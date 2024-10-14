import random
import string

class Person():
    def __init__(self, name, image):
        self.name = name
        self.image = image

class Client(Person):
    def __init__(self, name, image, money):
        super().__init__(name, image)
        self.money: int = money
        self.is_paying: bool = False

class MarketManager(Person):
    def __init__(self, name, image):
        super().__init__(name, image)
        self.manager_access: bool = True
        self.access_key = self.generate_access_key(5)  
        

    def __str__(self):
        return f"Your access key is {self.access_key}"

    def generate_access_key(self, key_length):
        letters = string.ascii_lowercase
        key = ''.join(random.choice(letters) for i in range(key_length))
        return key


manager = MarketManager("John Doe", "image_url.png")
jorge = MarketManager("Manolo", "")
print(manager.access_key)
print(jorge.access_key)
print(jorge)