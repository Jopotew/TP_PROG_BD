import random
import time

class Queue():
    """ Cola de clientes """
    def __init__(self):
        self.clientInQueue = []
          
    def enter(self, carrito):
        """ Enters the queue """
        self.clientInQueue.append(carrito)
        print(carrito.client.name, " esta en la cola")

    def leave(self, client):
        """ Leaves the queue """
        self.clientInQueue.remove(client)

    def getQueue(self):
        return self.clientInQueue
    
    # Elimina siempre a la primera persona siempre y cuando su valor isPaying sea True, luego le da el valor True al siguiente
    def popOut(self):
        payTimeout = random.randint(1, 3)
        clientCart = self.getFirst()
        if clientCart.isPaying:  # bool que marca si está para pagar o no
            print(payTimeout)
            print("El cliente", clientCart.client.name, " está pagando.")
            time.sleep(payTimeout)
            self.leave(clientCart)
            self.clientInQueue[0].isPaying = True
        else: 
            print("There are no clients paying")
        
    def getFirst(self):
        return self.clientInQueue[0]
