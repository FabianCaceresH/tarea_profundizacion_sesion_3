# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con texto
a = str(input("ingrese la primera palabra:"))
b = str(input("ingrese la segunda palabra:"))
c = str(input("ingrese la tercera palanra:"))
d = len(a)
e = len(b)
f = len(c)
if a > b and a > c :
    print(f"{a} es mayor")
elif b > a and b > c :
    print(f"{b} es mayor")
elif c > a and c > b :
    print(f"{c} es mayor")
if d > e and d > f:
    print(f"{a} es la palabra que contiene mas caracteres ")
elif e > d and e > f:
    print(f"{b} es la palabra que contiene mas caracteres  ")
elif f > d and f > e:
    print(f"{c} es la palabra que contiene mas caracteres ")
if d < e and d < f:
    print(f"{a} es la palabra que contiene menos caracteres ")    
elif e < d and e < f:
    print(f"{b} es la palabra que contiene menos caracteres")
elif f < e and f < d:
    print(f"{c} es la palabra que contiene menos caracteres")
if d > e > f:
    print(f"el orden es {a},{b},{c}")
elif d > f > e:
    print(f"el orden es {a},{c},{b}")
elif e > f > d:
    print(f"el orden es {b},{c},{a}")
elif e > d > f:
    print(f"el orden es {b},{a},{c}")
elif f > e > d:
    print(f"el orden es {c},{b},{a} ")
elif f > d > e:
    print(f"el orden es {c},{a},{b}")



'''
Enunciado:r
Realice un programa que solicite por consola 3 palabras cuales quiera
Luego el programa debe consultar al usuario como quiere ordenar las palabras
1 - Ordenar por orden alfabético (usando el operador ">")
2 - Ordenar por cantidad de letras (longitud de la palabra (len) y operador ">")
Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
e imprimir en pantalla de la mayor a la menor
Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
e imprimir en pantalla de la mayor a la menor
IMPORTANTE: Para ordenar las palabras deben realizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido.
'''

print('Ejercicios de práctica con cadenas')
# Empezar aquí la resolución del ejercicio