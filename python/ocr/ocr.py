import os
import io
from PIL import Image
import pytesseract
import fitz  # PyMuPDF

def tiene_imagenes(ruta_pdf):
    doc = fitz.open(ruta_pdf)
    for pagina_num in range(doc.page_count):
        pagina = doc[pagina_num]
        imagenes = pagina.get_images(full=True)
        if imagenes:
            return True
    return False

def extraer_texto_imagen(image_bytes):
    try:
        image = Image.open(io.BytesIO(image_bytes))
        texto = pytesseract.image_to_string(image)
        return texto
    except Exception as e:
        print(f"No se pudo procesar la imagen: {e}")
        return ""

def guardar_en_archivo(texto, nombre_archivo):
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        archivo.write(texto)

def procesar_pdfs_con_imagenes_en_ruta(carpeta_salida='resultados'):
    # Obtener la ruta del directorio del script
    ruta_script = os.path.dirname(__file__)
    ruta_carpeta = os.path.join(ruta_script, carpeta_salida)

    if not os.path.exists(ruta_carpeta):
        os.makedirs(ruta_carpeta)

    for nombre_archivo in os.listdir(ruta_script):
        ruta_archivo = os.path.join(ruta_script, nombre_archivo)

        if os.path.isfile(ruta_archivo) and ruta_archivo.lower().endswith('.pdf') and tiene_imagenes(ruta_archivo):
            doc = fitz.open(ruta_archivo)
            texto = ""

            for pagina_num in range(doc.page_count):
                pagina = doc[pagina_num]
                imagenes = pagina.get_images(full=True)

                for img_idx, img_info in enumerate(imagenes):
                    xref = img_info[0]
                    base_image = doc.extract_image(xref)
                    image_bytes = base_image["image"]
                    texto += extraer_texto_imagen(image_bytes)

            nombre_archivo_salida = os.path.splitext(nombre_archivo)[0] + '_resultado.txt'
            ruta_archivo_salida = os.path.join(ruta_carpeta, nombre_archivo_salida)

            guardar_en_archivo(texto, ruta_archivo_salida)
            print(f"Texto extraído y guardado en '{ruta_archivo_salida}' para: {nombre_archivo}")

if __name__ == "__main__":
    procesar_pdfs_con_imagenes_en_ruta()
