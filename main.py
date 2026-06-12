archivo = open("testing.txt")
texto = archivo.read().lower()
archivo.close()

lista_palabras = texto.split()

print(len(lista_palabras), "words")
print(len(texto), "characters")

palabras_repetidas = {}
for palabra in lista_palabras:
    palabras_repetidas[palabra] = palabras_repetidas.get(palabra, 0) + 1

resultado = sorted(palabras_repetidas.items(), key=lambda p: p[1], reverse=True)

for palabra, cantidad in resultado:
    print(palabra + ":", cantidad)