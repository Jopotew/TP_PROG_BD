from pathlib import Path
from tkinter import Toplevel, Canvas, Button, PhotoImage, ttk
import controlador_funciones_ventanas as funciones

class ventanaPago():
    def __init__(self, clienteComprando) -> None:
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Spectre\Pictures\FINAL_prog_BD\assets")
        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        self.ventanaPago = Toplevel()
        self.ventanaPago.title("La Amistad")
        width = 600
        height = 450
        screen_width = self.ventanaPago.winfo_screenwidth()
        screen_height = self.ventanaPago.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.ventanaPago.geometry(f"{width}x{height}+{x}+{y}")
        self.ventanaPago.configure(bg = "#FFFFFF")
        self.ventanaPago.geometry("600x450")

        self.cliente = clienteComprando

        self.canvas = Canvas(
            self.ventanaPago,
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
            352.0,
            450.0,
            fill="#133020",
            outline="")

        self.canvas.create_text(
            10.0,
            83.0,
            anchor="nw",
            text="Gracias por Confiar \nen La Amistad",
            fill="#F8EDD9",
            font=("Agbalumo Regular", 36 * -1),
            justify="center"
        )

        image_image_1 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        image_1 = self.canvas.create_image(
            476.0,
            225.0,
            image=image_image_1
        )

        self.canvas.create_text(
            54.0,
            302.0,
            anchor="nw",
            text="Metodo de Pago",
            fill="#F8EDD9",
            font=("Inter", 13 * -1)
        )

        self.canvas.create_text(
            35.0,
            165.0,
            anchor="nw",
            text="\nA continuacion selecciona el metodo de pago que \nvayas a utilizar y la forma de entrega para \nfinalizar con tu compra",
            fill="#F8EDD9",
            font=("Inter", 12 * -1),
            justify="center"
        )

        totalCompra = funciones.totalCompra(self.cliente.username)
            
        self.canvas.create_text(
            54.0,
            271.0,
            anchor="nw",
            text = f"El total de su compra es de ${totalCompra} ",
            fill="#F8EDD9",
            font=("Inter", 12 * -1)
        )

        self.canvas.create_text(
            56.0,
            333.0,
            anchor="nw",
            text="Tipo de entrega",
            fill="#F8EDD9",
            font=("Inter", 13 * -1)
        )

        #linea divisoria
        self.canvas.create_rectangle(
            27.0,
            248.0,
            309.0228271484375,
            249.0,
            fill="#DD5C36",
            outline="")

        self.pagoCategoria = ttk.Combobox(self.ventanaPago, values=["Efectivo","MercadoPago", "Transferencia","Tarjeta"])
        self.pagoCategoria.place(x=170.0, y=302.0, width=130.0, height=20.0)
        self.pagoCategoria.set("Metodo de pago")

        self.envioCategoria = ttk.Combobox(self.ventanaPago, values=["Entrega Domicilio","Retiro Sucursal"])
        self.envioCategoria.place(x=170.0, y=333.0, width=130.0, height=20.0)
        self.envioCategoria.set("Forma de envio")

        self.botonPagar = Button(
            self.ventanaPago,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: funciones.finalizarCompra(self.envioCategoria, self.pagoCategoria, self.cliente.username, self.ventanaPago),
            relief="flat",
            bg="#E2714F",
            text="Pagar Compra"
        )
        self.botonPagar.place(
            x=115.0,
            y=372.0,
            width=109.0,
            height=25.0
        )
        
        self.ventanaPago.protocol("WM_DELETE_WINDOW", self.cerrarPrograma)
        self.ventanaPago.resizable(False, False)
        self.ventanaPago.mainloop()
        
    def cerrarPrograma(self):
        funciones.cerrarVentanaX(self.ventanaPago)
        
if __name__ == "__main__":
    app = ventanaPago()

