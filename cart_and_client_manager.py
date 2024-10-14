from client_and_employee_class import Client
from store import ShoppingCartSinDescuento
from api_manager import User
import random


def initializeCartClient(client_name, username,mail, password):
    money = random.randint(9999, 9999999)
    image = "https://th.bing.com/th/id/OIP.hcRhDT8KVqzySjYJmBhlzgHaHa?rs=1&pid=ImgDetMain"
    client = Client(client_name, money, username, password, mail, image)  
    clientCart = ShoppingCartSinDescuento(client)
    print(f"Carrito creado exitosamente! {client_name}")
    return clientCart

apiUser = User()
npcCartList: list = []
clientDict: dict = apiUser.getUser()

def createNpc(dictClient):
    for key, value in dictClient.items():
        name = value["name"]
        money = value["money"]
        image = value["image"]
        client = Client(name, money, image)
        npcCart = ShoppingCartSinDescuento(client)
        npcCartList.append(npcCart)
        
def starterClient(clientList):
    clientsInQueue = []
    while len(clientsInQueue) < 2:
        index = random.randint(0, len(npcCartList) - 1)
        client = npcCartList[index]
        if client not in clientsInQueue:
            clientsInQueue.append(client)
    return clientsInQueue


def initializeNpc():  # Devuelve la lista de 2 clientes
    createNpc(clientDict)
    clientInQueue: list = starterClient(npcCartList)
    return clientInQueue 

def cartCost(clientCart):  # CALCULA EL PRECIO DEL CARRITO
    return clientCart.getTotalPrice()
