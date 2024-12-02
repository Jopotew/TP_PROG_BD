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
        
    def searchByRow(self, table, row):
        '''
        Funcion que busca por fila y retorna los atributos en forma de diccionario
        '''
        rowToSearch = self.database.table(table).select(row).execute()
        return rowToSearch.data
    
    def searchByRowAndKey(self, table, row, column, keyToSearch):
        '''
        Funcion que busca por fila y por un valor en especifico y retorna un diccionario
        '''
        rowToSearch = self.database.table(table).select(row).eq(column, keyToSearch).execute()
        return rowToSearch.data
    
    def searchByProduct(self, table, product):
        '''
        Funcion que busca un producto en especifico en la tabla "PRODUCT" y retorna la informacion del 
        mismo en un diccionario 
        '''
        productToSearch = self.database.table(table).select("ID, producto, stock").eq("producto", product).execute()
        return productToSearch.data
    
    def searchUsername(self, table, username):
        '''
        Funcion que busca todos los datos relacionados con un "username" en la tabla CLIENT y retorna un 
        diccionario con los datos de ese cliente
        '''
        productToSearch = self.database.table(table).select('*').eq("USERNAME", username).execute()
        return productToSearch.data
    
    def insertProduct(self, table, data):
        '''
        Funcion que recibe un diccionario y atraves de el agrega a la tabla correpondiente esos valores en
        las columnas
        '''
        response = self.database.table(table).insert(data).execute()
        return response.data

    def updateProduct(self, table, productId, data):  
        """ 
        Funcion que tiene la misma logica que insertProduct pero esta permite actualizar un atributo de
        alguna de las columnas de una tabla especifica en donde el "ID" sea igual al que se desea actuaizar
        cierto valor
        """
        response = self.database.table(table).update(data).eq('ID', productId).execute()
        return response.data

    def deleteTable(self, table, idToRemove):
        '''
        Funcion que remueve una fila de la tabla en donde el "ID" sea igual que el IdToRemove
        '''
        response = self.database.table(table).delete().eq('ID', idToRemove).execute()
        return response.data
                        
    def checkAndCreateOrder(self, username):
        '''
        Funcion que chequea a traves del username del usuario si tiene creada una order, de no ser asi
        le crea una nueva. Si el usuario tiene una order creada, verifica el estado de la misma. Si se
        encuentra abonada (ID_STATUS = 1) se crea una nueva, si se encuentra impaga (ID_STATUS = 2) 
        se le otorga la misma.
        '''
        clientInfo = self.searchUsername("CLIENT", username)
        if not clientInfo:
            print(f"Cliente con username '{username}' no encontrado.")
            messagebox.showerror("ERROR", "Usuario no encontrado, intente nuevamente o registre un usuario")
            return None
        clientId = clientInfo[0]['ID']
        clientOrder = self.searchByRowAndKey("ORDER", "*", "ID_CLIENT", clientId)
        if clientOrder:
            for status in clientOrder:
                if status["ID_STATUS"] == 1: 
                    for unpaidStatus in clientOrder:
                        if unpaidStatus["ID_STATUS"] == 2:
                            unpaidOrder = self.returnUnpaidOrder(clientId, username)
                            return unpaidOrder
                    newOrder = self.createNewOrder(clientId, username)   
                    return newOrder   
                else:   
                    unpaidOrder = self.returnUnpaidOrder(clientId, username)
                    return unpaidOrder
        else:       
            newOrder = self.createNewOrder(clientId, username)   
            return newOrder   
    
    def returnUnpaidOrder(self, clientId, username):
        '''
        Funcion que retorna esa order que no fue abonada por el cliente
        '''
        existingOrder = self.database.table("ORDER").select("*").eq("ID_CLIENT", clientId).eq("ID_STATUS", 2).execute()
        if existingOrder.data:
            print(f"Orden existente encontrada para el cliente '{username}'.")
            print("RETURNS UNPAID ORDER")
            return existingOrder.data[0]
        
    def createNewOrder(self, clientId, username):
        '''
        Funcion que crea una nueva order al cliente en base a su ID y USERNAME. Se le otorga un valor de 
        STATUS = 2, que refiere que la order esta impaga
        '''
        newOrderData = {
            "ID_CLIENT": clientId,
            "ID_STATUS": 2,
            "TOTAL_ORDER": 0,
        }
        newOrder = self.insertProduct("ORDER", newOrderData)
        print(f"Se ha creado una nueva orden para el cliente '{username}'.")
        print("CREATES NEW ORDER")
        return newOrder

    def newOrderLine(self, listBox, usernameClient):
        '''
        Funcion que a traves de la seleccion del listbox, obtiene la infroamcion del producto seleccionado
        y por medio del USERNAME del cliente se le crea una order_Line al cliente que "esta comprando". Si
        el producto que se desea agregar existe, se modifica la cantidad. Si el producto en cambio no
        existe, se crea una nueva order_Line.
        Esa order_line se le asigna a la ORDER del cliente
        '''
        selectedText = listBox.get(listBox.curselection()[0])
        productName = selectedText.split('|')[0].replace("Nombre:", "").strip()
        userInfo = self.searchUsername('CLIENT', usernameClient)
        if not userInfo:
            print(f"Usuario '{usernameClient}' no encontrado.")
            return None
        clientId = userInfo[0]['ID']
        orderInfo = self.database.table('ORDER').select('ID').eq('ID_CLIENT', clientId).eq('ID_STATUS', 2).execute()
        orderId = orderInfo.data[0]['ID']
        productTable = self.searchByRowAndKey('PRODUCT', 'ID', 'NAME', productName)
        productId = productTable[0]['ID']
        orderLineEntry = self.database.table('ORDER_LINE').select('*').eq('ID_ORDER', orderId).eq('ID_PRODUCT', productId).execute()
        if orderLineEntry.data:
            currentQuantity = orderLineEntry.data[0]['QUANTITY']
            orderLineId = orderLineEntry.data[0]['ID']
            data = {'QUANTITY': currentQuantity + 1}
            updatedLine = self.updateProduct('ORDER_LINE', orderLineId, data)
            return updatedLine
        else:
            return self.createOrderLine(productId, orderId, 1)

    def createOrderLine(self, productId, orderId, quantity):
        '''
        Funcion que obtiene el ID del producto, el de la order y la cantidad y crea una order_line al
        cliente con su ORDER ID.
        '''
        newOrderLineData = {
            'ID_PRODUCT': productId,
            'ID_ORDER': orderId,
            'QUANTITY': quantity,
        }
        newLine = self.insertProduct('ORDER_LINE', newOrderLineData)
        return newLine

    '''
    def removeOrderLine(self, listBox, usernameClient):
    '''
    '''
        Cuando se desea remover un producto se elimina una order_line, entonces se verifica la cantidad 
        de esa order, si es mayor a 1 no se eliminar la fila y se resta 1 a la columna QUANTITY. Si la
        cantidad del producto es igual a 1, se elimina la order_line 
    '''
    '''
        selectedText = listBox.get(listBox.curselection()[0])
        productName = selectedText.split('|')[0].replace("Nombre:", "").strip()
        userInfo = self.searchUsername('CLIENT', usernameClient)
        clientId = userInfo[0]['ID']
        orderInfo = self.searchByRowAndKey('ORDER', 'ID', 'ID_CLIENT', clientId)
        orderId = orderInfo[0]['ID']
        productTable = self.searchByRowAndKey('PRODUCT', 'ID', 'NAME', productName)
        productId = productTable[0]['ID']
        orderLineTable = self.searchByRowAndKey('ORDER_LINE', '*', 'ID_PRODUCT', productId)
        for order in orderLineTable:
            quantity = order['QUANTITY']
            orderProduct = order['ID_PRODUCT']
            orderLineId = order['ID']
            orderIdCheck = order['ID_ORDER']
            if productId == orderProduct and orderId == orderIdCheck:
                if quantity > 1:
                    data = {'QUANTITY': quantity - 1}
                    newLine = self.updateProduct('ORDER_LINE', orderLineId, data)
                    self.cargarProdutosCarrito(listBox, usernameClient)
                    return newLine
                elif quantity <= 1:
                    response = self.deleteTable('ORDER_LINE', orderLineId)
                    self.cargarProdutosCarrito(listBox, usernameClient)
                    return response
    '''
    def removeOrderLine(self, listBox, usernameClient):
        """
        Función para remover un producto de la ORDER_LINE del cliente. 
        Si la cantidad del producto en la línea de orden es mayor a 1, se decrementa en 1. 
        Si es igual a 1, se elimina la línea de orden.
        """
        selectedText = listBox.get(listBox.curselection()[0])
        productName = selectedText.split('|')[0].replace("Nombre:", "").strip()
        userInfo = self.searchUsername('CLIENT', usernameClient)
        clientId = userInfo[0]['ID']
        orderInfo = self.database.table('ORDER').select('ID').eq('ID_CLIENT', clientId).eq('ID_STATUS', 2).execute()
        orderId = orderInfo.data[0]['ID']
        productTable = self.searchByRowAndKey('PRODUCT', 'ID', 'NAME', productName)
        productId = productTable[0]['ID']
        orderLineEntry = self.database.table('ORDER_LINE').select('*').eq('ID_ORDER', orderId).eq('ID_PRODUCT', productId).execute()
        orderLine = orderLineEntry.data[0]
        quantity = int(orderLine['QUANTITY'])
        orderLineId = orderLine['ID']
        if quantity > 1:
            data = {'QUANTITY': quantity - 1}
            updatedLine = self.updateProduct('ORDER_LINE', orderLineId, data)
            self.cargarProdutosCarrito(listBox, usernameClient)
            return updatedLine
        else:
            deletedLine = self.deleteTable('ORDER_LINE', orderLineId)
            self.cargarProdutosCarrito(listBox, usernameClient)
            return deletedLine

    def cargarProdutosMercado(self,listBox):
        '''
        Se obtienen los datos de la tabla PRODUCTS, y se muestran en una listbox los campos 
        de NAME, PRICE, STOCK.
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
        Funcion que muestra en pantalla la imagen del producto que se selecciona a traves de la listbox, y
        se muestra en una posicion especifica (a la izquierda de la listbox). Ademas de la imagen se debe
        de mostrar el nombre y el precio del prodcuto seleccionado.
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

    def cargarProductosFiltrados(self, listBox, event, menuCategoria):
        '''
        En base a la seleccion del menu desplegable se seleccionan los productos que tienen esa categoria. Se debe primero obtener el id de categoria que tiene el producto,
        luego ese  id se busca en la tabla categorias y es el que se utiliza para buscar y mostrar 
        en pantalla.
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

    def cargarProdutosCarrito(self, listBox,usernameClient):
        '''
        Se obtienen los datos de la tabla ORDER_LINE, y se muestran en una 
        listbox los campos de PRODUCT_NAME, QUANTITY
        '''
        listBox.delete(0, END)
        userInfo = self.searchUsername('CLIENT', usernameClient)
        if not userInfo:
            print(f"Usuario '{usernameClient}' no encontrado.")
            return None
        clientId = userInfo[0]['ID']
        orderInfo = self.database.table('ORDER').select('ID').eq('ID_CLIENT', clientId).eq('ID_STATUS', 2).execute()
        orderID = orderInfo.data[0]['ID']
        data = self.database.table('ORDER_LINE').select('ID_PRODUCT', 'QUANTITY').eq('ID_ORDER', orderID).execute()
        items = data.data
        if items:
            for item in items:
                idProducto = item['ID_PRODUCT']
                dataCategoria = self.database.table('PRODUCT').select('NAME').eq('ID', idProducto).execute()
                nombreProducto = dataCategoria.data[0]['NAME'] if dataCategoria.data else 'Desconocido'
                listBox.insert(END, f"Nombre: {nombreProducto} | Cantidad Adquirida: {item['QUANTITY']}")         
                
    def mostrarProductoPantallaCarrito(self, event, listBox, canvas, usernameClient):
        '''
        Esta función obtiene los datos de la ORDER_LINE que vendria a ser una especie de carrito de 
        compras, selecciona aquellas linea que tienen el ID_ORDER del usuario que ingreso sesion.
        De ahi se obtiene la informacion del producto, la cantidad y el subtotal de la linea. 
        Ademas de la imagen.
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
                user_info = self.searchUsername('CLIENT', usernameClient)
                client_Id = user_info[0]['ID']                
                order_info = self.database.table('ORDER').select('ID').eq('ID_CLIENT', client_Id).eq('ID_STATUS', 2).execute()
                orderID= order_info.data[0]['ID']              
                dataOrderLine = self.database.table('ORDER_LINE').select('QUANTITY', 'SUBTOTAL_ORDERLINE').eq('ID_PRODUCT', idProducto).eq('ID_ORDER', orderID).execute()                
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
        """
        Carga los productos desde la base de datos en un ListBox.
        """
        listBox.delete(0, END)
        data = self.database.table('PRODUCT').select('ID','NAME','IMAGE', 'PRICE', 'STOCK','ID_CATEGORY').execute()
        items = data.data
        if items:
            for item in items:
                listBox.insert(END, f" ID: {item['ID']} | Nombre: {item['NAME']} | Imagen: {item['IMAGE']} | Precio: {item['PRICE']} | Stock: {item.get('STOCK', 0)} | Categoria: {item['ID_CATEGORY']}")

    def agregarProductoTabla(self, nombreEntry, imagenEntry, precioEntry, stockEntry, categoria):
        """
        Agrega un nuevo producto a la tabla PRODUCT recibiendo como parametro lo que ingresa el manager
        desde su respectiva ventana en los entrys
        """
        name = nombreEntry.get()
        image = imagenEntry.get()
        price = precioEntry.get()
        stock = stockEntry.get()
        category = categoria.get()
        if not name or not image or not price or not stock or not category:
            messagebox.showwarning("Advertencia", "Por favor completa todos los campos.")
            return
        resultado = self.searchByRowAndKey('CATEGORIES', 'ID', 'CAT_NAME', category)
        categoryID = resultado[0]["ID"] if resultado else None
        nuevoProducto = {
            "NAME": name,
            "IMAGE": image,
            "PRICE": float(price),
            "STOCK": int(stock), 
            "ID_CATEGORY": int(categoryID)
        }
        self.database.table('PRODUCT').insert(nuevoProducto).execute()
        messagebox.showinfo("Éxito", "Producto agregado correctamente.")
        
    global selectedId
    selectedId = None 
    def actualizarValor(self, nuevoValorEntry, menuAtributoModificar, listBox):
        """
        Actualiza un atributo específico de un producto seleccionado desde el combobox y el producto que se selecciona
        desde la listbox
        """
        global selectedId
        selectedID = self.enSeleccion(listBox)
        if not selectedId:
            messagebox.showwarning("Advertencia", "Por favor selecciona un producto.")
            return
        nuevoValor = nuevoValorEntry.get()
        atributo = menuAtributoModificar.get()
        if atributo == "NAME":
            self.database.table('PRODUCT').update({"NAME": nuevoValor}).eq("ID", selectedId).execute()
        elif atributo == "IMAGE":
            self.database.table('PRODUCT').update({"IMAGE": nuevoValor}).eq("ID", selectedId).execute()
        elif atributo == "PRICE":
            self.database.table('PRODUCT').update({"PRICE": float(nuevoValor)}).eq("ID", selectedId).execute()
        elif atributo == "STOCK":
            self.database.table('PRODUCT').update({"STOCK": int(nuevoValor)}).eq("ID", selectedId).execute()
        elif atributo == "CATEGORY":
            self.database.table('PRODUCT').update({"ID_CATEGORY": int(nuevoValor)}).eq("ID", selectedId).execute()
        messagebox.showinfo("Éxito", f"{atributo} modificado correctamente.")

    def enSeleccion(self, listBox):
        """
        Captura el ID del producto seleccionado en el ListBox.
        """
        global selectedId
        selectedIndex = listBox.curselection()
        if selectedIndex:
            selectedText = listBox.get(selectedIndex)
            selectedId = int(selectedText.split('|')[0].split(':')[1].strip())
        return selectedId
    
    def setPayment(self, metodoPago, usernameCliente):
        """
        Asigna un método de pago a la orden activa de un cliente que se selecciona desde la combobox
        """
        userInfo = self.searchUsername('CLIENT', usernameCliente)
        clientId = userInfo[0]['ID']
        orderInfo = self.database.table('ORDER').select('ID').eq('ID_CLIENT', clientId).eq('ID_STATUS', 2).execute()
        orderID = orderInfo.data[0]['ID']
        # llamamos a la funcion de supabase
        self.database.rpc("set_payment_type", {"id_order": orderID, "payment_type": metodoPago}).execute()
        return True

    def setDelivery(self, metodoEnvio, usernameCliente):
        """
        Asigna un método de envío a la orden activa de un cliente desde el combobox
        """
        userInfo = self.searchUsername('CLIENT', usernameCliente)
        clientId = userInfo[0]['ID']
        orderInfo = self.database.table('ORDER').select('ID').eq('ID_CLIENT', clientId).eq('ID_STATUS', 2).execute()
        orderID = orderInfo.data[0]['ID']
        # llamamos a la funcion de supabase
        self.database.rpc("set_deliver_type", {"id_order": orderID, "deliver_type": metodoEnvio}).execute()
        return True
        
    def totalCompra(self, usernameCliente):
        """
        Obtiene el total de la orden activa de un cliente de su ORDER asignada. El total se calcula con un trigger desde SQL
        """
        userInfo = self.searchUsername('CLIENT', usernameCliente)
        clientId = userInfo[0]['ID']
        orderInfo = self.database.table('ORDER').select('*').eq('ID_CLIENT', clientId).eq('ID_STATUS', 2).execute()
        orderTotal = orderInfo.data[0]['TOTAL_ORDER']
        return orderTotal
                    
    def cambiarEstadoOrden(self, usernameCliente):
        """
        Una vez que se termina la order se cambia el estado de la orden activa de un cliente a PAGADO
        """
        userInfo = self.searchUsername('CLIENT', usernameCliente)
        clientId = userInfo[0]['ID']
        orderInfo = self.database.table('ORDER').select('ID').eq('ID_CLIENT', clientId).eq('ID_STATUS', 2).execute()
        orderID = orderInfo.data[0]['ID']
        data = {'ID_STATUS': 1}
        self.updateProduct('ORDER',orderID, data)
        
    def cambiarVentanaCarritoNulo(self, usernameCliente):
        """
        Obtiene las líneas de compra de la orden activa de un cliente para permitir si es que las hay el cambio de ventana
        """
        userInfo = self.searchUsername('CLIENT', usernameCliente)
        clientId = userInfo[0]['ID']
        orderInfo = self.database.table('ORDER').select('ID').eq('ID_CLIENT', clientId).eq('ID_STATUS', 2).execute()
        orderId = orderInfo.data[0]['ID']
        orderLineInfo = self.database.table('ORDER_LINE').select('ID').eq('ID_ORDER', orderId).execute()
        return orderLineInfo