from pathlib import Path
from tkinter import END, Tk, Canvas, Button, PhotoImage, Entry, messagebox
from PIL import Image, ImageTk
import cart_and_client_manager
import item_manager

class VentanaInicio:
    def __init__(self):
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Spectre\Documents\UB\Segundo\Prog3\PARCIAL\build\assets\frame0")
        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)
        
        self.venInicio = Tk()
        self.venInicio.title("Portal Compras")
        width = 600
        height = 450
        screen_width = self.venInicio.winfo_screenwidth()
        screen_height = self.venInicio.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.venInicio.geometry(f"{width}x{height}+{x}+{y}")
        self.venInicio.configure(bg = "#FFFFFF")
        
        self.canvas = Canvas(
            self.venInicio,
            bg = "#FFFFFF",
            height = height,
            width = width,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            410.0,
            236.0,
            560.0,
            282.0,
            fill="#F8EDD9",
            outline=""
            )

        image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(
            184.0,
            225.0,
            image=image_image_1
        )

        self.canvas.create_rectangle(
            369.0,
            0.0,
            600.0,
            450.0,
            fill="#133020",
            outline="")

        self.canvas.create_text(
            393.0,
            97.0,
            anchor="nw",
            text="Portal\nCompras",
            fill="#F8EDD9",
            font=("Agbalumor", 35),  # Tipo de letra y tamaño
            justify="center"
        )
        
        self.canvas.create_text(
            425,
            222.0,
            anchor="nw",
            text="Ingrese su nombre:",
            fill="#F8EDD9",
            font=("Afacad", 10),  # Tipo de letra y tamaño
            justify="center"
        )

        self.nombreUsuario = Entry(self.venInicio, bg = "#F8EDD9",relief="flat",text = "Ingrese su nombre")
        self.nombreUsuario.pack(pady=10)
        self.nombreUsuario.place(
            width=120,
            height = 20,
            x=425.0,
            y=240.0
        )
        
        def validarNombre():
            nombre = self.nombreUsuario.get()
            if not nombre or nombre == "Ingrese su nombre":
                messagebox.showerror("ERROR","Ingrese su nombre nuevamente.")
            else:
                carrito = cart_and_client_manager.initializeCartClient(nombre)
                market = item_manager.initializeItem()  # Obtener el objeto SuperMarket
                items = market.items 
                newVentana(self, items, carrito)

        def newVentana(self, items, carrito):
            self.venInicio.withdraw()
            from ventanaPrincipal import ventanaPrincipal
            ventanaPrincipal(items, carrito)
        
        self.botonInicioCompra = Button(
            borderwidth=0,
            highlightthickness=0,
            text = "Iniciar Compra",
            bg = "#E2714F",
            command = validarNombre,
            relief="flat"
        )
        self.botonInicioCompra.place(
            x=410.0,
            y=270.0,
            width=160.0,
            height=35.0
        )
        
        self.venInicio.resizable(False, False)
        self.venInicio.mainloop()

if __name__ == "__main__":
    app = VentanaInicio()
