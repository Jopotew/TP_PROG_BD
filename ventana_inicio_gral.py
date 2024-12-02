from pathlib import Path
from tkinter import Tk, Canvas, Button
from PIL import Image, ImageTk
import controlador_funciones_ventanas as funcion

class venInicioMercado:
    def __init__(self) -> None:
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Spectre\Pictures\FINAL_prog_BD\assets")
        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)
        
        self.venInicioMercado = Tk()
        self.venInicioMercado.title("La Amistad")
        width = 600
        height = 450
        screen_width = self.venInicioMercado.winfo_screenwidth()
        screen_height = self.venInicioMercado.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.venInicioMercado.geometry(f"{width}x{height}+{x}+{y}")
        self.venInicioMercado.configure(bg = "#FFFFFF")
        self.venInicioMercado.geometry("600x450")

        self.canvas = Canvas(
            self.venInicioMercado,
            bg = "#FFFFFF",
            height = 450,
            width = 600,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            369.0,
            0.0,
            600.0,
            450.0,
            fill="#133020",
            outline="")

        self.canvas.create_text(
            393.0,
            150.0,
            anchor="nw",
            text="La Amistad",
            fill="#F8EDD9",
            font=("Agbalumo Regular", 40 * -1)
        )

        self.inicioManager = Button(
            borderwidth=0,
            highlightthickness=0,
            command=lambda: funcion.PantallaInicioSesionManager(self.venInicioMercado),
            relief="flat",
            bg="#E2714F",
            text="Inicio Sesion Manager",
            fg="black"
        )
        
        self.inicioManager.place(
            x=415.0,
            y=270.0,
            width=130,
            height=35
        )

        self.inicioCliente = Button(
            borderwidth=0,
            highlightthickness=0,
            command= lambda: funcion.pantallaInicioCliente(self.venInicioMercado),
            relief="flat",
            bg="#F0BE49",
            text="Inicio Sesion Cliente",
            fg="black"
        )
        self.inicioCliente.place(
            x=415.0,
            y=225.0,
            width=130,
            height=35
        )

        self.canvas.create_rectangle(
            0.0,
            0.0,
            369.0,
            450.0,
            fill="#FFFFFF",
            outline="")

        self.imagen3 = relative_to_assets("imagen_3.png")
        self.imagenOrigianl = Image.open(self.imagen3)
        self.imagenModi = self.imagenOrigianl.resize((369, 450))
        self.image_image_1 = ImageTk.PhotoImage(self.imagenModi)
        self.image = self.canvas.create_image(
            184.0,
            225.0,
            image = self.image_image_1
        )
        self.canvas.image = self.image_image_1

        self.venInicioMercado.resizable(False, False)
        self.venInicioMercado.mainloop()
        
if __name__ == "__main__":
    app = venInicioMercado()
