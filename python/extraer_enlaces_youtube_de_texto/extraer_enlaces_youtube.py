import os
import re

def extraer_enlaces_youtube(texto):
    # Expresión regular para encontrar los enlaces de YouTube
    patron = r'(https?://youtu.be/[^\s]+)'
    
    # Buscar todos los enlaces de YouTube en el texto
    enlaces_youtube = re.findall(patron, texto)
    
    return enlaces_youtube

# Ruta relativa para el archivo de entrada
ruta_relativa = 'texto.txt'

# Obtener la ruta absoluta al archivo de entrada
directorio_actual = os.path.dirname(os.path.abspath(__file__))
archivo_entrada = os.path.join(directorio_actual, ruta_relativa)

try:
    with open(archivo_entrada, 'r', encoding='utf-8') as file:
        texto = file.read()

    enlaces_youtube = extraer_enlaces_youtube(texto)

    # Ruta relativa para el archivo de salida
    archivo_salida = 'enlaces_youtube.txt'

    # Obtener la ruta absoluta al archivo de salida
    archivo_salida = os.path.join(directorio_actual, archivo_salida)

    with open(archivo_salida, 'w', encoding='utf-8') as file:
        for enlace in enlaces_youtube:
            file.write('yt-dlp.exe --extract-audio --audio-quality best --audio-format mp3 ' + enlace + '\n')

    print(f"Los enlaces de YouTube se han guardado en el archivo '{archivo_salida}'.")

except FileNotFoundError:
    print(f"No se encontró el archivo '{archivo_entrada}'.")
