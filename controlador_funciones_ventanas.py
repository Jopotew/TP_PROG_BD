import requests
from io import BytesIO
from PIL import Image, ImageTk
from data_base_class import DataBase
from client_class import Client
from manager_class import Manager
import controlador_queue
import sys
from tkinter import messagebox

baseDatos = DataBase()

# Controlador de funciones que funciona como intermediario entre las ventanas, las clases y la base de datos

def cerrar():
    print("Cerrando ventana...")
    exit(0)

def cargarProductos(listBox):    
    '''
    Funcion que carga los productos en la ventana para luego ser mostrados en la listbox
    '''
    baseDatos.cargarProdutosMercado(listBox)
        
def mostrarProductos(listBox,event, canvas):
    '''
    Funcion que muestra los productos en la ventana
    '''
    baseDatos.mostrarProductoPantalla(listBox, event, canvas)
        
def mostrarProductoPorCategoria(listBox, event, menuCategoria):
    '''
    Al seleccionar una categoria del menu desplegable se muestran los prouctos en el listbox filtrados
    por la categoria seleccionada
    '''
    baseDatos.cargarProductosFiltrados(listBox, event, menuCategoria)
    
def cargarProductosCarrito(listBox, clienteComprando):
    '''
    Funcion que carga los productos en la ventana carrito para que luego se muestren en la pantalla
    '''
    baseDatos.cargarProdutosCarrito(listBox, clienteComprando)
    
def mostrarProductosPantallaCarito(event, listBox, canvas, usernameClient):
    '''
    Funcion que muestra los productos en la ventana carrito
    '''
    baseDatos.mostrarProductoPantallaCarrito(event, listBox, canvas, usernameClient)
    
def cargarProductoManagerManager(listBox):
    '''
    Funcion que carga los productos en la ventana de manager
    '''
    baseDatos.cargarProductoManager(listBox)

def agregarNuevoProductoTabla(nombreEntry, imagenEntry, precioEntry, stockEntry, CategoriaEntry, listBox):
    '''
    Se obtienen los datos de los entrys de la ventana manager para que puedan se agregados a la tabla correspondiente
    a traves de las funciones de database.
    Al finalizar se vuelven a cargar los productos para actualizar la listbox
    '''
    baseDatos.agregarProductoTabla(nombreEntry, imagenEntry, precioEntry, stockEntry, CategoriaEntry)
    baseDatos.cargarProductoManager(listBox)
    
def actualizarAtributo(nuevoValorEntry, menuAtributoModificar, listBox):
    '''
    Se recibe el atributo que se desea modificar desde el entry, como tambien el valor del combobox
    '''
    baseDatos.actualizarValor(nuevoValorEntry, menuAtributoModificar, listBox)
    baseDatos.cargarProductoManager(listBox)
    
def seleccion(event, listBox):
    '''
    Funcion que permite obtener informacion del dato que se selecciono de la listbox
    '''
    baseDatos.enSeleccion(event, listBox)
    
def cerrarVentanaX(ventana):
    '''
    Funcion para cerrar cualquier ventana y que se ejecute un EXIT 0 asi deja de correr el programa
    '''
    print("Cerrando la ventana...")
    ventana.destroy()
    sys.exit(0)
    
def iniciarCompra(username, ventana, password):
    '''
    Cuando aparece la ventana de inicio de sesion, el cliente ingresa sus datos y son usados por esta funcion
    para que pueda validarse la contraseña y asi se realice el cambio de pantalla. 
    Aqui se validan las credenciales del usuario
    '''
    password2 = password.get()
    username2 = username.get()
    if username2 and password2 != None:
        access = Client.checkPw(password2, username2)
        if access == True:
            userInfo = baseDatos.searchUsername('CLIENT', username2)
            nameClient = userInfo[0]['NAME']
            usernameClient = userInfo[0]['USERNAME']
            mailClient = userInfo[0]['MAIL']
            passwordClient = userInfo[0]['PASSWORD']
            imageClient = userInfo[0]['IMAGE']
            clienteComprando = Client(nameClient, usernameClient, passwordClient, mailClient, imageClient)
            baseDatos.checkAndCreateOrder(username2)
            messagebox.showinfo("La Amistad", f"Bienvenido al supermerrcado La Amistad {username2}!")
            pantallaMenuProductosAppear(ventana, clienteComprando)
            return clienteComprando
        else:
            messagebox.showwarning("La Amistad", "Usuario o contraseña incorrecto. Intente nuevamente")        

