"""Controlador de items"""
from store import Item
import random
from api_manager import Product
from store import SuperMarket
from data_base_class import DataBase


apiProducts = Product()
itemList: list = []
itemDict: dict = apiProducts.getProduct()
data_base = DataBase() 
print(itemDict.items())
def createItem(itemDict):
    for key, value in itemDict.items():
        name = value["name"]
        price = value["price"]
        image = value["image"]
        
        stock = random.randint(1, 10)
        new_product = {"NAME": name, "PRICE": price, "STOCK": stock, "IMAGE": image}
        data_base.insert_product("PRODUCT", new_product)
        item = Item(name, price, stock, image)
        itemList.append(item)
    
def selectItem(itemList):
    itemInShelf = []
    while len(itemInShelf) < 4:
        index = random.randint(0, len(itemList) - 1)
        item = itemList[index]
        if item not in itemInShelf:
            itemInShelf.append(item)
    return itemInShelf

def putItemInShelf(itemList):
    market = SuperMarket()
    for item in itemList:
        market.addItem(item)
    return market

def initializeItem():  # Devuelve el mercado con sus items
    createItem(itemDict)
    itemInShelf = selectItem(itemList)
    market = putItemInShelf(itemInShelf)
    print("Productos agregados al mercado")
    return market
