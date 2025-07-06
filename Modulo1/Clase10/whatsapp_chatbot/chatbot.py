from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
import os
import json
from dotenv import load_dotenv
import openai

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

with open("data.json", "r", encoding="utf-8") as file:
    datos = json.load(file)

usuarios = {}
conversaciones = {}

def agregar_mensaje(numero, role, contenido):
    if numero not in conversaciones:
        conversaciones[numero] = [
            {"role": "system", "content": datos["bot"]["prompt"]},
        ]
    conversaciones[numero].append({"role": role, "content": contenido})
    conversaciones[numero] = conversaciones[numero][-10:]

def obtener_historial(numero):
    return conversaciones.get(numero, [])

def responder_openai(numero, mensaje):
    agregar_mensaje(numero, "user", mensaje)
    historial = obtener_historial(numero)
    respuesta = client.chat.completions.create(
        model="gpt-4o",
        messages=historial,
        temperature=0.7,
        max_tokens=400
    )
    contenido = respuesta.choices[0].message.content
    agregar_mensaje(numero, "assistant", contenido)
    return contenido

def generar_respuesta(numero, mensaje):
    mensaje = mensaje.lower().strip()
    estado = usuarios.get(numero, {"estado": "inicio", "nombre": None, "email": None})

    if mensaje in ["menu", "volver"]:
        estado["estado"] = "menu"
        usuarios[numero] = estado
        return "📋 *Menú principal:*\n1️⃣ Información de cursos\n2️⃣ Consultas al bot de programación\n3️⃣ Hablar con un profesor\n\n(Escribe el número de opción o 'menu' para volver aquí)"

    if estado["estado"] == "inicio" or mensaje in ["hola", "info"]:
        estado["estado"] = "esperando_datos"
        usuarios[numero] = estado
        return "Hola, bienvenido a CoderHub 👋\n¿Puedes indicarnos tu *nombre y correo electrónico*?"

    elif estado["estado"] == "esperando_datos":
        if "@" in mensaje:
            partes = mensaje.split()
            if len(partes) >= 2:
                estado["nombre"] = partes[0]
                estado["email"] = partes[1]
                estado["estado"] = "menu"
                usuarios[numero] = estado
                return f"Gracias {estado['nombre']} ✅\n\n📋 *Menú principal:*\n1️⃣ Información de cursos\n2️⃣ Consultas al bot de programación\n3️⃣ Hablar con un profesor"
            else:
                return "Por favor, escribe tu *nombre y correo electrónico* separados por un espacio."
        else:
            return "Asegúrate de incluir tu *correo electrónico*."

    elif estado["estado"] == "menu":
        if mensaje == "1":
            estado["estado"] = "info_cursos"
            usuarios[numero] = estado
            texto = "📚 *Cursos disponibles:*\n"
            for curso in datos["cursos"]:
                texto += f"{curso['id']}. {curso['nombre']}\n"
            texto += "\nEscribe el número de un curso para ver más información, o escribe 'menu' para volver al menú principal."
            return texto

        elif mensaje == "2":
            estado["estado"] = "chat"
            usuarios[numero] = estado
            return "✅ Has activado el *bot de programación*.\nHazme una pregunta, como:\n> ¿Qué es una variable en Python?\n> ¿Cómo funciona un bucle for?"

        elif mensaje == "3":
            return "📨 En breve serás atendido por un profesor. Te responderemos directamente por este medio."

        else:
            return "❓ Opción no válida. Escribe 1, 2 o 3. O 'menu' para volver."

    elif estado["estado"] == "info_cursos":
      for curso in datos["cursos"]:
          if mensaje == str(curso["id"]):
              return f"📘 *{curso['nombre']}*\n{curso['descripcion']}\n💰 Precio: {curso['precio']}\n\nEscribe 'menu' para volver al menú principal."
      return "Opción no válida. Escribe el número de un curso o 'menu'."


    elif estado["estado"] == "chat":
      return responder_openai(numero, mensaje)

    return "Lo siento, no entendí eso. Escribe 'menu' para ver las opciones disponibles."


# ---------------------- Servidor ----------------------

def manejar_peticion(handler):
  longitud = int(handler.headers['Content-Length'])
  datos = handler.rfile.read(longitud)
  datos_decodificados = urllib.parse.parse_qs(datos.decode())

  mensaje = datos_decodificados.get("Body", [""])[0]
  numero = datos_decodificados.get("From", [""])[0]

  print(f"[{numero}] Usuario: {mensaje}")
  respuesta = generar_respuesta(numero, mensaje)
  print(f"[{numero}] Bot: {respuesta}")

  handler.send_response(200)
  handler.send_header("Content-Type", "text/xml")
  handler.end_headers()

  xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Message>{respuesta}</Message>
</Response>"""

  handler.wfile.write(xml.encode("utf-8"))

def ejecutar_servidor():
  def responder(handler_self, *args):
    if handler_self.command == "POST":
        manejar_peticion(handler_self)

  class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        responder(self)

  puerto = 8080
  servidor = HTTPServer(("0.0.0.0", puerto), SimpleHTTPRequestHandler)
  print(f"🤖 Bot de CoderHub activo en http://localhost:{puerto}")
  servidor.serve_forever()

if __name__ == "__main__":
  ejecutar_servidor()
