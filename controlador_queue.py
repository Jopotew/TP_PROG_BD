from queue_class import Queue
import cart_and_client_manager

clientNPC = cart_and_client_manager

def initializeQueue(client):
    '''
    Funcion que crea la cola para luego abonar. La fila sigue el siguiente formato:
    2 CLIENTE NPC
    CLIENTE
    2 CLIENTE NPC
    Cuando se encuntra en la primera posicion se establece el atributo is_paying a TRUE y se lo quita de 
    la cola
    '''
    queue = Queue()  # TAMBIEN SE PODRIA HACER QUE SE PASE LA LISTA DE NPCS ANTES. NOC
    for npc in clientNPC.initializeNpc():
        queue.enter(npc)
    queue.enter(client)
    for npc in clientNPC.initializeNpc():
        queue.enter(npc)
    for npc in clientNPC.initializeNpc():
        queue.enter(npc)
    queue.getFirst().is_paying = True
    #print(queue.clientInQueue[0].is_paying)
    #print(queue.clientInQueue[2].is_paying)
    #print(queue.clientInQueue[4].is_paying)
    return queue

def removeFromQueue(queue):
    '''
    Funcion que elimina el cliente que esta pagando de la fila luego de x tiempo
    '''
    queue.popOut()