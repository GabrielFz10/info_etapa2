'''
Métodos y propiedades de string
Indexar estructuras de datos
Todos los tipos de datos

Se te pide crear un programa que le pida al usuario que ingresar un texto cualquiera, por ejemplo, un artículo o una frase.
Luego el programa le va a pedir al usuario que también ingrese 3 letras a su elección.
Nuestro código va a procesar esa información para realizar los análisis necesarios para devolverle al usuario la siguiente información:

1- Cantidad de veces que aparece cada una de letras que eligió.
    Tip 1: almacenar las letras en una lista para usar algún método de contar un substring en un
string
    Tip 2: al buscar las letras puede haber mayúscula y minúsculas. Para asegurar que se
encuentren todas las letras, pasa tanto el texto original como las letras a buscar a
minúscula.
2- Cuantas palabras hay en total en todo el texto.
    Tip 3: usa métodos para transformar el texto en lista de palabras y para calcular su longitud.
3- Cual es la primera letra y cuál es la última. (Indexación)
4- Mostrar el texto en orden inverso.
5- Decir si la palabra "python" aparece en el texto.
    Tip 4: usa bool para verificar si se encuentra, y un diccionario para asociar el booleano con un
string para mostrar al usuario
'''

texto = input("Ingrese un texto: ").lower()
letras = list(input("Ingrese 3 letras: ").lower()) # defino la lista de letras en la misma entrada de datos

#texto_minusc = texto.lower()
#letras_minusc = letras.lower()

# 1- Cantidad de veces que aparece cada una de letras que eligió.
veces = []
for letra in letras:
    conteo_letras = texto.count(letra) # contamos las letras
    veces.append(conteo_letras) # añadimos las letras YA contadas a una nueva lista
print(f'Las letras": {letras}, aparecen: {veces} veces en el texto') # mostramos las letras y las veces que aparecen en el texto.

# 2- Cuantas palabras hay en total en todo el texto.
cantidad_palabras = len(texto.split())
print(f'Hay {cantidad_palabras} palabras en el texto')

# 3- Cual es la primera letra y cuál es la última. (Indexación)
primera_letra = texto[0]
ultima_letra = texto[-1]
print(f"La primera letra es {primera_letra} y la última letra es {ultima_letra}")

# 4- Mostrar el texto en orden inverso.
texto_inverso = texto[::-1]
print(f"El texto en orden inverso es: {texto_inverso}")

# 5- Decir si la palabra "python" aparece en el texto.
if "python" in texto:
    encontrado = True
else:
    encontrado = False

diccionario_resultado = {True: "La palabra 'python' aparece en el texto.", False: "La palabra 'python' no aparece en el texto"}