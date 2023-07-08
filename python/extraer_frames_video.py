import cv2
import os

def extract_frames(video_path, output_path):
    # Abre el video
    video = cv2.VideoCapture(video_path)

    # Crea la carpeta de salida si no existe
    os.makedirs(output_path, exist_ok=True)

    # Inicializa variables
    frame_count = 0
    success = True

    # Extrae los fotogramas hasta que no haya más
    while success:
        # Lee el siguiente fotograma
        success, frame = video.read()

        if success:
            # Guarda el fotograma en un archivo de imagen
            frame_path = os.path.join(output_path, f"frame_{frame_count}.jpg")
            cv2.imwrite(frame_path, frame)

            frame_count += 1

    # Cierra el video
    video.release()

    print(f"Se extrajeron {frame_count} fotogramas.")

# Ejemplo de uso
video_path = r"C:\Users\rai\Desktop\videos\video_calle.mp4"
output_path = r"C:\Users\rai\Desktop\videos\frames_video_calle"

extract_frames(video_path, output_path)
