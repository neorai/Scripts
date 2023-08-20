
## Instrucciones
Instalar dependencias primero.
Crear carpeta C:\screenshots\
Poner el PDF en modo presenteacion o pantalla completa, girar a horizontal.
Ejecutar  drmpdf_to_image.py tiene 30 segundos de delay antes de iniciarse, da tiempo a abrir el PDF o lo que dese capturar. modificar num_screenshots a numero de paginas del libro.
Ejecutar images_to_PDF_image.py
Seguir instrucciones apartado OCR

## Dependencias drmpdf_to_images y images_to_PDF_image

### Instalar Python
https://www.python.org/downloads/

### Librerias
`pip install pyautogui pillow`

`pip install img2pdf`

### WSL
`wsl --install`

`wsl --set-default-version 2`

### Docker
Docker para WSL2
https://docs.docker.com/desktop/install/windows-install/ 



## OCR
https://ocrmypdf.readthedocs.io/en/latest/docker.html#docker

`docker pull jbarlow83/ocrmypdf`

`docker tag jbarlow83/ocrmypdf ocrmypdf`

`docker run --rm -i ocrmypdf`



Ejecutar en la misma carpeta donde esta el archivo PDF_image.pdf 

`docker run -i --rm jbarlow83/ocrmypdf - - <PDF_image.pdf >PDF_OCR.pdf`