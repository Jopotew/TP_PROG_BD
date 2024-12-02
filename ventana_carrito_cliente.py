from tkinter import Toplevel, Canvas, Button, Listbox, Scrollbar, END, Tk
import controlador_funciones_ventanas as funciones

class ventanaCarrito:
    def __init__(self, clienteComprando) -> None:
        self.venCart = Toplevel()
        width = 600
        height = 450
        screenWidth = self.venCart.winfo_screenwidth()
        screen_Height = self.venCart.winfo_screenheight()
        x = (screenWidth - width) // 2
        y = (screen_Height - height) // 2
        self.venCart.geometry(f"{width}x{height}+{x}+{y}")
        self.venCart.configure(bg = "#F8EDD9")
        self.venCart.title("La Amistad")

        self.cliente = clienteComprando
        
        self.canvas = Canvas(
            self.venCart,
            bg = "#F8EDD9",
            height = 450,
            width = 600,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)

        self.coordenadaListBox = (87.0, 108.0, 348.0, 380.0,)
        self.ListBoxCarrito = Listbox(self.venCart, bg="#D9D9D9", width=40, height=10)
        self.ListBoxCarrito.place(x=self.coordenadaListBox[0], y=self.coordenadaListBox[1], width=self.coordenadaListBox[2]-self.coordenadaListBox[0], height=self.coordenadaListBox[3]-self.coordenadaListBox[1])

        self.scrollbarHorizontal1 = Scrollbar(self.venCart, orient="horizontal", command=self.ListBoxCarrito.xview)
        self.scrollbarHorizontal1.place(x=self.coordenadaListBox[0], y=self.coordenadaListBox[3], width=self.coordenadaListBox[2] - self.coordenadaListBox[0])
        self.ListBoxCarrito.config(xscrollcommand=self.scrollbarHorizontal1.set)

        funciones.cargarProductosCarrito(self.ListBoxCarrito, self.cliente.username)
        self.ListBoxCarrito.bind("<<ListboxSelect>>", lambda event : funciones.mostrarProductosPantallaCarito(event, self.ListBoxCarrito, self.canvas, self.cliente.username))

        self.canvas.create_rectangle(
            0.0,
            0.0,
            600.0,
            74.0,
            fill="#133020",
            outline="")

        self.canvas.create_text(
            75.0,
            18.0,
            anchor="nw",
            text="Carrito de Compras ",
            fill="#F8EDD9",
            font=("Agbalumo Regular", 40 * -1)
        )

        self.canvas.create_rectangle(
            408.0,
            156.0,
            513.0,
            261.0,
            fill="#D9D9D9",
            outline="",
            tags="info"
            )

        self.canvas.create_text(
            410.0,
            268.0,
            anchor="nw",
            text="Producto:",
            fill="#000000",
            font=("Inter", 12 * -1),
            tags="info"
        )

        self.canvas.create_text(
            410.0,
            288.0,
            anchor="nw",
            text="Cantidad: 0",
            fill="#000000",
            font=("Inter", 12 * -1),
            tags="info"
        )

        self.canvas.create_text(
            410.0,
            310.0,
            anchor="nw",
            text="Subtotal: $0.00",
            fill="#000000",
            font=("Inter", 12 * -1),
            tags="info"
        )

        self.botonAgregarProducto = Button(
            self.venCart,
            borderwidth=0,
            highlightthickness=0,
            command = lambda: funciones.agregarProductoVentanaCarrito(self.ListBoxCarrito, self.cliente.username, self.venCart),
            relief="flat",
            bg="#133020",
            fg="white",
            text="Agregar Producto"
        )
        self.botonAgregarProducto.place(
            x=405.0,
            y=330.0,
            width=110.0,
            height=20.0
        )

        self.botonEliminarPoroducto = Button(
            self.venCart,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: funciones.eliminarProductoCarrito(self.ListBoxCarrito, self.cliente.username, self.venCart),
            relief="flat",
            bg="#B62D05",
            text="Eliminar Producto"
        )
        self.botonEliminarPoroducto.place(
            x=405.0,
            y=355.0,
            width=110.0,
            height=20.0
        )

        self.botonFila = Button(
            self.venCart,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: funciones.ventanaFilaCliente(self.venCart, self.cliente),
            relief="flat",
            text="Finalizar Compra",
            bg="#F0BE49",
        )
        self.botonFila.place(
            x=481.0,
            y=414.0,
            width=97.0,
            height=23.0
        )

        self.botonVolver = Button(
            self.venCart,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: funciones.volverPantallaMercado(self.venCart, self.cliente),
            relief="flat",
            text="Volver",
            bg="#133020",
            fg="white"
        )
        self.botonVolver.place(
            x=10.0,
            y=413.0,
            width=58.0,
            height=23.0
        )
        
        self.venCart.protocol("WM_DELETE_WINDOW", funciones.cerrar)
        self.venCart.resizable(False, False)
        self.venCart.mainloop()
    
if __name__ == "__main__":
    app = ventanaCarrito()

