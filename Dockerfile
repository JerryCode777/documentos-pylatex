FROM python:3.10-slim

# Actualizar los repositorios y luego instalar texlive-latex y sus dependencias
RUN apt-get update && apt-get install -y \
    texlive-latex-recommended \
    texlive-fonts-recommended \
    texlive-latex-extra \
    latexmk

# Instalar pylatex
RUN pip install pylatex

# Crear directorio de trabajo
WORKDIR /app

# Copiar archivos al contenedor
COPY . /app

# Comando por defecto
CMD ["python", "main.py"]
