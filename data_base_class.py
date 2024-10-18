import urllib.request
from PIL import Image, ImageTk
from io import BytesIO
from supabase import create_client, Client
from tkinter import END, messagebox

class DataBase():
    def __init__(self):
        self.key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJkZmx1a3lvc3NiZXVwaHlldWZwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjgzMDA1NTgsImV4cCI6MjA0Mzg3NjU1OH0.lkUwkPifUMKOcJSu-ODIaZQZmtK4HTsq9ruWWSLnF6g"  
        self.url = "https://rdflukyossbeuphyeufp.supabase.co"
        self.database: Client = create_client(self.url, self.key)

    def search_by_row(self, table, row):  # BUSCA POR FILA
        row_to_search = self.database.table(table).select(row).execute()
        return row_to_search.data
    
    def search_by_row_and_key(self, table, row, column, key_to_search):  # BUSCA POR FILA
        row_to_search = self.database.table(table).select(row).eq(column, key_to_search).execute()
        return row_to_search.data
    
    def search_by_product(self, table, product):  # BUSCA UN PRODUCTO
        product_to_search = self.database.table(table).select("ID, producto, stock").eq("producto", product).execute()
        return product_to_search.data
    
    def search_username(self, table, username):  #Busca contrasenias
        product_to_search = self.database.table(table).select("ID, USERNAME, PASSWORD").eq("USERNAME", username).execute()
        return product_to_search.data

    def insert_product(self, table, data):  # INSERTA UN PRODUCTO
        response = self.database.table(table).insert(data).execute()
        return response.data

    def update_product(self, table, product_id, data):  
        """ 
        MODIFICA UN PRODUCTO. DEBE RECIBIR UN DICT. EJEMPLO : DATA_A_CAMBIAR = {"STOCK" : 3}
        PUEDE TAMBIEN RECIBIR OTRA COSA. EJ: DATA_A_CAMBIAR = {"NOMBRE_PRODUCTO" : "MANZANA"}
        LA PRIMERA PARTE DEL DICT REFIERE A LA SECCION DE LA TABLA QUE QUERES MODIFICAR
        """
        response = self.database.table(table).update(data).eq('ID', product_id).execute()
        return response.data

    def delete_product(self, table, product_id):  # ELIMINA UN PRODUCTO
        response = self.database.table(table).delete().eq('ID', product_id).execute()
        return response.data
                    
                        
    def check_and_create_order(self, username):
        
        client_info = self.search_username("CLIENT", username)
        if not client_info:
            print(f"Cliente con username '{username}' no encontrado.")
            return None
        
        client_id = client_info[0]['ID']
        client_order = self.search_by_row_and_key("ORDER", "*", "ID_CLIENT", client_id)
        
        if client_order:
            for status in client_order:
                if status["ID_STATUS"] == 1: 
                    print("EXISTE ORDEN PAGA")
                    for unpaid_status in client_order:
                        print("BUSCANDO ORDEN IMPAGA")
                        if unpaid_status["ID_STATUS"] == 2:
                            print("hay una orden paga, pero tiene una impaga. Utilizando la impaga")
                            unpaid_order = self.return_unpaid_order(client_id, username)
                            return unpaid_order
                    print("NO EXISTE ORDEN IMPAGA")
                    new_order = self.create_new_order(client_id, username)   
                    return new_order   
                            
                else:   
                    print("ORden impaga")
                    unpaid_order = self.return_unpaid_order(client_id, username)
                    return unpaid_order

        else:       
            print("NO HAY ORDEN")
            new_order = self.create_new_order(client_id, username)   
            return new_order   
    
    def return_unpaid_order(self, client_id, username):
        existing_order = self.database.table("ORDER").select("*").eq("ID_CLIENT", client_id).eq("ID_STATUS", 2).execute()
        if existing_order.data:
            print(f"Orden existente encontrada para el cliente '{username}'.")
            print("RETURNS UNPAID ORDER")
            return existing_order.data[0] 
        
    def create_new_order(self, client_id, username):
        new_order_data = {
        "ID_CLIENT": client_id,
        "ID_STATUS": 2,
        "TOTAL_ORDER": 0,
            }
        new_order = self.insert_product("ORDER", new_order_data)
        print(f"Se ha creado una nueva orden para el cliente '{username}'.")
        print("CREATES NEW ORDER")
        return new_order

