import requests
from io import BytesIO
from PIL import Image, ImageTk
from pathlib import Path
from tkinter import Toplevel, Canvas, Button, messagebox
import controlador_funciones_ventanas as funciones
import controlador_queue

class ventanaFila:
    def __init__(self, clienteComprando, fila) -> None:
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Spectre\Pictures\FINAL_prog_BD\assets")
        
        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        self.venFila = Toplevel()
        self.venFila.title("La Amistad")
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
        self.canvas.create_rectangle(0.0, 0.0, 600.0, 74.0, fill="#133020", outline="")

        image_path = relative_to_assets("cajaregistradora.jpg") 
        imagen1 = Image.open(image_path) 
        imagen1 = imagen1.resize((105, 171))
        self.imagen1_tk = ImageTk.PhotoImage(imagen1)
        self.canvas.create_image(355.0, 315.0, image=self.imagen1_tk, anchor="center")

        self.canvas.create_text(
            143.0, 18.0, anchor="nw", text="Fila para abonar",
            fill="#F8EDD9", font=("Agbalumo Regular", 40 * -1)
        )

        buttonVolver = Button(
            self.venFila, 
            borderwidth=0, 
            highlightthickness=0, 
            fg="#FFFFFF",
            command=lambda: funciones.pantallaCarritoAppear(self.venFila, clienteComprando),
            relief="flat", 
            text="Volver", 
            bg="#133020"
        )
        buttonVolver.place(x=13.0, y=402.0, width=60.0, height=25.0)

        buttonIniciarPayment = Button(
            self.venFila, 
            borderwidth=0, 
            highlightthickness=0, 
            fg="#FFFFFF",
            command=lambda: funciones.iniciarPago(fila, self.venFila, self.canvas, clienteComprando),
            relief="flat", 
            text="Iniciar Pago", 
            bg="#F0BE49"
        )
        buttonIniciarPayment.place(x=315, y=402.0, width=100, height=30.0)

        self.images = funciones.dibujarImagenes(self.canvas, fila)


        self.venFila.protocol("WM_DELETE_WINDOW", self.cerrarPrograma)
        self.venFila.resizable(False, False)
        self.venFila.mainloop()

    def cerrarPrograma(self):
        funciones.cerrarVentanaX(self.venFila)

if __name__ == "__main__":
    app = ventanaFila()