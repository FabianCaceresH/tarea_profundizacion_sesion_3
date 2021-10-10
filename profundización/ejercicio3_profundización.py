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

# Ejercicios de práctica con números
a = int(input("ingrese el primer numero:"))
b = int(input("ingrese el segundo numero:"))
c = int(input("ingrese el tercer numero:"))
if a > b and a > c:
    print(f"{a} es la temperatura maxima  ")
elif b > a and b > c:
    print(f"{b} es la temperatura maxima")
elif c > a and c > b:
    print(f"{c} es la temperatura maxima")
if a < b and a < c:
    print(f"{a} es la temperatura minima")
elif b < a and b < c:
    print(f"{b} es la temperatura minima")
elif c < a and c < b:
    print(f"{c} es la temperatura minima") 
if a > 0:
    d = (a+b+c)/3
    print(f"el promedio de las temperaturas es {d}")



'''
Enunciado:
Realice un programa que solicite ingresar tres valores de temperatura
De las temperaturas ingresadas por consola determinar:    
1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
3 - ¿Cuál es el promedio de las temperaturas ingresadas?
En cada caso imprimir en pantalla el resultado
IMPORTANTE: Para ordenar las temperatuas debe utilizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido. Recomendamos pensar bien este problema de lógica con un lápiz y papel.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio