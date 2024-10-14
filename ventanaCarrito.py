import requests
from io import BytesIO
from PIL import Image, ImageTk
from tkinter import Toplevel, Canvas, Button
import queue_manager

class ventanaCarrito:
    def __init__(self, items, carrito) -> None:
        self.ventCarrito = Toplevel()
        width = 600
        height = 450
        screenWidth = self.ventCarrito.winfo_screenwidth()
        screen_Height = self.ventCarrito.winfo_screenheight()
        x = (screenWidth - width) // 2
        y = (screen_Height - height) // 2
        self.ventCarrito.geometry(f"{width}x{height}+{x}+{y}")
        self.ventCarrito.configure(bg = "#F8EDD9")
        self.ventCarrito.title("Portal Compras")

        # Bloque de Canvas
        self.canvas = Canvas(
            self.ventCarrito,
            bg = "#F8EDD9",
            height = 450,
            width = 600,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        self.canvas.place(x = 0, y = 0)

        # Canvas de rectangulos y textos de la ventana
        self.canvas.create_rectangle(0.0, 0.0, 600.0, 74.0, fill="#133020", outline="")
        self.canvas.create_text(75.0, 18.0, anchor="nw", text="Carrito de Compras ", fill="#F8EDD9", font=("Agbalumo Regular", 40 * -1))
        
        itemcarrito = carrito.cart

        if len(carrito.cart) == 1:
            self.imagen1 = itemcarrito[0].image
            response = requests.get(self.imagen1)
            if response.status_code == 200:
                imagen_bytes = BytesIO(response.content)
                imagen = Image.open(imagen_bytes)
                nuevo_tamano = (105, 105)
                imagen_redimensionada = imagen.resize(nuevo_tamano)
                self.imagen_tk1 = ImageTk.PhotoImage(imagen_redimensionada)  # Guardar la referencia
                self.canvas.create_image(134.5, 155.5, image=self.imagen_tk1)

            self.canvas.create_text(200.0, 124.0, anchor="nw", text = f"{itemcarrito[0].name}: ${itemcarrito[0].price}", fill="#000000", font=("Inter", 12 * -1))
            buttonAgregarProduct1 = Button(self.ventCarrito, borderwidth=0, highlightthickness=0,text = "Agregar",bg="#327039", command=lambda: carrito.addItem(itemcarrito[0]))
            buttonAgregarProduct1.place(x=200.0, y=148.0, width=79.0, height=18.0)
            buttonEliminarProduct1 = Button(self.ventCarrito, borderwidth=0, highlightthickness=0,text="Eliminar", bg="#DD5C36", command=lambda: carrito.removeItem(itemcarrito[0]))
            buttonEliminarProduct1.place(x=200.0, y=170.0, width=79.0, height=18.0)
            
        if len(carrito.cart) ==2:
            self.imagen1 = itemcarrito[0].image
            response = requests.get(self.imagen1)
            if response.status_code == 200:
                imagen_bytes = BytesIO(response.content)
                imagen = Image.open(imagen_bytes)
                nuevo_tamano = (105, 105)
                imagen_redimensionada = imagen.resize(nuevo_tamano)
                self.imagen_tk1 = ImageTk.PhotoImage(imagen_redimensionada)  # Guardar la referencia
                self.canvas.create_image(134.5, 155.5, image=self.imagen_tk1)

            self.canvas.create_text(200.0, 124.0, anchor="nw", text = f"{itemcarrito[0].name}: ${itemcarrito[0].price}", fill="#000000", font=("Inter", 12 * -1))
            buttonAgregarProduct1 = Button(self.ventCarrito, borderwidth=0, highlightthickness=0,text = "Agregar",bg="#327039", command=lambda: carrito.addItem(itemcarrito[0]))
            buttonAgregarProduct1.place(x=200.0, y=148.0, width=79.0, height=18.0)
            buttonEliminarProduct1 = Button(self.ventCarrito, borderwidth=0, highlightthickness=0,text="Eliminar", bg="#DD5C36", command=lambda: carrito.removeItem(itemcarrito[0]))
            buttonEliminarProduct1.place(x=200.0, y=170.0, width=79.0, height=18.0)
             
            self.imagen2 = itemcarrito[1].image
            response2 = requests.get(self.imagen2)
            if response2.status_code == 200:
                imagen_bytes = BytesIO(response2.content)
                imagen = Image.open(imagen_bytes)
                nuevo_tamano = (105, 105)
                imagen_redimensionada = imagen.resize(nuevo_tamano)
                self.imagen_tk2 = ImageTk.PhotoImage(imagen_redimensionada)  # Guardar la referencia
                self.canvas.create_image(393.5, 151.5, image=self.imagen_tk2)

            self.canvas.create_text(459, 124.0, anchor="nw", text = f"{itemcarrito[1].name}: ${itemcarrito[1].price}", fill="#000000", font=("Inter", 12 * -1))
            buttonAgregarProduct2 = Button(self.ventCarrito, borderwidth=0, highlightthickness=0,text = "Agregar",bg="#327039", command=lambda: carrito.addItem(itemcarrito[1]))
            buttonAgregarProduct2.place(x=459.0, y=148.0, width=79.0, height=18.0)
            buttonEliminarProduct2 = Button(self.ventCarrito, borderwidth=0, highlightthickness=0,text="Eliminar", bg="#DD5C36", command=lambda: carrito.removeItem(itemcarrito[1]))
            buttonEliminarProduct2.place(x=459.0, y=170.0, width=79.0, height=18.0)
            
        if len(carrito.cart) == 3:
            self.imagen1 = itemcarrito[0].image
            response = requests.get(self.imagen1)
            if response.status_code == 200:
                imagen_bytes = BytesIO(response.content)
                imagen = Image.open(imagen_bytes)
                nuevo_tamano = (105, 105)
                imagen_redimensionada = imagen.resize(nuevo_tamano)
                self.imagen_tk1 = ImageTk.PhotoImage(imagen_redimensionada)  # Guardar la referencia
                self.canvas.create_image(134.5, 155.5, image=self.imagen_tk1)

            self.canvas.create_text(200.0, 124.0, anchor="nw", text = f"{itemcarrito[0].name}: ${itemcarrito[0].price}", fill="#000000", font=("Inter", 12 * -1))
            buttonAgregarProduct1 = Button(self.ventCarrito, borderwidth=0, highlightthickness=0,text = "Agregar",bg="#327039", command=lambda: carrito.addItem(itemcarrito[0]))
            buttonAgregarProduct1.place(x=200.0, y=148.0, width=79.0, height=18.0)
            buttonEliminarProduct1 = Button(self.ventCarrito, borderwidth=0, highlightthickness=0,text="Eliminar", bg="#DD5C36", command=lambda: carrito.removeItem(itemcarrito[0]))
            buttonEliminarProduct1.place(x=200.0, y=170.0, width=79.0, height=18.0)
             
            self.imagen2 = itemcarrito[1].image
            response2 = requests.get(self.imagen2)
            if response2.status_code == 200:
                imagen_bytes = BytesIO(response2.content)
                imagen = Image.open(imagen_bytes)
                nuevo_tamano = (105, 105)
                imagen_redimensionada = imagen.resize(nuevo_tamano)
                self.imagen_tk2 = ImageTk.PhotoImage(imagen_redimensionada)  # Guardar la referencia
                self.canvas.create_image(393.5, 151.5, image=self.imagen_tk2)

            self.canvas.create_text(459, 124.0, anchor="nw", text = f"{itemcarrito[1].name}: ${itemcarrito[1].price}", fill="#000000", font=("Inter", 12 * -1))
            buttonAgregarProduct2 = Button(self.ventCarrito, borderwidth=0, highlightthickness=0,text = "Agregar",bg="#327039", command=lambda: carrito.addItem(itemcarrito[1]))
            buttonAgregarProduct2.place(x=459.0, y=148.0, width=79.0, height=18.0)
            buttonEliminarProduct2 = Button(self.ventCarrito, borderwidth=0, highlightthickness=0,text="Eliminar", bg="#DD5C36", command=lambda: carrito.removeItem(itemcarrito[1]))
            buttonEliminarProduct2.place(x=459.0, y=170.0, width=79.0, height=18.0)
          
            self.imagen3 = itemcarrito[2].image
            response3 = requests.get(self.imagen3)
            if response3.status_code == 200:
                imagen_bytes = BytesIO(response3.content)
                imagen = Image.open(imagen_bytes)
                nuevo_tamano = (105, 105)
                imagen_redimensionada = imagen.resize(nuevo_tamano)
                self.imagen_tk3 = ImageTk.PhotoImage(imagen_redimensionada)  # Guardar la referencia
                self.canvas.create_image(134.5, 298.0, image=self.imagen_tk3)

            self.canvas.create_text(200.0, 266.0, anchor="nw", text = f"{itemcarrito[2].name}: ${itemcarrito[2].price}", fill="#000000", font=("Inter", 12 * -1))
            buttonAgregarProduct3 = Button(self.ventCarrito, borderwidth=0, highlightthickness=0,text = "Agregar",bg="#327039", command=lambda: carrito.addItem(itemcarrito[2]))
            buttonAgregarProduct3.place(x=200.0, y=290.0, width=79.0, height=18.0)
            buttonEliminarProduct3 = Button(self.ventCarrito, borderwidth=0, highlightthickness=0,text="Eliminar", bg="#DD5C36", command=lambda: carrito.removeItem(itemcarrito[2]))
            buttonEliminarProduct3.place(x=200.0, y=312.0, width=79.0, height=18.0)
            
        if len(carrito.cart) >= 4:
            self.imagen1 = itemcarrito[0].image
            response = requests.get(self.imagen1)
            if response.status_code == 200:
                imagen_bytes = BytesIO(response.content)
                imagen = Image.open(imagen_bytes)
                nuevo_tamano = (105, 105)
                imagen_redimensionada = imagen.resize(nuevo_tamano)
                self.imagen_tk1 = ImageTk.PhotoImage(imagen_redimensionada)  # Guardar la referencia
                self.canvas.create_image(134.5, 155.5, image=self.imagen_tk1)

            self.canvas.create_text(200.0, 124.0, anchor="nw", text = f"{itemcarrito[0].name}: ${itemcarrito[0].price}", fill="#000000", font=("Inter", 12 * -1))
            buttonAgregarProduct1 = Button(self.ventCarrito, borderwidth=0, highlightthickness=0,text = "Agregar",bg="#327039", command=lambda: carrito.addItem(itemcarrito[0]))
            buttonAgregarProduct1.place(x=200.0, y=148.0, width=79.0, height=18.0)
            buttonEliminarProduct1 = Button(self.ventCarrito, borderwidth=0, highlightthickness=0,text="Eliminar", bg="#DD5C36", command=lambda: carrito.removeItem(itemcarrito[0]))
            buttonEliminarProduct1.place(x=200.0, y=170.0, width=79.0, height=18.0)
             
            self.imagen2 = itemcarrito[1].image
            response2 = requests.get(self.imagen2)
            if response2.status_code == 200:
                imagen_bytes = BytesIO(response2.content)
                imagen = Image.open(imagen_bytes)
                nuevo_tamano = (105, 105)
                imagen_redimensionada = imagen.resize(nuevo_tamano)
                self.imagen_tk2 = ImageTk.PhotoImage(imagen_redimensionada)  # Guardar la referencia
                self.canvas.create_image(393.5, 151.5, image=self.imagen_tk2)

            self.canvas.create_text(459, 124.0, anchor="nw", text = f"{itemcarrito[1].name}: ${itemcarrito[1].price}", fill="#000000", font=("Inter", 12 * -1))
            buttonAgregarProduct2 = Button(self.ventCarrito, borderwidth=0, highlightthickness=0,text = "Agregar",bg="#327039", command=lambda: carrito.addItem(itemcarrito[1]))
            buttonAgregarProduct2.place(x=459.0, y=148.0, width=79.0, height=18.0)
            buttonEliminarProduct2 = Button(self.ventCarrito, borderwidth=0, highlightthickness=0,text="Eliminar", bg="#DD5C36", command=lambda: carrito.removeItem(itemcarrito[1]))
            buttonEliminarProduct2.place(x=459.0, y=170.0, width=79.0, height=18.0)
          
            self.imagen3 = itemcarrito[2].image
            response3 = requests.get(self.imagen3)
            if response3.status_code == 200:
                imagen_bytes = BytesIO(response3.content)
                imagen = Image.open(imagen_bytes)
                nuevo_tamano = (105, 105)
                imagen_redimensionada = imagen.resize(nuevo_tamano)
                self.imagen_tk3 = ImageTk.PhotoImage(imagen_redimensionada)  # Guardar la referencia
                self.canvas.create_image(134.5, 298.0, image=self.imagen_tk3)

            self.canvas.create_text(200.0, 266.0, anchor="nw", text = f"{itemcarrito[2].name}: ${itemcarrito[2].price}", fill="#000000", font=("Inter", 12 * -1))
            buttonAgregarProduct3 = Button(self.ventCarrito, borderwidth=0, highlightthickness=0,text = "Agregar",bg="#327039", command=lambda: carrito.addItem(itemcarrito[2]))
            buttonAgregarProduct3.place(x=200.0, y=290.0, width=79.0, height=18.0)
            buttonEliminarProduct3 = Button(self.ventCarrito, borderwidth=0, highlightthickness=0,text="Eliminar", bg="#DD5C36", command=lambda: carrito.removeItem(itemcarrito[2]))
            buttonEliminarProduct3.place(x=200.0, y=312.0, width=79.0, height=18.0)
                       
            self.imagen4 = itemcarrito[3].image
            response4 = requests.get(self.imagen4)
            if response4.status_code == 200:
                imagen_bytes = BytesIO(response4.content)
                imagen = Image.open(imagen_bytes)
                nuevo_tamano = (105, 105)
                imagen_redimensionada = imagen.resize(nuevo_tamano)
                self.imagen_tk4 = ImageTk.PhotoImage(imagen_redimensionada)  # Guardar la referencia
                self.canvas.create_image(393.5, 298.0, image=self.imagen_tk4)

            self.canvas.create_text(459.0, 264.0, anchor="nw", text = f"{itemcarrito[3].name}: ${itemcarrito[3].price}", fill="#000000", font=("Inter", 12 * -1))
            buttonAgregarProduct4 = Button(self.ventCarrito, borderwidth=0, highlightthickness=0,text = "Agregar",bg="#327039", command=lambda: carrito.addItem(itemcarrito[3]))
            buttonAgregarProduct4.place(x=459.0, y=290.0, width=79.0, height=18.0)
            buttonEliminarProduct4 = Button(self.ventCarrito, borderwidth=0, highlightthickness=0,text="Eliminar", bg="#DD5C36", command=lambda: carrito.removeItem(itemcarrito[3]))
            buttonEliminarProduct4.place(x=459.0, y=312.0, width=79.0, height=18.0)

        # Bloque de Buttons
        #este boton sollamente te dirige a la siguiente ventana, en la ventana sigueitne se deben de inicar los metodos, o podemos inicar payment en la otra ventana, me aprece mejor
        def pagar():
            fila = queue_manager.initializeQueue(carrito)
            # ESTO SE DEBE DE MANDAR A LA OTR VENTANA
            # pago = queue_manager.initialize_payment(carrito, fila)
            newVentana(items, carrito, fila)
            
        def newVentana (items, carrito, fila):
            self.ventCarrito.withdraw()
            from ventanaFila import ventanaFila
            ventanaFila(items, carrito, fila)
            
        buttonPagar = Button(self.ventCarrito, borderwidth=0, highlightthickness=0,text = "Pagar Compra",bg="#F0BE49", command=pagar, relief="flat")
        buttonPagar.place(x=238.0, y=384.0, width=126.0, height=36.0)

        def volver():
            self.ventCarrito.withdraw()
            from ventanaPrincipal import ventanaPrincipal
            ventanaPrincipal(items, carrito)

        buttonVolver = Button(self.ventCarrito, borderwidth=0, highlightthickness=0,bg="#133020",fg="#FFFFFF", text="Volver", command =volver, relief="flat")
        buttonVolver.place(x=13.0, y=402.0, width=60.0, height=25.0)


        def cerrar():
            print("Cerrando ventana...")
            exit(0)
        self.ventCarrito.protocol("WM_DELETE_WINDOW", cerrar)
        self.ventCarrito.resizable(False, False)
        self.ventCarrito.mainloop()