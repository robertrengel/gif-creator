import os
from PIL import Image

# Definir el número de imágenes y la ruta de la carpeta
num_images = 147
folder_path = "ruta/a/la/carpeta"

# Definir las variables para el tamaño de las imágenes
width = 800
height = 600

# Crear una lista para almacenar las imágenes
images = []

# Bucle para cargar las imágenes y agregarlas a la lista
for i in range(1, num_images+1):
    # Construir la ruta de la imagen
    img_path = os.path.join(folder_path, f"imagen_{i}.png")
    
    # Cargar la imagen usando Pillow
    img = Image.open(img_path)
    
    # Cambiar el tamaño de la imagen
    img = img.resize((width, height))
    
    # Agregar la imagen a la lista
    images.append(img)
    
# Guardar las imágenes en un archivo GIF
images[0].save("animacion.gif", save_all=True, append_images=images[1:], optimize=False, duration=100, loop=0)
