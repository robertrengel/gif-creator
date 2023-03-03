import os
from PIL import Image

# Definir el número de imágenes y la ruta de la carpeta
num_images = 144
folder_path = os.path.abspath("capturas")

# Definir las variables para el tamaño de las imágenes
#dimensiones de imagen original
origin_width = 1920
origin_height = 1080

#dimenciones de imagen final
final_width = 800
finally_height = 500

# Crear una lista para almacenar las imágenes
images_path = []
images = []

left = (origin_width - final_width) / 2
top = (origin_height - finally_height) / 2
right = left + final_width
bottom = top + finally_height


# Bucle para cargar las imágenes y agregarlas a la lista
for i in range(10, num_images+1):
    # Construir la ruta de la imagen
    img_path = os.path.join(folder_path, f"screenshot_{i}.png")

    images_path.append(img_path)

for path in images_path:
    try:
        with Image.open(path) as img:
            # Recorta la imagen
            cropped_img = img.crop((left, top, right, bottom))
            # Agrega la imagen recortada a la lista
            images.append(cropped_img)
    except(FileNotFoundError):
        continue
        
    
# Guardar las imágenes en un archivo GIF
images[0].save("animacion.gif", save_all=True, append_images=images[1:], optimize=True, duration=1000, loop=0)
print("La animación ha sido creada")
