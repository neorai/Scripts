import re
import os

# Ruta al archivo .txt
# Ruta relativa para el archivo de entrada
archivo_entrada_rt = 'texto.txt'

# Ruta relativa para el archivo de salida
archivo_salida_rt = 'nombre_canciones.txt'


# Obtener la ruta absoluta al archivo de entrada
directorio_actual = os.path.dirname(os.path.abspath(__file__))
archivo_entrada = os.path.join(directorio_actual, archivo_entrada_rt)

# Obtener la ruta absoluta al archivo de salida
archivo_salida = os.path.join(directorio_actual, archivo_salida_rt)

with open(archivo_entrada, "r", encoding="utf-8") as file:
    texto = file.read()

patron = r'(.+)(?=https://www.shazam.com)'
resultados = re.findall(patron, texto, re.MULTILINE)

with open(archivo_salida, "w", encoding="utf-8") as file:
    for resultado in resultados:
        file.write(resultado.strip() + "\n")
