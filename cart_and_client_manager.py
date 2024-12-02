from client_NPC_class import ClientNPC
from api_user_class import UserApi
import random

apiUser = UserApi()
npcCartList: list = []
clientDict: dict = apiUser.getUser()

def createNpc(dictClient):
    """
    Del diccionario cliente que se obtiene a traves de la api usuarios se instancian clientes de la clase ClienteNPC
    """
    for key, value in dictClient.items():
        name = value["name"]
        money = value["money"]
        image = value["image"]
        client = ClientNPC(name, money, image)
        npcCartList.append(client)
        
def starterClient(clientList):
    """
    Selecciona aleatoriamente dos clientes únicos de la lista npcCartList para colocarlos en una cola de espera.
    """
    clientsInQueue = []
    while len(clientsInQueue) < 2:
        index = random.randint(0, len(npcCartList) - 1)
        client = npcCartList[index]
        if client not in clientsInQueue:
            clientsInQueue.append(client)
    return clientsInQueue

def initializeNpc():
    """
    Inicializa el proceso de creación e inserción de clientes NPC en una cola.
    1. Crea instancias de ClientNPC utilizando los datos de clientDict.
    2. Selecciona dos clientes únicos de npcCartList para formar una cola.
    """
    createNpc(clientDict)
    clientInQueue: list = starterClient(npcCartList)
    return clientInQueue 
