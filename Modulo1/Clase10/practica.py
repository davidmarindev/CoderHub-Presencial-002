frases = [
  "La vida es como una bicicleta, para mantener el equilibrio debes seguir adelante.",
  "No cuentes los días, haz que los días cuenten.",
  "El único modo de hacer un gran trabajo es amar lo que haces.",
  "La felicidad no es algo hecho. Viene de tus propias acciones.",
  "El éxito es la suma de pequeños esfuerzos repetidos día tras día.",
  "No importa cuántas veces fracases, lo importante es levantarte una vez más",
  "La vida es un 10% lo que te sucede y un 90% cómo reaccionas a ello.",
  "El futuro pertenece a aquellos que creen en la belleza de sus sueños"
]

def filtrar_frases(frases, palabra):
    frases_filtradas = []
    for frase in frases:
      if palabra.lower() in frase.lower():
        frases_filtradas.append(frase)
    
    return frases_filtradas

nuevas_frases = filtrar_frases(frases, "La")
print("Frases", nuevas_frases)
print("Cantidad de frases", len(nuevas_frases))