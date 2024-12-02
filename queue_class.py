import random
import time

class Queue():
    """ Cola de clientes """
    def __init__(self):
        self.clientInQueue = []
          
    def enter(self, client):
        """ Enters the queue """
        self.clientInQueue.append(client)
        print(client.name, " esta en la cola")

    def leave(self, client):
        """ Leaves the queue """
        self.clientInQueue.remove(client)

    def getQueue(self):
        return self.clientInQueue
    
    # Elimina siempre a la primera persona siempre y cuando su valor isPaying sea True, luego le da el valor True al siguiente
    def popOut(self):
        payTimeout = random.randint(1, 3)
        client = self.getFirst()
        if client.is_paying:  # bool que marca si está para pagar o no
            print(payTimeout)
            print("El cliente", client.name, " está pagando.")
            time.sleep(payTimeout)
            self.leave(client)
            self.clientInQueue[0].is_paying = True
        else: 
            print("There are no clients paying")
        
    def getFirst(self):
        return self.clientInQueue[0]