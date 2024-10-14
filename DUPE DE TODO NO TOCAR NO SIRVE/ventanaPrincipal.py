from io import BytesIO
from pathlib import Path
import requests
from tkinter import Toplevel, Canvas, Button, messagebox
from PIL import Image, ImageTk

class ventanaPrincipal:
    def __init__(self, items, carrito) -> None:
        self.venPrincipal = Toplevel()
        width = 600
        height = 450
        screenWidth = self.venPrincipal.winfo_screenwidth()
        screenHeight = self.venPrincipal.winfo_screenheight()
        x = (screenWidth - width) // 2
        y = (screenHeight - height) // 2
        self.venPrincipal.geometry(f"{width}x{height}+{x}+{y}")
        self.venPrincipal.configure(bg = "#F8EDD9")
        self.venPrincipal.title("Portal Compras")

        itemMercado = items
        
        self.canvas = Canvas(
            self.venPrincipal,
            bg = "#F8EDD9",
            height = height,
            width = width,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        
        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            0.0,
            0.0,
            600.0,
            74.0,
            fill="#133020",
            outline="")

        self.canvas.create_text(
            210.0,
            18.0,
            anchor="nw",
            text="Productos ",
            fill="#F8EDD9",
            font=("Agbalumo Regular", 40 * -1),
            justify = "center"
        )

#posiciones, imagen1=134.5, 155.5 / imagen2=134.5, 298.0 / imagen3 = 393.5, 151.5 / imagen4 = 393.5, 298.0
#imagen producto 1
        self.imagen1 = itemMercado[0].image
        response = requests.get(self.imagen1)
        if response.status_code == 200:
            imagen_bytes = BytesIO(response.content)
            imagen = Image.open(imagen_bytes)
            nuevo_tamano = (105, 105)
            imagen_redimensionada = imagen.resize(nuevo_tamano)
            self.imagen_tk1 = ImageTk.PhotoImage(imagen_redimensionada)  # Guardar la referencia
            self.canvas.create_image(134.5, 155.5, image=self.imagen_tk1)

#imagen producto 2
        self.imagen2 = itemMercado[1].image
        response2 = requests.get(self.imagen2)
        if response2.status_code == 200:
            imagen_bytes = BytesIO(response2.content)
            imagen = Image.open(imagen_bytes)
            nuevo_tamano = (105, 105)
            imagen_redimensionada = imagen.resize(nuevo_tamano)
            self.imagen_tk2 = ImageTk.PhotoImage(imagen_redimensionada)  # Guardar la referencia
            self.canvas.create_image(393.5, 151.5, image=self.imagen_tk2)

#imagen producto 3
        self.imagen3 = itemMercado[2].image
        response3 = requests.get(self.imagen3)
        if response3.status_code == 200:
            imagen_bytes = BytesIO(response3.content)
            imagen = Image.open(imagen_bytes)
            nuevoTamano = (105, 105)
            imagenRedimensionada = imagen.resize(nuevoTamano)
            self.imagen_tk3 = ImageTk.PhotoImage(imagenRedimensionada)  # Guardar la referencia
            self.canvas.create_image(134.5, 298.0, image=self.imagen_tk3)

#imagen producto 4
        self.imagen4 = itemMercado[3].image
        response4 = requests.get(self.imagen4)
        if response4.status_code == 200:
            imagen_bytes = BytesIO(response4.content)
            imagen = Image.open(imagen_bytes)
            nuevo_tamano = (105, 105)
            imagen_redimensionada = imagen.resize(nuevo_tamano)
            self.imagen_tk4 = ImageTk.PhotoImage(imagen_redimensionada)  # Guardar la referencia
            self.canvas.create_image(393.5, 298.0, image=self.imagen_tk4)

