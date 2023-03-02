from PIL import ImageGrab
import time

# Ruta de la carpeta donde se guardarán las capturas de pantalla
folder_path = r'D:\\vscode project\\python capturador\\capturas\\'

# Tiempo en segundos entre cada captura de pantalla
time_between_screenshots = 1

# Contador para el nombre de las capturas de pantalla
screenshot_count = 1

while True:
    # Toma la captura de pantalla
    screenshot = ImageGrab.grab()

    # Guarda la captura de pantalla en la carpeta especificada
    screenshot.save(folder_path + 'screenshot_{}.png'.format(screenshot_count))

    # Incrementa el contador de las capturas de pantalla
    screenshot_count += 1
    print("se guardo una imagen")

    # Espera el tiempo especificado antes de tomar otra captura de pantalla
    time.sleep(time_between_screenshots)
