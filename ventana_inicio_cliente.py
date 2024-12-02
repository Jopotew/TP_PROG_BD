from pathlib import Path
from tkinter import END, Toplevel, Canvas, Button, PhotoImage, Entry, messagebox, font
import controlador_funciones_ventanas as funcion

class ventanaInicio:
    def __init__(self):
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Spectre\Pictures\FINAL_prog_BD\assets")
        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)
                
        self.venInicio = Toplevel()
        self.venInicio.title("La Amistad")
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
        self.canvas.image = image_image_1


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
            text="La \n Amistad",
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

        self.nombreUsuario = Entry(self.venInicio, bg = "#F8EDD9",relief="flat",text = "Ingrese su Username")
        self.nombreUsuario.pack(pady=10)
        self.nombreUsuario.place(
            width=120,
            height = 20,
            x=425.0,
            y=240.0
        )
        
        self.canvas.create_text(
            425,
            265.0,
            anchor="nw",
            text="Ingrese su Contraseña:",
            fill="#F8EDD9",
            font=("Afacad", 10),  # Tipo de letra y tamaño
            justify="center"
        )

        self.contraseniaUsuario = Entry(self.venInicio, bg = "#F8EDD9",relief="flat",text = "Ingrese su Ccontraseña")
        self.contraseniaUsuario.pack(pady=10)
        self.contraseniaUsuario.place(
            width=120,
            height = 20,
            x=425.0,
            y=283.0
        )
        
        self.botonInicioCompra = Button(
            self.venInicio,
            borderwidth=0,
            highlightthickness=0,
            text = "Iniciar Compra",
            bg = "#F0BE49",
            command = lambda: funcion.iniciarCompra(self.nombreUsuario, self.venInicio, self.contraseniaUsuario),
            relief="flat"
        )
        self.botonInicioCompra.place(
            x=425.0,
            y=315.0,
            width=130.0,
            height=30.0
        )
        
        self.botonRegistro = Button(
            self.venInicio,
            borderwidth=0,
            highlightthickness=0,
            text = "Registrar Usuario",
            bg = "#E2714F",
            command = lambda: funcion.pantallaCreacionUsuario(self.venInicio),
            relief="flat",
            fg="black"
        )
        self.botonRegistro.place(
            x=425.0,
            y=350.0,
            width=130.0,
            height=30.0
        )
        
        self.venInicio.protocol("WM_DELETE_WINDOW", self.cerrarPrograma)
        self.venInicio.resizable(False, False)
        self.venInicio.mainloop()
    
    def cerrarPrograma(self):
        funcion.cerrarVentanaX(self.venInicio)

if __name__ == "__main__":
    app = ventanaInicio()
