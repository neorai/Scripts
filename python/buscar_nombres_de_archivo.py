import os

def buscar_por_cadena(carpeta, cadena):
    resultados = []
    for ruta_actual, carpetas, archivos in os.walk(carpeta):
        for archivo in archivos:
            if archivo.lower().find(cadena.lower()) != -1:
                ruta_completa = os.path.join(ruta_actual, archivo)
                resultados.append(ruta_completa)
        for carpeta in carpetas:
            if carpeta.lower().find(cadena.lower()) != -1:
                ruta_completa = os.path.join(ruta_actual, carpeta)
                resultados.append(ruta_completa)


def guardar_resultados(resultados, nombre_archivo):
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        for resultado in resultados:
            archivo.write(resultado + '\n')
            

        
# Carpeta de búsqueda
carpeta_raiz = r"D:\cursos"
cadena_busqueda = input('Ingrese la cadena de búsqueda: ')

# Buscar archivos y guardar resultados
resultados = buscar_por_cadena(carpeta_raiz, cadena_busqueda)
nombre_archivo_salida = 'resultados.txt'
guardar_resultados(resultados, nombre_archivo_salida)

print('Búsqueda finalizada. Los resultados se han guardado en', nombre_archivo_salida)
