# Entornos virtuales en python.

# Son una herramienta que permite crear entornos aislados para proyectos de Python, 
# evitando conflictos entre dependencias y versiones de paquetes.


# Los entornos virtuales no se guardan en el repositorio de código, por lo que no se 
# suben a GitHub, Si quieres tener la misma configuración en otro equipo, debes 
# crear un nuevo entorno virtual y reinstalar las dependencias.

# Ejemplo de como hacerlo con las carpetas de esta clase:

# git clone url de este repositorio
# cd Modulo1/Clase10/whatsapp_chatbot
# python -m venv .
# source venv/bin/activate        # o venv\Scripts\activate en Windows
# pip install -r requirements.txt -> Este comando instala todas las dependencias del proyecto

# Cabe destacar que el archivo requirements.txt es un archivo que contiene una lista de todas 
# las dependencias del proyecto y se crea con el comando pip freeze > requirements.txt