def iniciarSesionManager(username, password, accessKey, ventana):
    '''
    Realiza lo mismo que el inicioSesionCliente solo que no instancia como objeto al manager y ademas de validar
    la contraseña valida el access key que se le genera de manera random y automatica a la hora de registrar
    un usuario. Una vez verificadas las credenciales se hace el pase de pantalla
    '''
    password2 = password.get()
    username2 = username.get()
    accessKey2 = accessKey.get()
    if username2 and password2 and accessKey2 != None:
        access = Manager.checkPw(password2, username2, accessKey2)
        if access == True:
            messagebox.showinfo("La Amistad", f"Bienvenido al supermerrcado La Amistad {username2}!")
            pantallaProductosManager(ventana)
        else:
            messagebox.showwarning("La Amistad", "Usuario o contraseña incorrecto. Intente nuevamente")        

def createNewUser(name, username, mail, password, image, ventana):
    '''
    Se obtienen todos los datos necesarios para crear el cliente y almacenarlo en la base de datos
    '''
    name2 = name.get()
    username2 = username.get()
    mail2 = mail.get()
    password2 = password.get()
    image2 = image.get()
    if len(password2) < 8:
        messagebox.showerror("La Amistad", "Debe de ingresar un password que tenga 8 caracteres como minimo")
    else:
        Client.createUser(password2, name2, username2, mail2, image2)
        messagebox.showinfo("La Amistad", "Usuario creado correctamente!")
        pantallaInicioCliente(ventana)
    
def createNewManager(name, username, mail, password, image, ventana):
    '''
    Se obtienen los datos ddel manager necesarios para crearlo y luego se almacena en la base de datos
    '''
    name2 = name.get()
    username2 = username.get()
    mail2 = mail.get()
    password2 = password.get()
    image2 = image.get()
    accessKey = Manager.createUser(password2, name2, username2, mail2, image2)
    messagebox.showinfo("La Amistad", f"Usuario creado correctamente! Su access Key es{accessKey}")
    PantallaInicioSesionManager(ventana)
    
def agregarProductoCarrito(listBox, usernameCliente, ventana):
    '''
    Funcion que permite agregar un producto al carrito (tabla ORDER_LINE) del cliente a traves 
    de la seleccoion de la Listbox 
    '''
    baseDatos.newOrderLine(listBox, usernameCliente)
    siguiente = messagebox.showinfo("La Amistad", "Producto agregado exitosamente al carrito!")
    if siguiente:
        ventana.update()    
    
def agregarProductoVentanaCarrito(listBox, usernameCliente, ventana):
    '''
    Funcion que permite agregar un producto al carrito (tabla ORDER_LINE) del cliente a traves 
    de la seleccoion de la Listbox 
    '''
    baseDatos.newOrderLine(listBox, usernameCliente)
    baseDatos.cargarProdutosCarrito(listBox, usernameCliente)
    siguiente = messagebox.showinfo("La Amistad", "Producto agregado exitosamente al carrito!")
    if siguiente:
        ventana.update()
    
def eliminarProductoCarrito(listBox, usernameCliente, ventana):
    '''
    Funcion que permite eliminar un productos seleccionado de la Listbox del carrito (tabla ORDER_LINE)
    '''
    baseDatos.removeOrderLine(listBox,usernameCliente)
    siguiente = messagebox.showinfo("La Amistad", "Producto eliminado del carrito exitosamente")
    if siguiente:
        ventana.update()
    

def iniciarPago(fila, ventana, canvas, clienteComprando):
    '''
    Funcion que ejecuta la creacion de clientes NPC para formar la fila. Cuando se invoca la funcion se posicionan
    2 NPC - CLIENTE - 2 NPC.
    Aqui se inica la queue
    '''
    dibujarImagenes(canvas, fila)
    controlador_queue.removeFromQueue(fila)
    dibujarImagenes(canvas, fila)
    controlador_queue.removeFromQueue(fila)
    dibujarImagenes(canvas, fila)
    pagar = messagebox.showinfo("La Amistad", "Es tu turno de pagar! A continuacion, selecciona el metodo de pago y de delivery que deseas")
    if pagar:
        ventanaPagoCompra(ventana, clienteComprando)
        
def cargarYRedimensionarImagen(self, url):
    '''
    Funcion que recibe una url de una imagen y la redimensiona para luego ser utilizada en la ventana
    '''
    response = requests.get(url)
    if response.status_code == 200:
        imagen_bytes = BytesIO(response.content)
        imagen = Image.open(imagen_bytes)
        return imagen.resize((105, 105))
    return None