#Primer boton de cambio de ventana
        def newVentana():
            if not carrito.cart:  # Verifica si el carrito está vacío
                messagebox.showerror("ERROR", "Debes agregar ítems al carrito antes de continuar.")
            else:
                self.venPrincipal.withdraw()
                from ventanaCarrito import ventanaCarrito
                ventanaCarrito(items, carrito)

        self.buttonIrCarrito = Button(
            self.venPrincipal,
            borderwidth=0,
            text = "Carrito de Compras",
            bg = "#F0BE49",
            highlightthickness=0,
            command = newVentana,
            relief="flat"
        )
        self.buttonIrCarrito.place(
            x=237.0,
            y=384.0,
            width=152.0,
            height=36.0
        )

#PRODUCTO 1
        self.nombreProducto1 = itemMercado[0].name
        self.precioProdcuto1 = itemMercado[0].price
        self.canvas.create_text(
            200.0,
            134.0,
            anchor="nw",
            text=f"{self.nombreProducto1}: ${self.precioProdcuto1}",
            fill="#000000",
            font=("Inter", 12 * -1)
        )
        self.buttonAgregarPro1 = Button(
            self.venPrincipal,
            borderwidth=0,
            text = "Agregar",
            bg = "#327039",
            highlightthickness=0,
            command=lambda:carrito.addItem(itemMercado[0]),
            relief="flat"
        )
        self.buttonAgregarPro1.place(
            x=197.0,
            y=156.0,
            width=79.0,
            height=18.0
        )

#PRODUCTO 2
        self.nombreProducto2 = itemMercado[1].name
        self.precioProdcuto2 = itemMercado[1].price
        self.canvas.create_text(
            459.0,
            134.0,
            anchor="nw",
            text=f"{self.nombreProducto2}: ${self.precioProdcuto2}",
            fill="#000000",
            font=("Inter", 12 * -1)
        )
        self.buttonAgregarPro2 = Button(
            self.venPrincipal,
            borderwidth=0,
            text = "Agregar",
            bg = "#327039",
            highlightthickness=0,
            command=lambda:carrito.addItem(itemMercado[1]),
            relief="flat"
        )
        self.buttonAgregarPro2.place(
            x=459.0,
            y=156.0,
            width=79.0,
            height=18.0
        )

#PRODCUTO 3
        self.nombreProducto3 = itemMercado[2].name
        self.precioProdcuto3 = itemMercado[2].price
        self.canvas.create_text(
            200.0,
            276.0,
            anchor="nw",
            text=f"{self.nombreProducto3}: ${self.precioProdcuto3}",
            fill="#000000",
            font=("Inter", 12 * -1)
        )
        self.buttonAgregarPro3 = Button(
            self.venPrincipal,
            borderwidth=0,
            text = "Agregar",
            bg = "#327039",
            highlightthickness=0,
            command=lambda:carrito.addItem(itemMercado[2]),
            relief="flat"
        )
        self.buttonAgregarPro3.place(
            x=197.0,
            y=298.0,
            width=79.0,
            height=18.0
        )

#PRODUCTO 4
        self.nombreProducto4 = itemMercado[3].name
        self.precioProdcuto4 = itemMercado[3].price
        self.canvas.create_text(
            459.0,
            274.0,
            anchor="nw",
            text=f"{self.nombreProducto4}: ${self.precioProdcuto4}",
            fill="#000000",
            font=("Inter", 12 * -1)
        )
        self.buttonAgregarPro4 = Button(
            self.venPrincipal,
            borderwidth=0,
            text = "Agregar",
            bg = "#327039",
            highlightthickness=0,
            command=lambda:carrito.addItem(itemMercado[3]),
            relief="flat"
        )
        self.buttonAgregarPro4.place(
            x=459.0,
            y=298.0,
            width=79.0,
            height=18.0
        )
        
        
        def cerrar():
            print("Cerrando ventana...")
            exit(0)
        self.venPrincipal.protocol("WM_DELETE_WINDOW", cerrar)
        self.venPrincipal.resizable(False, False)
        self.venPrincipal.mainloop()

