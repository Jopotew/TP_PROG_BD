import requests
from io import BytesIO
from pathlib import Path
from tkinter import Toplevel, Canvas, Button, messagebox
from PIL import Image, ImageTk  # Importamos las clases necesarias de Pillow
import queue_manager
import cart_and_client_manager

class ventanaFila:
    def __init__(self, items, carrito, fila) -> None:
    
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Spectre\Documents\UB\Segundo\Prog3\PARCIAL\build\assets\frame0")
        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        self.venFila = Toplevel()
        self.venFila.geometry("600x450")
        width = 600
        height = 450
        screen_width = self.venFila.winfo_screenwidth()
        screen_height = self.venFila.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.venFila.geometry(f"{width}x{height}+{x}+{y}")
        self.venFila.configure(bg="#FFFFFF")
        
        self.canvas = Canvas(
            self.venFila,
            bg="#FFFFFF",
            height=450,
            width=600,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(
            0.0,
            0.0,
            600.0,
            74.0,
            fill="#133020",
            outline="")

        image_path = relative_to_assets("cajaregistradora.jpg") 
        imagen1 = Image.open(image_path) 
        imagen1 = imagen1.resize((105, 171))
        self.imagen1_tk = ImageTk.PhotoImage(imagen1)  # Mantener la referencia de la imagen
        self.canvas.create_image(
            355.0,  # Coordenada X
            315.0,  # Coordenada Y
            image=self.imagen1_tk,
            anchor="center"  # Imagen convertida para Tkinter
        )
        
        self.canvas.create_text(
            143.0,
            18.0,
            anchor="nw",
            text="Fila para abonar",
            fill="#F8EDD9",
            font=("Agbalumo Regular", 40 * -1)
        )

        # Almacenar las referencias de las imágenes de los clientes
        self.imagen_tk1 = None
        self.imagen_tk2 = None
        self.imagen_tk3 = None
        self.imagen_tk4 = None

        # Dibujar imágenes de los clientes al iniciar
        self.dibujarImagenes(fila)

        
        def iniciarPago(fila, carrito):
            while len(fila.clientInQueue) > 5:
                self.dibujarImagenes(fila)
                self.venFila.update()
                queue_manager.removeFromQueue(fila)
                self.dibujarImagenes(fila)
                self.venFila.update()
            self.dibujarImagenes(fila)
            self.venFila.update()
            pagar = messagebox.showinfo("Turno de Pago", f"Es tu turno de pagar. El total de tu compra es de ${cart_and_client_manager.cartCost(carrito)}\n¿Deseas abonar el total de la compra?")
            if pagar:
                print("Programa finalizado.")
                self.venFila.quit()
                self.venFila.destroy()
                exit(0)

        def volver():
            self.venFila.withdraw()
            from ventanaCarrito import ventanaCarrito
            ventanaCarrito(items, carrito)

        buttonVolver = Button(self.venFila, borderwidth=0, highlightthickness=0, fg="#FFFFFF", command=volver, relief="flat", text="Volver", bg="#133020")
        buttonVolver.place(x=13.0, y=402.0, width=60.0, height=25.0)

        buttonIniciarPayment = Button(self.venFila, borderwidth=0, highlightthickness=0, fg="#FFFFFF", command=lambda: iniciarPago(fila,carrito), relief="flat", text="Iniciar Pago", bg="#F0BE49")
        buttonIniciarPayment.place(x=315, y=402.0, width=100, height=30.0)

        def cerrar():
            print("Cerrando ventana...")
            exit(0)

        self.venFila.protocol("WM_DELETE_WINDOW", cerrar)
        self.venFila.resizable(False, False)
        self.venFila.mainloop()

    def dibujarImagenes(self, fila):
        #CLIENTE 4
        self.imagen1 = fila.clientInQueue[3].client.image
        response = requests.get(self.imagen1)
        if response.status_code == 200:
            imagen_bytes = BytesIO(response.content)
            imagen = Image.open(imagen_bytes)
            nuevo_tamano = (105, 105)
            imagen_redimensionada = imagen.resize(nuevo_tamano)
            self.imagen_tk1 = ImageTk.PhotoImage(imagen_redimensionada)  # Guardar la referencia
            self.canvas.create_image(103.0, 173.0, image=self.imagen_tk1)

        #CLIENTE 3
        self.imagen2 = fila.clientInQueue[2].client.image
        response2 = requests.get(self.imagen2)
        if response2.status_code == 200:
            imagen_bytes = BytesIO(response2.content)
            imagen = Image.open(imagen_bytes)
            nuevo_tamano = (105, 105)
            imagen_redimensionada = imagen.resize(nuevo_tamano)
            self.imagen_tk2 = ImageTk.PhotoImage(imagen_redimensionada)  # Guardar la referencia
            self.canvas.create_image(220.0, 173.0, image=self.imagen_tk2)

        #CLIENTE 2
        self.imagen3 = fila.clientInQueue[1].client.image
        response3 = requests.get(self.imagen3)
        if response3.status_code == 200:
            imagen_bytes = BytesIO(response3.content)
            imagen = Image.open(imagen_bytes)
            nuevoTamano = (105, 105)
            imagenRedimensionada = imagen.resize(nuevoTamano)
            self.imagen_tk3 = ImageTk.PhotoImage(imagenRedimensionada)  # Guardar la referencia
            self.canvas.create_image(337.0, 173.0, image=self.imagen_tk3)

        #CLIENTE PAGANDO
        self.imagen4 = fila.clientInQueue[0].client.image
        response4 = requests.get(self.imagen4)
        if response4.status_code == 200:
            imagen_bytes = BytesIO(response4.content)
            imagen = Image.open(imagen_bytes)
            nuevo_tamano = (105, 105)
            imagen_redimensionada = imagen.resize(nuevo_tamano)
            self.imagen_tk4 = ImageTk.PhotoImage(imagen_redimensionada)  # Guardar la referencia
            self.canvas.create_image(503.0, 334.0, image=self.imagen_tk4)