def dibujarImagenes(canvas, fila):
    '''
    Funcion que dibuja las imagenes en la ventana de la fila para que siga esa idea de "movimiento"
    '''
    posiciones = [(503.0, 334.0), (337.0, 173.0), (220.0, 173.0), (103.0, 173.0)]
    images = [None] * 4
    for i in range(4):
        imagen_url = fila.clientInQueue[i].image
        response = requests.get(imagen_url)
        if response.status_code == 200:
            imagen_bytes = BytesIO(response.content)
            imagen = Image.open(imagen_bytes).resize((105, 105))
            images[i] = ImageTk.PhotoImage(imagen)
            canvas.create_image(posiciones[i][0], posiciones[i][1], image=images[i], anchor="center")
        canvas.update()
    return images

def finalizarCompra(combobox1, combobox2, usernameCliente, ventana):
    '''
    Funcion que se invoca cuando ya es tu turno de pagar, aqui el usuario ingresa lo que vendria a ser su medio de
    pago, el supuesto metodo de envio y todo esto se almacena en la base de datos (ORDER)
    '''
    metodoEnvio = combobox1.get()
    formaPago = combobox2.get()
    pago = baseDatos.setPayment(formaPago, usernameCliente)
    envio = baseDatos.setDelivery(metodoEnvio, usernameCliente)
    if envio and pago:
        baseDatos.cambiarEstadoOrden(usernameCliente)
        pagar = messagebox.showinfo("La Amistad", f"Muchas gracias por tu compra. Que tengas un excelente dia {usernameCliente}!")
        if pagar:
            ventana.quit()
            ventana.destroy()
            exit(0)

def totalCompra(usernameCliente):
    '''
    Funcion que obtiene el total de la compra de la tabla "ORDER" de la base de datos
    '''
    totalCompra = baseDatos.totalCompra(usernameCliente)
    return totalCompra

def cambioCarrito(ventana, usernameCliente, clienteComprando):
    '''
    Funcion que valida que tengas una order con alguna order_line, de no ser asi no permite el cambio de 
    pantalla (carrito)
    '''
    orderLineInfo = baseDatos.cambiarVentanaCarritoNulo(usernameCliente)
    if not orderLineInfo.data:
        messagebox.showwarning("La Amistad", "Para poder continuar debes tener algun producto en el carrito. Agrega algo para ver tu carrito!")
    else:
        pantallaCarritoAppear(ventana, clienteComprando)


'''
A continuacion se detallan las funciones que hay que invocar para pasar de una ventana a la otra, cerrando la ventana en la
que se estaba previemante. El modelo a seguir es facil, se cierra la ventana actual (ventana.withdraw()) y 
luego se crea la ventana que le sigue a esa (from ventanaX import ventana X -> ventanaX())
'''
def pantallaCarritoAppear(ventana, clienteComprando):
    ventana.withdraw()
    from ventana_carrito_cliente import ventanaCarrito
    ventanaCarrito(clienteComprando)

def pantallaMenuProductosAppear(ventana, clienteComprando):
    ventana.withdraw()
    from ventana_productos_cliente import ventanaProductosMercado
    ventanaProductosMercado(clienteComprando)
    
def volverPantallaMercado(ventana, clienteComprando):
    ventana.withdraw()
    from ventana_productos_cliente import ventanaProductosMercado
    ventanaProductosMercado(clienteComprando)
    
def pantallaInicioCliente(ventana):
    ventana.withdraw()
    from ventana_inicio_cliente import ventanaInicio
    ventanaInicio()
    
def pantallaCreacionUsuario(ventana):
    ventana.withdraw()
    from ventana_registro_usuario import ventanaUserCreator
    ventanaUserCreator()
    
def PantallaInicioSesionManager(ventana):
    ventana.withdraw()
    from ventana_inicio_manager import ventanaInicioManager
    ventanaInicioManager()
    
def pantallaCreacionUsuarioManager(ventana):
    ventana.withdraw()
    from ventana_registro_manager import ventanaManagerCreator
    ventanaManagerCreator()

def pantallaProductosManager(ventana):
    ventana.withdraw()
    from ventana_productos_manager import ventanaManager
    ventanaManager()

def pantallaInicioGral(ventana):
    ventana.withdraw()
    from ventana_inicio_gral import venInicioMercado
    venInicioMercado()
    
def ventanaFilaCliente(ventana, clienteComprando):
    ventana.withdraw()
    from ventana_fila_cliente import ventanaFila
    fila = controlador_queue.initializeQueue(clienteComprando)
    ventanaFila(clienteComprando, fila)
    
def ventanaPagoCompra(ventana, clienteComprando):
    ventana.withdraw()
    from ventana_pago_delivery_cliente import ventanaPago
    ventanaPago(clienteComprando)
    
def volverPantallaInicioSesion(ventana):
    ventana.withdraw()
    from ventana_inicio_cliente import ventanaInicio
    ventanaInicio()