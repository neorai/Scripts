import os
import img2pdf

# Carpeta que contiene las imágenes PNG
folder_path = r'C:\screenshots'

# Nombre del archivo PDF de salida
output_pdf = 'C:\screenshots\PDF_image.pdf'

# Función para obtener la lista de archivos PNG en la carpeta
def get_png_files_in_folder(folder_path):
    png_files = [file for file in os.listdir(folder_path) if file.lower().endswith('.png')]
    return png_files

# Función para convertir imágenes a PDF
def convert_images_to_pdf(image_paths, output_pdf):
    with open(output_pdf, "wb") as pdf_file:
        pdf_file.write(img2pdf.convert(image_paths))

# Obtener la lista de archivos PNG en la carpeta
png_files = get_png_files_in_folder(folder_path)

# Convertir la lista de nombres de archivos a rutas completas
image_paths = [os.path.join(folder_path, file) for file in png_files]

# Llamar a la función para crear el PDF
convert_images_to_pdf(image_paths, output_pdf)

print(f"Se ha creado el archivo PDF: {output_pdf}")
