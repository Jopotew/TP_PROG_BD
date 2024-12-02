class ClientNPC:
    def __init__(self, name , money, image, is_paying = False):
        self.name = name
        self.money = money
        self.image = image
        self.is_paying = is_paying