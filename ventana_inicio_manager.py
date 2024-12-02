from pathlib import Path
from tkinter import END, Toplevel, Canvas, Button, PhotoImage, Entry
import controlador_funciones_ventanas as funcion

class ventanaInicioManager:
    def __init__(self):
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Spectre\Pictures\FINAL_prog_BD\assets")
        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)
                
        self.venInicioManager = Toplevel()
        self.venInicioManager.title("La Amistad")
        width = 600
        height = 450
        screen_width = self.venInicioManager.winfo_screenwidth()
        screen_height = self.venInicioManager.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.venInicioManager.geometry(f"{width}x{height}+{x}+{y}")
        self.venInicioManager.configure(bg = "#FFFFFF")
        
        self.canvas = Canvas(
            self.venInicioManager,
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

        self.nombreUsuarioManager = Entry(self.venInicioManager, bg = "#F8EDD9",relief="flat",text = "Ingrese su Username")
        self.nombreUsuarioManager.pack(pady=10)
        self.nombreUsuarioManager.place(
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

        self.contraseniaUsuarioManager = Entry(self.venInicioManager, bg = "#F8EDD9",relief="flat",text = "Ingrese su Ccontraseña")
        self.contraseniaUsuarioManager.pack(pady=10)
        self.contraseniaUsuarioManager.place(
            width=120,
            height = 20,
            x=425.0,
            y=283.0
        )
        
        self.canvas.create_text(
            425,
            306.0,
            anchor="nw",
            text="Ingrese su acess key:",
            fill="#F8EDD9",
            font=("Afacad", 10),  # Tipo de letra y tamaño
            justify="center"
        )

        self.accesKeyUsuarioManager = Entry(self.venInicioManager, bg = "#F8EDD9",relief="flat",text = "Ingrese su access key:")
        self.accesKeyUsuarioManager.pack(pady=10)
        self.accesKeyUsuarioManager.place(
            width=120,
            height = 20,
            x=425.0,
            y=325.0
        )
        
        self.botonInicioCompra = Button(
            self.venInicioManager,
            borderwidth=0,
            highlightthickness=0,
            text = "Iniciar Sesion",
            bg = "#F0BE49",
            command = lambda: funcion.iniciarSesionManager(self.nombreUsuarioManager, self.contraseniaUsuarioManager, self.accesKeyUsuarioManager, self.venInicioManager) ,
            relief="flat"
        )
        self.botonInicioCompra.place(
            x=425.0,
            y=355.0,
            width=130.0,
            height=30.0
        )
        
        self.botonRegistro = Button(
            self.venInicioManager,
            borderwidth=0,
            highlightthickness=0,
            text = "Registrar Usuario",
            bg = "#E2714F",
            command = lambda: funcion.pantallaCreacionUsuarioManager(self.venInicioManager) ,
            relief="flat",
            fg="black"
        )
        self.botonRegistro.place(
            x=425.0,
            y=390.0,
            width=130.0,
            height=30.0
        )
        
        self.venInicioManager.protocol("WM_DELETE_WINDOW", self.cerrarPrograma)
        self.venInicioManager.resizable(False, False)
        self.venInicioManager.mainloop()
    
    def cerrarPrograma(self):
        funcion.cerrarVentanaX(self.venInicioManager)

if __name__ == "__main__":
    app = ventanaInicioManager()
