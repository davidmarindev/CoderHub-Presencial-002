import openpyxl
import json

wb = openpyxl.Workbook()  # Crea un nuevo libro de trabajo
ws = wb.active  # Obtiene la hoja activa del libro de trabajo
ws.title = "Estudiantes"  # Cambia el título de la hoja activa

archivo = open('Estudiantes/estudiantes.json', 'r')  # Abre el archivo en modo lectura y escritura
estudiantes = json.load(archivo)  # Carga el contenido del archivo JSON
archivo.close()  # Cierra el archivo

ws.append(["Nombre", "Edad", "Carrera"])  # Agrega los encabezados de las columnas

for estudiante in estudiantes:
    ws.append([estudiante["nombre"], estudiante["edad"], estudiante["carrera"]])  # Agrega cada estudiante a la hoja
    
wb.save("Estudiantes/archivo_estudiantes.xlsx")  # Guarda el libro de trabajo en un archivo Excel
