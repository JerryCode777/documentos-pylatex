# Proyecto de Generación de Documentos con PyLaTeX

Este proyecto utiliza **PyLaTeX**, una biblioteca de Python, para generar documentos en formato LaTeX de manera programática. Este enfoque permite automatizar la creación de documentos, lo que es especialmente útil para la generación de informes, cartas, facturas, o cualquier tipo de contenido que requiera un formato consistente y personalizable.

## Contenido del Proyecto

- **Dockerfile**: Archivo que configura el entorno de Docker para ejecutar el proyecto.
- **main.py**: Script en Python que genera un documento LaTeX y lo compila en un PDF.
- **pylatex_document.tex**: Documento LaTeX generado (si se mantiene `clean_tex=False` en el script).
- **pylatex_document.pdf**: Archivo PDF generado a partir del documento LaTeX.

## Instalación

Para ejecutar este proyecto, necesitarás tener Docker instalado en tu máquina. Sigue estos pasos:

1. **Clona este repositorio** o descarga los archivos necesarios.
2. **Construye la imagen de Docker**:
   ```bash
   docker build -t pylatex_docker .

3. **Ejecuta el contenedor**:
docker run -v C:/ruta/a/tu/directorio:/app pylatex_docker
