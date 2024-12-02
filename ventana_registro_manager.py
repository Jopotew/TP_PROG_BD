from pathlib import Path
from tkinter import Toplevel, Canvas, Entry, Button, PhotoImage
import controlador_funciones_ventanas as funcion

class ventanaManagerCreator:
    def __init__(self) -> None:
        def relative_to_assets(path: str) -> Path:
            return self.ASSETS_PATH / Path(path)
        
        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path(r"C:\Users\Spectre\Pictures\FINAL_prog_BD\assets")

        self.venManagerCreation = Toplevel()
        width = 600
        height = 450
        screenWidth = self.venManagerCreation.winfo_screenwidth()
        screen_Height = self.venManagerCreation.winfo_screenheight()
        x = (screenWidth - width) // 2
        y = (screen_Height - height) // 2
        self.venManagerCreation.geometry(f"{width}x{height}+{x}+{y}")
        self.venManagerCreation.configure(bg = "#F8EDD9")


        self.canvas = Canvas(
            self.venManagerCreation,
            bg = "#FFFFFF",
            height = 450,
            width = 600,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            0.0,
            0.0,
            339.0,
            450.0,
            fill="#133020",
            outline="")

        self.canvas.create_text(
            25.0,
            50.0,
            anchor="nw",
            text="Registrar Usuario",
            fill="#F8EDD9",
            font=("Agbalumo Regular", 36 * -1)
        )

        self.canvas.create_text(
            42.0,
            211.0,
            anchor="nw",
            text="Nombre",
            fill="#F8EDD9",
            font=("Inter", 13 * -1)
        )

        self.canvas.create_text(
            8.0,
            110.0,
            anchor="nw",
            text="Bienvenido a Supermercado La Amistad, a conitunuacion \n complete el formulaio para crear un usuario manager. Si \n ya cuenta con uno regrese a la ventana de inicio de sesión.",
            fill="#F8EDD9",
            font=("Inter", 12 * -1),
            justify = "center"
        )

        self.canvas.create_text(
            42.0,
            244.0,
            anchor="nw",
            text="Imagen",
            fill="#F8EDD9",
            font=("Inter", 13 * -1)
        )

        self.canvas.create_text(
            42.0,
            278.0,
            anchor="nw",
            text="Username",
            fill="#F8EDD9",
            font=("Inter", 13 * -1)
        )

        self.canvas.create_text(
            42.0,
            311.0,
            anchor="nw",
            text="Mail",
            fill="#F8EDD9",
            font=("Inter", 13 * -1)
        )

        self.canvas.create_text(
            42.0,
            344.0,
            anchor="nw",
            text="Contraseña",
            fill="#F8EDD9",
            font=("Inter", 13 * -1)
        )

        self.canvas.create_rectangle(
            27.0,
            181.0,
            309.0228271484375,
            182.0,
            fill="#DD5C36",
            outline="")

        self.nameEntry = Entry(
            self.venManagerCreation,
            bd=0,
            bg="#D9D9D9",
            highlightthickness=0
        )
        self.nameEntry.place(
            x=144.0,
            y=211.0,
            width=153.0,
            height=19.0
        )

        self.imageEntry = Entry(
            self.venManagerCreation,
            bd=0,
            bg="#D9D9D9",
            highlightthickness=0
        )
        self.imageEntry.place(
            x=144.0,
            y=243.0,
            width=153.0,
            height=19.0
        )

        self.usernameEntry = Entry(
            self.venManagerCreation,
            bd=0,
            bg="#D9D9D9",
            highlightthickness=0
        )
        self.usernameEntry.place(
            x=144.0,
            y=276.0,
            width=153.0,
            height=18.0
        )

        self.mailEntry = Entry(
            self.venManagerCreation,
            bd=0,
            bg="#D9D9D9",
            highlightthickness=0
        )
        self.mailEntry.place(
            x=144.0,
            y=308.0,
            width=153.0,
            height=19.0
        )

        self.passwordEntry = Entry(
            self.venManagerCreation,
            bd=0,
            bg="#D9D9D9",
            highlightthickness=0
        )
        self.passwordEntry.place(
            x=144.0,
            y=340.0,
            width=153.0,
            height=19.0
        )
        self.botonRegistrar = Button(
            self.venManagerCreation,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: funcion.createNewManager(self.nameEntry, self.usernameEntry, self.mailEntry,self.passwordEntry, self.imageEntry, self.venManagerCreation),
            relief="flat",
            text="Crear Usuario",
            bg="#E2714F"
        )
        self.botonRegistrar.place(
            x=78.0,
            y=381.0,
            width=85.0,
            height=25.0
        )

        self.iniciarSesionboton = Button(
            self.venManagerCreation,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: funcion.PantallaInicioSesionManager(self.venManagerCreation),
            relief="flat",
            text="Volver",
            bg="#F0BE49"
        )
        self.iniciarSesionboton.place(
            x=175.0,
            y=381.0,
            width=85.0,
            height=25.0
        )
        
        self.image_image_1 = PhotoImage(
            file=relative_to_assets("imagen_4.png"))
        self.image_1 = self.canvas.create_image(
            469.0,
            225.0,
            image=self.image_image_1
        )
        self.canvas.image = self.image_image_1

        self.venManagerCreation.protocol("WM_DELETE_WINDOW", self.cerrarPrograma)
        self.venManagerCreation.resizable(False, False)
        self.venManagerCreation.mainloop()
        self.venManagerCreation.pack(fill="both", expand=True)
    
    def cerrarPrograma(self):
        funcion.cerrarVentanaX(self.venManagerCreation)
        
if __name__ == "__main__":
    app = ventanaManagerCreator()