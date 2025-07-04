import json

archivo_json = open("personas.json", "r")
personas = json.load(archivo_json)
archivo_json.close()

print("Personas:", personas)

nombre_del_nuevo_archivo = "Archivo/archivo_prueba.txt"

archivo_nuevo = open(nombre_del_nuevo_archivo, "w")

for persona in personas:
    if persona["active"]:
        archivo_nuevo.write(f"{persona['nombre']} - {persona['edad']} - {persona['ci']}\n")

archivo_nuevo.close()
print(f"Archivo creado: {nombre_del_nuevo_archivo}")
