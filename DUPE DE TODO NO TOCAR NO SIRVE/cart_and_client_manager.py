from client_&_employee_class import Client
from store import ShoppingCartSinDescuento
from api_manager import User
import random


def initializeCartClient(nombreCliente):
    name = nombreCliente  # le otorgo el valor de una variable que se obtiene de la ventana de inicio
    money = random.randint(9999, 9999999)
    image = "https://th.bing.com/th/id/OIP.hcRhDT8KVqzySjYJmBhlzgHaHa?rs=1&pid=ImgDetMain"
    client = Client(name, money, image)  # saltaba error porque el client tiene una imagen asignada, tengo que ver que lo tome como corresponda, le asigno una imagen random al usuario.
    clientCart = ShoppingCartSinDescuento(client)
    print(f"Carrito creado exitosamente! {name}")
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
