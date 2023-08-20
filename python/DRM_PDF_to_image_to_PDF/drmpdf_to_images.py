import pyautogui
import time
from PIL import ImageGrab, Image
import os

# Tiempo de espera antes de iniciar el script (en segundos)
initial_delay = 30

print(f"El script comenzará en {initial_delay} segundos...")
time.sleep(initial_delay)

# Configuración
num_screenshots = 5  # Número de capturas de pantalla a tomar
output_directory = "C:\\screenshots\\"  # Directorio donde se guardarán las capturas

# Crea el directorio de salida si no existe
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Función para capturar y guardar la pantalla
def capture_and_save_screenshot(filename):
    screenshot = ImageGrab.grab()
    screenshot.save(filename)

# Bucle para tomar capturas y simular la tecla de flecha abajo
for i in range(num_screenshots):
    # Captura y guarda la captura de pantalla
    screenshot_name = f"{output_directory}{i+1}.png"
    capture_and_save_screenshot(screenshot_name)
    print(f"Captura de pantalla {i+1} guardada como {screenshot_name}")

    # Carga la captura de pantalla y gira 90 grados hacia la derecha
    screenshot = Image.open(screenshot_name)
    rotated_screenshot = screenshot.rotate(-90, expand=True)
    rotated_screenshot.save(screenshot_name)  # Sobrescribe la captura con la versión girada
    
    # Simula la tecla de flecha abajo
    pyautogui.press('down')
    print("Tecla de flecha abajo presionada")

    # Espera un poco antes de la siguiente iteración
    time.sleep(2)  # Ajusta este valor según sea necesario

print("Capturas de pantalla completado")
