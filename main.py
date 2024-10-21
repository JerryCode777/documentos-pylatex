from pylatex import Document, Section, Subsection, Tabular, Math, NoEscape
from pylatex.utils import italic

# Crear el documento
doc = Document()

# Título y autor
doc.preamble.append(NoEscape(r'\title{Uso de PyLaTeX para Generar Documentos LaTeX}'))
doc.preamble.append(NoEscape(r'\author{Jerry Anderson Huaynacho Mango}'))
doc.preamble.append(NoEscape(r'\date{\today}'))
doc.append(NoEscape(r'\maketitle'))

# Sección de introducción
with doc.create(Section('Introducción')):
    doc.append('Este documento fue generado usando PyLaTeX, una librería de Python para crear archivos LaTeX programáticamente.')
    doc.append(' A continuación se muestran ejemplos de cómo trabajar con variables y tablas.')

# Definición de variables en Python
x = 4 
y = 10
resultado = x * y

# Sección con cálculos
with doc.create(Section('Uso de Variables en PyLaTeX')):
    doc.append(f'Definimos las variables x = {x} e y = {y}.')
    doc.append('El resultado de la multiplicación de x por y es: ')
    # Insertar la ecuación en formato LaTeX
    with doc.create(Math()):
        doc.append(f'{x} \\times {y} = {resultado}')

# Generación de una tabla dinámica
with doc.create(Section('Generación de Tablas')):
    doc.append('La siguiente tabla muestra datos generados dinámicamente:')

    # Crear una tabla
    with doc.create(Tabular('|c|c|c|')) as table:
        table.add_hline()
        table.add_row(('ID', 'Nombre', 'Edad'))
        table.add_hline()
        # Agregar filas dinámicas
        for i in range(1, 6):
            table.add_row((i, f'Persona {i}', 20 + i * 5))
            table.add_hline()

# Conclusión
with doc.create(Section('Conclusión')):
    doc.append('En este documento hemos mostrado cómo generar variables, realizar cálculos y crear tablas de manera dinámica usando PyLaTeX.')

# Generar el archivo PDF
doc.generate_pdf('pylatex_document', clean_tex=False)
