from ventanaInicio import venInicio
from ventanaPrincipal import venPrincipal
from ventanaCarrito import venCarrito
from ventanaFila import venFila
from tkinter import Tk, Canvas, Button, PhotoImage

class funciones:
    def __init__(self) -> None:
        
        def verVentanaCarrito():
            venInicio.withdraw() 
            venPrincipal()