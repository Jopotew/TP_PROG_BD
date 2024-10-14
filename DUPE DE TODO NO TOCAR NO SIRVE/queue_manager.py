"""QUEUE MANAGER"""

from queue_class import Queue
import cart_and_client_manager

CartMangr = cart_and_client_manager

def initializeQueue(client):
    queue = Queue()  # TAMBIEN SE PODRIA HACER QUE SE PASE LA LISTA DE NPCS ANTES. NOC
    for npc in CartMangr.initializeNpc():
        queue.enter(npc)
    queue.enter(client)
    for npc in CartMangr.initializeNpc():
        queue.enter(npc)
    for npc in CartMangr.initializeNpc():
        queue.enter(npc)
    queue.getFirst().isPaying = True
    print(queue.clientInQueue[0].isPaying)
    print(queue.clientInQueue[2].isPaying)
    print(queue.clientInQueue[4].isPaying)
    return queue

def removeFromQueue(queue):  # elimina de cola
    queue.popOut()
