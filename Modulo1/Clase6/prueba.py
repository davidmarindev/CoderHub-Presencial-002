from gtts import gTTS

def text_to_speech(text, lang='es', slow=False):
    """
    Convierte el texto proporcionado a voz y lo guarda en un archivo mp3.

    :param text: Texto a convertir a voz.
    :param lang: Idioma del texto (por defecto 'es' para español).
    :param slow: Si es True, la voz se reproducirá más lentamente.
    """
    tts = gTTS(text=text, lang=lang, slow=slow)
    tts.save("output.mp3")
    print("El texto ha sido convertido a voz y guardado como output.mp3")
    
tts = gTTS("Hola esto es un ejemplo de la clase 6 de python, CR7 es el goat")
tts.save('prueba.mp3')


