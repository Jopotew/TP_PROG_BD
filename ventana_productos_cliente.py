from tkinter import Toplevel, Canvas, Button, Listbox, END, ttk, Scrollbar
import controlador_funciones_ventanas as funciones

class ventanaProductosMercado:
    def __init__(self, clienteComprando):
        self.venProductosMercado = Toplevel()
        width = 600
        height = 450
        screenWidth = self.venProductosMercado.winfo_screenwidth()
        screen_Height = self.venProductosMercado.winfo_screenheight()
        x = (screenWidth - width) // 2
        y = (screen_Height - height) // 2
        self.venProductosMercado.geometry(f"{width}x{height}+{x}+{y}")
        self.venProductosMercado.configure(bg = "#F8EDD9")
        self.venProductosMercado.title("La Amistad")

        self.funcion = funciones
        self.cliente = clienteComprando
        
        self.canvas = Canvas(
            self.venProductosMercado,
            bg = "#F8EDD9",
            height = 450,
            width = 600,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.coordenadaListBox = (29.0, 128.0, 345.0, 400.0)
        self.ListBoxProductos = Listbox(self.venProductosMercado, bg="#D9D9D9", width=40, height=10)
        self.ListBoxProductos.place(x=self.coordenadaListBox[0], y=self.coordenadaListBox[1], width=self.coordenadaListBox[2]-self.coordenadaListBox[0], height=self.coordenadaListBox[3]-self.coordenadaListBox[1])

        self.scrollbarHorizontal1 = Scrollbar(self.venProductosMercado, orient="horizontal", command=self.ListBoxProductos.xview)
        self.scrollbarHorizontal1.place(x=self.coordenadaListBox[0], y=self.coordenadaListBox[3], width=self.coordenadaListBox[2] - self.coordenadaListBox[0])
        self.ListBoxProductos.config(xscrollcommand=self.scrollbarHorizontal1.set)

        self.menuCategoria = ttk.Combobox(self.venProductosMercado, values=["TODOS","Fruta", "Electrodomesticos", "Bebidas", "Lacteos", "Carnes"])
        self.menuCategoria.place(x=252.0, y=91.0, width=145.0, height=25.0)
        self.menuCategoria.set("Selecciona la categoria")
           
        self.menuCategoria.bind("<<ComboboxSelected>>", lambda event: self.funcion.mostrarProductoPorCategoria(self.ListBoxProductos,event, self.menuCategoria))
        self.funcion.cargarProductos(self.ListBoxProductos)
        self.ListBoxProductos.bind("<<ListboxSelect>>", lambda event: self.funcion.mostrarProductos(self.ListBoxProductos,event, self.canvas))
        
        #Creacion de los bloques de design de la ventana 
        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            0.0,
            0.0,
            600.0,
            74.0,
            fill="#133020",
            outline=""
        )

        self.canvas.create_text(
            156.0,
            18.0,
            anchor="nw",
            text="Productos ",
            fill="#F8EDD9",
            font=("Agbalumo Regular", 40 * -1),
            justify="center"
        )

        self.canvas.create_text(
                418.0,
                291.0,
                anchor="nw",
                text="Producto:",
                fill="#000000",
                font=("Inter", 12 * -1),
                tags="info"
        )
        
        self.canvas.create_text(
                418.0,
                311.0,
                anchor="nw",
                text="Precio: $0.00",
                fill="#000000",
                font=("Inter", 12 * -1),
                tags="info"
        )

        self.canvas.create_rectangle(
            416.0,
            179.0,
            521.0,
            284.0,
            fill="#D9D9D9",
            outline=""
        )

        self.botonAgregarProduto = Button(    
            self.venProductosMercado,
            borderwidth=0,
            highlightthickness=0,
            command = lambda: self.funcion.agregarProductoCarrito(self.ListBoxProductos, self.cliente.username, self.venProductosMercado),
            relief="flat",
            text="Agregar Producto",
            bg="#133020",
            fg="white"
        )
        self.botonAgregarProduto.place(
            x=419.0,
            y=335.0,
            width=105.0,
            height=25.0
        )

        self.botonCarritoCompra = Button(
            self.venProductosMercado,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.funcion.cambioCarrito(self.venProductosMercado, self.cliente.username, self.cliente),
            relief="flat",
            text="Carrito Compras",
            bg="#F0BE49",
        )
        self.botonCarritoCompra.place(
            x=481.0,
            y=412.0,
            width=105.0,
            height=25.0
        )

        self.venProductosMercado.protocol("WM_DELETE_WINDOW", self.funcion.cerrar)
        self.venProductosMercado.resizable(False, False)
        self.venProductosMercado.mainloop()
        
if __name__ == "__main__":
    app = ventanaProductosMercado()