#Queda hacer que se ligue a una orderLine
    def new_order_line(self, order, product, ):
        
        order_id = order["ID"]
        product_table= self.search_by_row_and_key("PRODUCT","*","NAME",product)
        product_id = product_table[0]["ID"]
        
        order_line_table = self.search_by_row_and_key("ORDER_LINE","*","ID_PRODUCT", product_id)
        

        for order in order_line_table:
            quantity = order["QUANTITY"]
            order_product = order["ID_PRODUCT"]
            order_line_id = order["ID"]
            order_id_check =  order["ID_ORDER"]
            if product_id == order_product and order_id == order_id_check:
                print("ID PRODUCTO Y ID ORDER ENCONTRADOS DENTRO DEL ORDERLINE")
                print("SUMANDO 1 A LA CANTIDAD")
                data = {"QUANTITY" : quantity + 1}
                new_line= self.update_product("ORDER_LINE",order_line_id, data)
                return new_line
            else : 
                print("ID PRODUCTO NO EXISTE DENTRO DEL ORDERLINE")
                print("CREANDO  NUEVO ORDERLINE CON PRODUCTO")
                new_line= self.create_order_line(product_id, order_id, quantity)
                return new_line
        print("No hay ordenes dentro de la orderline, creando una")
        self.create_order_line(product_id, order_id, 0)


    def create_order_line(self, product_id, order_id, quantity):
        new_order_line_data : dict = {
            "ID_PRODUCT": product_id,
            "ID_ORDER" : order_id,
            "QUANTITY": quantity + 1,
            }
        new_line = self.insert_product("ORDER_LINE", new_order_line_data)
        return new_line
    
    
    def cargarProdutosMercado(self,listBox):
        '''
        Se obtienen los datos de la tabla PRODUCTS, y se muestran en una listbox los campos de NAME, PRICE, STOCK.
        '''
        listBox.delete(0, END)
        data = self.database.table('PRODUCT').select('NAME', 'ID_CATEGORY', 'STOCK').execute()
        items = data.data
        if items:
            for item in items:
                idCategoria = item['ID_CATEGORY']
                dataCategoria = self.database.table('CATEGORIES').select('CAT_NAME').eq('ID', idCategoria).execute()
                nombreCategoria = dataCategoria.data[0]['CAT_NAME'] if dataCategoria.data else 'Desconocido'
                listBox.insert(END, f"Nombre: {item['NAME']} | Categoria: {nombreCategoria} | Stock disponible: {item['STOCK']}")


    def mostrarProductoPantalla(self, listBox, event, canvas):
        '''
        Esta funcion obtiene los datos de la base de datos de la tabla PRODUCTS, muestra los campos NAME, PRICE e IMAGE
        en el lado izquierdo de la lista. Aqui se crean los textos y las imagenes en sus posiciones y formatos correspondientes.
        '''
        seleccion = listBox.curselection()
        if seleccion:
            canvas.delete("info")
            
            textoSeleccionado = listBox.get(seleccion[0])
            nombreProducto = textoSeleccionado.split('|')[0].replace("Nombre: ", "").strip()

            dataProducto = self.database.table('PRODUCT').select('NAME', 'PRICE', 'IMAGE').eq('NAME', nombreProducto).execute()
            producto = dataProducto.data[0] if dataProducto.data else None

            if producto:
                nombre = producto['NAME']
                precio = producto['PRICE']
                imagenUrl = producto['IMAGE']

                canvas.create_text(
                    418.0,
                    291.0,
                    anchor="nw",
                    text=f"Producto: {nombre}",
                    fill="#000000",
                    font=("Inter", 12 * -1),
                    tags="info"
                )

                canvas.create_text(
                    418.0,
                    311.0,
                    anchor="nw",
                    text=f"Precio: ${precio}",
                    fill="#000000",
                    font=("Inter", 12 * -1),
                    tags="info"
                )
                try:
                    with urllib.request.urlopen(imagenUrl) as u:
                        raw_data = u.read()
                    imagenProducto = Image.open(BytesIO(raw_data))
                    imagenProducto = imagenProducto.resize((105, 105))
                    self.imagenProductoTk = ImageTk.PhotoImage(imagenProducto)

                    canvas.create_image(
                        468.0, 232.0,
                        anchor="center",
                        image=self.imagenProductoTk, 
                    )
                    canvas.image = self.imagenProductoTk
                except Exception as e:
                    print(f"Error al cargar la imagen: {e}")


    def cargarProductosFiltrados(self, listBox, event, menuCategoria):
        '''
        En base a la seleccion del menu desplegable se seleccionan los productos que tienen esa categoria. Se debe primero obtener el id de categoria que tiene el producto,
        luego ese  id se busca en la tabla categorias y es el que se utiliza para buscar y osmtrar en pantalla.
        '''
        listBox.delete(0, END)
        categoriaSeleccionada = menuCategoria.get()
                    
        dataCategoria = self.database.table('CATEGORIES').select('ID').eq('CAT_NAME', categoriaSeleccionada).execute()
        idCategoria = dataCategoria.data[0]['ID'] if dataCategoria.data else None
            
        if categoriaSeleccionada == "TODOS":
            data = self.database.table('PRODUCT').select('NAME', 'ID_CATEGORY', 'STOCK').execute()
        elif idCategoria is not None:
            data = self.database.table('PRODUCT').select('NAME', 'ID_CATEGORY', 'STOCK').eq('ID_CATEGORY', idCategoria).execute()

        items = data.data
        if items:
            for item in items:
                idCategoria = item['ID_CATEGORY']
                dataCategoria = self.database.table('CATEGORIES').select('CAT_NAME').eq('ID', idCategoria).execute()
                nombreCategoria = dataCategoria.data[0]['CAT_NAME'] if dataCategoria.data else 'Desconocido'
                listBox.insert(END, f"Nombre: {item['NAME']} | Categoria: {nombreCategoria} | Stock disponible: {item['STOCK']}")


    def cargarProdutosCarrito(self, listBox):
        '''
        Se obtienen los datos de la tabla ORDER_LINE, y se muestran en una listbox los campos de PRODUCT_NAME, QUANTITY
        '''
        listBox.delete(0, END)
        data = self.database.table('ORDER_LINE').select('ID_PRODUCT', 'QUANTITY').execute()
        items = data.data
        if items:
            for item in items:
                idProducto = item['ID_PRODUCT']
                dataCategoria = self.database.table('PRODUCT').select('NAME').eq('ID', idProducto).execute()
                nombreProducto = dataCategoria.data[0]['NAME'] if dataCategoria.data else 'Desconocido'
                listBox.insert(END, f"Nombre: {nombreProducto} | Cantidad Adquirida: {item['QUANTITY']}")     
                
                
    def mostrarProductoPantallaCarrito(self, event, listBox, canvas):
        '''
        Esta función obtiene los datos de la ORDER_LINE que vendria a ser una especie de carrito de compras, selecciona
        aquellas linea que tienen el ID_ORDER del usuario que ingreso sesion.
        De ahi se obtiene la informacion del producto, la cantidad y el subtotal de la linea. Ademas de la imagen.
        '''
        seleccion = listBox.curselection()
        if seleccion:
            canvas.delete("info")
            textoSeleccionado = listBox.get(seleccion[0])
            nombreProducto = textoSeleccionado.split('|')[0].replace("Nombre: ", "").strip()
            
            dataProducto = self.database.table('PRODUCT').select('ID', 'NAME', 'IMAGE').eq('NAME', nombreProducto).execute()
            producto = dataProducto.data[0] if dataProducto.data else None
            
            if producto:
                idProducto = producto['ID']
                imagenUrl = producto['IMAGE']
                
                dataOrderLine = self.database.table('ORDER_LINE').select('QUANTITY', 'SUBTOTAL_ORDERLINE').eq('ID_PRODUCT', idProducto).execute()
                orderLine = dataOrderLine.data[0] if dataOrderLine.data else None

                if orderLine:
                    cantidad = orderLine['QUANTITY']
                    subtotal = orderLine['SUBTOTAL_ORDERLINE']
                    
                    canvas.create_text(
                        410.0,
                        268.0,
                        anchor="nw",
                        text=f"Producto: {nombreProducto}",
                        fill="#000000",
                        font=("Inter", 12 * -1),
                        tags="info"
                    )
                    
                    canvas.create_text(
                        410.0,
                        288.0,
                        anchor="nw",
                        text=f"Cantidad: {cantidad}",
                        fill="#000000",
                        font=("Inter", 12 * -1),
                        tags="info"
                    )
                    
                    canvas.create_text(
                        410.0,
                        308.0,
                        anchor="nw",
                        text=f"Subtotal: ${subtotal}",
                        fill="#000000",
                        font=("Inter", 12 * -1),
                        tags="info"
                    )
                    
                    with urllib.request.urlopen(imagenUrl) as u:
                        raw_data = u.read()
                    imagenProducto = Image.open(BytesIO(raw_data))
                    x = 105
                    y = 105
                    imagenProducto = imagenProducto.resize((x, y))
                    imagen = ImageTk.PhotoImage(imagenProducto)
                    canvas.create_image(
                        460.5,208.5,
                        anchor="center",
                        image=imagen,
                        tags="info"
                    )
                    canvas.image = imagen      

    def cargarProductoManager(self, listBox):
        listBox.delete(0, END)
        data = self.database.table('PRODUCT').select('*').execute()
        items = data.data
        if items:
            for item in items:
                listBox.insert(END, f"ID: {item['ID']} | Nombre: {item['NAME']} | Imagen: {item['IMAGE']} | Precio: {item['PRICE']} | Stock: {item.get('STOCK', 0)} | Categoria: {item['ID_CATEGORY']}")
        
    def cargarCategoriaManager(self, listBox):
        listBox.delete(0, END)
        dataCat = self.database.table('CATEGORIES').select('*').execute()
        items = dataCat.data
        if items:
            for item in items:
                listBox.insert(END, f"ID: {item['ID']} | Categoria: {item['CAT_NAME']} ")

    def agregarProductoTabla(self, nombreEntry, imagenEntry, precioEntry, stockEntry, idCategoriaEntry):
        #MANAGER
        name = nombreEntry.get()
        image = imagenEntry.get()
        price = precioEntry.get()
        stock = stockEntry.get()
        category = idCategoriaEntry.get()
        
        if not name or not image or not price or not stock or not category:
            messagebox.showwarning("Advertencia", "Por favor completa todos los campos.")
            return
        nuevoProducto = {
            "NAME": name,
            "IMAGE": image,
            "PRICE": float(price),
            "STOCK": int(stock), 
            "ID_CATEGORY": int(category) 
        }
        self.database.table('PRODUCT').insert(nuevoProducto).execute()
        messagebox.showinfo("Éxito", "Producto agregado correctamente.")
        
        
    global selected_id
    selected_id = None 
    def actualizarValor(self, nuevoValorEntry, menuAtributoModificar):
        global selected_id
        if not selected_id:
            messagebox.showwarning("Advertencia", "Por favor selecciona un producto.")
            return

        nuevoValor = nuevoValorEntry.get()
        atributo = menuAtributoModificar.get()

        if atributo == "NAME":
            self.database.table('PRODUCT').update({"NAME": nuevoValor}).eq("ID", selected_id).execute()
        elif atributo == "IMAGE":
            self.database.table('PRODUCT').update({"IMAGE": nuevoValor}).eq("ID", selected_id).execute()
        elif atributo == "PRICE":
            self.database.table('PRODUCT').update({"PRICE": float(nuevoValor)}).eq("ID", selected_id).execute()
        elif atributo == "STOCK":
            self.database.table('PRODUCT').update({"STOCK": int(nuevoValor)}).eq("ID", selected_id).execute()
        elif atributo == "CATEGORY":
            self.database.table('PRODUCT').update({"ID_CATEGORY": int(nuevoValor)}).eq("ID", selected_id).execute()
        messagebox.showinfo("Éxito", f"{atributo} modificado correctamente.")


    def enSeleccion(self, event, listBox):
        global selected_id
        selected_index = listBox.curselection()
        if selected_index:
            selected_text = listBox.get(selected_index)
            selected_id = int(selected_text.split('|')[0].split(':')[1].strip())
        return selected_id
        


        
        



db = DataBase()
def test():
    order = db.check_and_create_order("juan")
    db.new_order_line(order, "Pera")

test()