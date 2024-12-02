from tkinter import Toplevel, Canvas, Entry,Button, Listbox, END, ttk
from tkinter import PhotoImage
import urllib.request
from io import BytesIO
from PIL import Image, ImageTk
import controlador_funciones_ventanas as funciones

class ventanaManager:
    def __init__(self) -> None:
        self.venManager = Toplevel()
        width = 600
        height = 450
        screenWidth = self.venManager.winfo_screenwidth()
        screen_Height = self.venManager.winfo_screenheight()
        x = (screenWidth - width) // 2
        y = (screen_Height - height) // 2
        self.venManager.geometry(f"{width}x{height}+{x}+{y}")
        self.venManager.configure(bg = "#F8EDD9")
        self.venManager.title("La Amistad")

        self.funcion = funciones

        self.canvas = Canvas(
            self.venManager,
            bg="#F8EDD9",
            height=450,
            width=600,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x = 0, y = 0)

        self.coordenadasListBox1 = (11.0, 85.0, 400.0, 233.0)
        self.coordenadasImagenProducto = (413.0, 85.0, 588.0, 233.0)

        self.ListBoxProducto = Listbox(self.venManager, bg="#D9D9D9", width=40, height=10)
        self.ListBoxProducto.place(x=self.coordenadasListBox1[0], y=self.coordenadasListBox1[1], width=self.coordenadasListBox1[2]-self.coordenadasListBox1[0], height=self.coordenadasListBox1[3]-self.coordenadasListBox1[1])

        self.nombreEntry = Entry(self.venManager, bg="#D9D9D9")
        self.nombreEntry.place(x=147.0, y=264.0, width=123.0, height=19)

        self.nuevoValorEntry = Entry(self.venManager, bg="#D9D9D9")
        self.nuevoValorEntry.place(x=419.0, y=330.0, width=147.0, height=19)

        self.imagenEntry = Entry(self.venManager, bg="#D9D9D9")
        self.imagenEntry.place(x=147.0, y=292.0, width=123.0, height=19)

        self.stockEntry = Entry(self.venManager, bg="#D9D9D9")
        self.stockEntry.place(x=147.0, y=347.0, width=123.0, height=19)
        
        self.menuCategoria = ttk.Combobox(self.venManager, values=["Bebidas", "Carnes", "Lacteos", "Verduras", "Fruta", "Electrodomesticos"])
        self.menuCategoria.place(x=147.0, y=375.0, width=123.0, height=19)
        self.menuCategoria.set("Selecciona una categoria")
        
        self.precioEntry= Entry(self.venManager, bg="#D9D9D9")
        self.precioEntry.place(x=147.0, y=320.0, width=123.0, height=19)
        
        self.menuAtributoModificar = ttk.Combobox(self.venManager, values=["NAME", "IMAGE", "PRICE", "STOCK", "CATEGORY"])
        self.menuAtributoModificar.place(x=330.0, y=289.0, width=150.0, height=19)
        self.menuAtributoModificar.set("Selecciona el atributo")

        self.funcion.cargarProductoManagerManager(self.ListBoxProducto)
        self.ListBoxProducto.bind('<<ListboxSelect>>', lambda event: self.funcion.seleccion(event, self.ListBoxProducto))
        self.ListBoxProducto.bind('<<ListboxSelect>>', lambda event: self.seleccion(event))

        self.canvas.create_rectangle(
            0.0,
            0.0,
            600.0,
            74.0,
            fill="#133020",
            outline=""
        )

        self.canvas.create_text(
            106.0,
            18.0,
            anchor="nw",
            text="Manager Productos ",
            fill="#F8EDD9",
            font=("Agbalumo Regular", 40 * -1)
        )

        self.canvas.create_rectangle(
            297.0,
            246.0,
            300.0,
            422.0,
            fill="#133020",
            outline="") #linea divisora de actividades

        self.canvas.create_text(
            45.0,
            264.0,
            anchor="nw",
            text="Nombre",
            fill="#000000",
            font=("Inter", 13 * -1)
        )
        self.canvas.create_text(
            330.0,
            333.0,
            anchor="nw",
            text="Nuevo Valor",
            fill="#000000",
            font=("Inter", 13 * -1)
        )
        self.canvas.create_text(
            45.0,
            293.0,
            anchor="nw",
            text="Imagen",
            fill="#000000",
            font=("Inter", 13 * -1)
        )
        self.canvas.create_text(
            45.0,
            322.0,
            anchor="nw",
            text="Precio",
            fill="#000000",
            font=("Inter", 13 * -1)
        )
        self.canvas.create_text(
            45.0,
            350.0,
            anchor="nw",
            text="Stock",
            fill="#000000",
            font=("Inter", 13 * -1)
        )
        self.canvas.create_text(
            45.0,
            379.0,
            anchor="nw",
            text="ID Categoria",
            fill="#000000",
            font=("Inter", 13 * -1)
        )

        botonModificarProducto = Button(
                self.venManager,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: self.funcion.actualizarAtributo(self.nuevoValorEntry, self.menuAtributoModificar, self.ListBoxProducto),
                relief="flat",
                text="Modificar Producto",
                justify="center",
                bg="#F0BE49"
            )
        botonModificarProducto.place(
                x=412.0,
                y=369.0,
                width=110,
                height=25.0
            )

        botonAgregarProducto = Button(
            self.venManager,
            borderwidth=0,
            highlightthickness=0,
            command = lambda: self.funcion.agregarNuevoProductoTabla(self.nombreEntry, self.imagenEntry, self.precioEntry, self.stockEntry, self.menuCategoria, self.ListBoxProducto),
            relief="flat",
            text="Agregar Producto",
            bg="#133020",
            fg="white",
            justify="center"
        )
        botonAgregarProducto.place(
            x=96.0,
            y=407.0,
            width=102.090576171875,
            height=25.0
        )

        botonCerrarSesion = Button(
            self.venManager,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.funcion.PantallaInicioSesionManager(self.venManager),
            relief="flat",
            text="Cerrar Sesion",
            justify="center",
            bg="#E2714F"
        )
        botonCerrarSesion.place(
            x=486.0,
            y=415.0,
            width=105,
            height=25.0
        )

        self.venManager.protocol("WM_DELETE_WINDOW", self.funcion.cerrar)
        self.venManager.resizable(False, False)
        self.venManager.mainloop()
        
    def seleccion(self, event):
        selection = self.ListBoxProducto.curselection()
        if not selection:
            return
        selected_product = self.ListBoxProducto.get(selection[0])
        imagen_url = selected_product.split('|')[2].strip()
        if imagen_url.startswith('Imagen:'):
            imagen_url = imagen_url.replace('Imagen:', '').strip()
        self.mostrar_imagen(imagen_url)

    def mostrar_imagen(self, imagenUrl):
        with urllib.request.urlopen(imagenUrl) as u:
            raw_data = u.read()
        imagenProducto = Image.open(BytesIO(raw_data))
        x = 150
        y = 150
        imagenProducto = imagenProducto.resize((x, y))
        imagenPantalla = ImageTk.PhotoImage(imagenProducto)
        self.canvas.delete("imagen")
        self.canvas.create_image(
            500.0,
            160.0,
            anchor="center",
            image=imagenPantalla,
            tags="imagen"
        )
        self.canvas.image = imagenPantalla


            
if __name__ == "__main__":
    app = ventanaManager()