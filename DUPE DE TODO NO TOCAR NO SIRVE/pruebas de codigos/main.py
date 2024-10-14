from pathlib import Path
from tkinter import Toplevel, Canvas, Button
from PIL import Image, ImageTk
import item_manager
import requests
from io import BytesIO

class ventanaPrincipal:
    def __init__(self) -> None:
        # Inicializar el mercado y obtener los productos
        market = item_manager.initialize_item()
        items_in_market = market.items  # Lista de productos en el mercado
        
        self.venPrincipal = Toplevel()
        width = 600
        height = 450
        screen_width = self.venPrincipal.winfo_screenwidth()
        screen_height = self.venPrincipal.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.venPrincipal.geometry(f"{width}x{height}+{x}+{y}")
        self.venPrincipal.configure(bg = "#F8EDD9")
        self.venPrincipal.title("Portal Compras")

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
        self.canvas.create_rectangle(0.0, 0.0, 600.0, 74.0, fill="#133020", outline="")
        self.canvas.create_text(210.0, 18.0, anchor="nw", text="Productos ", fill="#F8EDD9", font=("Agbalumo Regular", 40 * -1), justify="center")

        # Crear los rectángulos donde mostrar las imágenes
        posiciones = [(82, 103, 187, 208), (341, 99, 446, 204), (82, 245, 187, 351), (341, 245, 446, 351)]
        self.imagenes = []

        for i, item in enumerate(items_in_market[:4]):  # Mostrar solo los primeros 4 productos
            x0, y0, x1, y1 = posiciones[i]
            self.canvas.create_rectangle(x0, y0, x1, y1, fill="#D9D9D9", outline="")
            
            # Obtener la imagen del producto desde la URL
            url_imagen = item.image
            response = requests.get(url_imagen)
            if response.status_code == 200:
                img_data = BytesIO(response.content)
                img = Image.open(img_data)
                img = img.resize((x1 - x0, y1 - y0), Image.ANTIALIAS)
                imagen_tk = ImageTk.PhotoImage(img)
                
                # Mostrar la imagen
                self.canvas.create_image((x0 + x1) // 2, (y0 + y1) // 2, image=imagen_tk)
                self.imagenes.append(imagen_tk)  # Guardar la referencia a la imagen para que no se recoja por el garbage collector
            
            # Mostrar el nombre del producto
            self.canvas.create_text(x0 + 115, y0 + 30, anchor="nw", text=item.name, fill="#000000", font=("Inter", 12 * -1))

        def newVentana():
            self.venPrincipal.withdraw()
            from ventanaCarrito import ventanaCarrito
            ventanaCarrito()

        self.buttonIrCarrito = Button(
            self.venPrincipal,
            borderwidth=0,
            text = "Carrito de Compras",
            bg = "#F0BE49",
            highlightthickness=0,
            command = newVentana,
            relief="flat"
        )
        self.buttonIrCarrito.place(x=237.0, y=384.0, width=152.0, height=36.0)
        
        # Botones para agregar los productos
        botones_agregar = [(197, 156), (459, 156), (197, 298), (459, 298)]
        for i in range(4):
            Button(
                self.venPrincipal,
                borderwidth=0,
                text="Agregar",
                bg="#327039",
                highlightthickness=0,
                command=lambda i=i: print(f"Producto {i+1} agregado"),
                relief="flat"
            ).place(x=botones_agregar[i][0], y=botones_agregar[i][1], width=79, height=18)

        def cerrar():
            print("Cerrando ventana...")
            exit(0)

        self.venPrincipal.protocol("WM_DELETE_WINDOW", cerrar)
        self.venPrincipal.resizable(False, False)
        self.venPrincipal.mainloop()

if __name__ == "__main__":
    app = ventanaPrincipal()
