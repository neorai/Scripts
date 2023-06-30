import os
import cv2

VIDEO_EXTENSIONS = ['.mp4', '.avi', '.mkv']

def calcular_total_minutos(carpeta_raiz):
    total_minutos = 0

    for ruta_carpeta, _, archivos in os.walk(carpeta_raiz):
        for archivo in archivos:
            ruta_archivo = os.path.join(ruta_carpeta, archivo)
            extension = os.path.splitext(ruta_archivo)[1]
            if extension.lower() in VIDEO_EXTENSIONS:
                try:
                    video = cv2.VideoCapture(ruta_archivo)
                    fps = video.get(cv2.CAP_PROP_FPS)
                    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
                    duracion = frame_count / fps / 60  # Convertir a minutos
                    total_minutos += duracion
                    video.release()
                except Exception as e:
                    print(f"Error al procesar {ruta_archivo}: {e}")
            else:
                print(f"Ignorando archivo no válido: {ruta_archivo}")

    return total_minutos

# Carpeta raíz donde se encuentran los archivos de video
carpeta_raiz = r"D:\cursos"

total_minutos = calcular_total_minutos(carpeta_raiz)
print(f"El total de minutos de los archivos de video es: {round(total_minutos,2)} minutos.")
total_horas = total_minutos / 60
print(f"El total de horas de los archivos de video es: {round(total_horas,2)} horas.")
