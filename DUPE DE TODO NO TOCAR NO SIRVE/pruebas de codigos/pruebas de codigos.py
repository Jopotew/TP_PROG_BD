import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

# Diccionario con la información de la imagen
producto = {
    'descripcion': 'Producto de Ejemplo',
    'imagen': "https://img.freepik.com/foto-gratis/cerca-manzana-fresca_144627-14640.jpg?w=826&t=st=1726583142~exp=1726583742~hmac=1595c1d7d65547bb2e2b3d2d43fb3711ef8ec41a56e5a80fe86d70245d05381b",  # URL de la imagen
    'precio': '$10.00'
}

class VentanaConCanvas:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Imagen en Canvas")

        # Crear un canvas
        self.canvas = tk.Canvas(self.root, width=400, height=300)
        self.canvas.pack()

        # Extraer la URL de la imagen del diccionario
        url_imagen = itemMercado[0].image
        imagen_bytes = BytesIO(url_imagen)
        imagen = Image.open(imagen_bytes)
        # Redimensionar la imagen (por ejemplo, a 200x150 píxeles)
        nuevo_tamano = (200, 150)  # Definir el tamaño deseado
        imagen_redimensionada = imagen.resize(nuevo_tamano)
        imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)
        self.canvas.create_image(200, 150, image=imagen_tk)
        self.canvas.image = imagen_tk
            
            # Mostrar descripción y precio en el canvas
            self.canvas.create_text(200, 250, text=producto['descripcion'], fill='black', font=('Arial', 12))
            self.canvas.create_text(200, 270, text=producto['precio'], fill='black', font=('Arial', 12))
        else:
            print("Error al descargar la imagen.")
        
        self.root.mainloop()

if __name__ == "__main__":
    app = VentanaConCanvas()
