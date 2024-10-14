from abc import ABC, abstractmethod

""" - Contiene las clases relacionadas con el supermercado, el carrito y los ítems - """
class Item:
    """ Items del supermercado """
    def __init__(self, name, price, stock, image):
        self.name = name
        self.price = price
        self._stock = stock if stock > 0 else 1
        self.image = image

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, stockNuevo):
        if stockNuevo > 0:
            self._stock = stockNuevo
        else:
            raise ValueError("El stock debe ser mayor que 0.")

    def __str__(self):
        return f"{self.name}: ${self.price}, Stock : {self.stock}"

class ShoppingCartAbstracto(ABC):
    """ Carrito de compras """
    def __init__(self, client):
        self.cart = []
        self.client = client
        self.isPaying: bool = client.isPaying
    
    @abstractmethod
    def addItem(self, item):
        pass

    @abstractmethod
    def removeItem(self, item):
        pass
        
    @abstractmethod  
    def getCart(self):
        pass
    
    @abstractmethod
    def getTotalPrice(self):
        pass
    
    @abstractmethod
    def clearCart(self):
        pass

class ShoppingCartConDescuento(ShoppingCartAbstracto):
    """ Carrito de compras """
    def __init__(self, client):
        super().__init__(client=client)
        self.cart = []
        self.client = client
        self.isPaying: bool = client.isPaying
    
    def addItem(self, item):
        self.cart.append(item)
        print(f"El cliente {self.client.name} añade el producto {item} al carrito")

    def removeItem(self, item):
        self.cart.remove(item)
        print(f"El cliente {self.client.name} elimina el producto {item} del carrito")
        
    def getCart(self):
        return self.cart
    
    def getTotalPrice(self):
        compraTotal = sum(item.price for item in self.cart)
        totalFinal = compraTotal * 0.90  # se aplica un 10% a la compra total
        return totalFinal
    
    def clearCart(self):
        self.cart.clear()
        print(f"El cliente {self.client.name} ha vaciado su carrito")
        
class ShoppingCartSinDescuento(ShoppingCartAbstracto):
    """ Carrito de compras """
    def __init__(self, client):
        super().__init__(client=client)
        self.cart = []
        self.client = client
        self.isPaying: bool = client.isPaying
    
    def addItem(self, item):
        self.cart.append(item)
        print(f"El cliente {self.client.name} añade el producto {item} al carrito")

    def removeItem(self, item):
        self.cart.remove(item)
        print(f"El cliente {self.client.name} elimina el producto {item} del carrito")
        
    def getCart(self):
        return self.cart
    
    def getTotalPrice(self): 
        return sum(item.price for item in self.cart)
    
    def clearCart(self):
        self.cart.clear()
        print(f"El cliente {self.client.name} ha vaciado su carrito")

class SuperMarket:
    """ Supermercado """
    def __init__(self):
        self.items = []
        
    def addItem(self, item):
        self.items.append(item)
        
    def removeItem(self, item):
        self.items.remove(item)
    
    def getItems(self):
        return self.items
