"""Controlador de items"""
from store import Item
import random
from api_manager import Product
from store import SuperMarket
from data_base_class import DataBase
from data_base_class import DataBase


apiProducts = Product()
itemList: list = []
data_base = DataBase() 
db_product = data_base.create_items()

def createItem(db_product):
    
    for product in db_product:
       
        name = product["NAME"]
        price = product["PRICE"]
        category = product["ID_CATEGORY"]
        image = product["IMAGE"]
        stock = product["STOCK"]
        new_product = {"NAME": name, "PRICE": price, "STOCK": stock, "ID_CATEGORY": category ,"IMAGE": image}
        data_base.insert_product("PRODUCT", new_product)
        item = Item(name, price, stock, category, image)
        itemList.append(item)
        print(itemList)
    
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
    createItem(db_product)
    itemInShelf = selectItem(itemList)
    market = putItemInShelf(itemInShelf)
    print("Productos agregados al mercado")
    return market