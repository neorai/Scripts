from youtubesearchpython import VideosSearch
import os

# Nombre del archivo que contiene las canciones
archivo_entrada_rt = "nombre_canciones.txt"

# Nombre del archivo en el que se guardarán los enlaces de YouTube
archivo_salida_rt = "links_youtube.txt"


# Obtener la ruta absoluta al archivo de entrada
directorio_actual = os.path.dirname(os.path.abspath(__file__))
archivo_entrada = os.path.join(directorio_actual, archivo_entrada_rt)

# Obtener la ruta absoluta al archivo de salida
archivo_salida = os.path.join(directorio_actual, archivo_salida_rt)

# Lista para almacenar los enlaces de YouTube
enlaces_youtube = []

# Leer el archivo de canciones
with open(archivo_entrada, "r", encoding="utf-8") as archivo:
    canciones = archivo.readlines()

# Buscar los enlaces de YouTube para cada canción
for cancion in canciones:
    cancion = cancion.strip()  # Eliminar los espacios en blanco y saltos de línea
    
    # Buscar la canción en YouTube
    videos_search = VideosSearch(cancion, limit=1)
    resultados = videos_search.result()["result"]
    
    # Obtener el primer resultado (enlace)
    if len(resultados) > 0:
        enlace = resultados[0]["link"]
        enlaces_youtube.append(enlace)

# Guardar los enlaces de YouTube en el archivo de resultados
with open(archivo_salida, "w", encoding="utf-8") as archivo:
    for enlace in enlaces_youtube:
        archivo.write('yt-dlp.exe --extract-audio --audio-quality best --audio-format mp3 ' + enlace + "\n")

print("¡Búsqueda completada! Los enlaces se han guardado en", archivo_salida)
