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

temperatura_1 = int(input('Ingrese temperatura 1:'))
temperatura_2 = int(input('Ingrese temperatura 2:'))
temperatura_3 = int(input('Ingrese temperatura 3:'))

if temperatura_1 > temperatura_2 and temperatura_3:
    print('{} Es la temperatura maxima'.format(temperatura_1))
elif temperatura_2 > temperatura_1 and temperatura_3:
    print('{} Es la temperatura maxima'.format(temperatura_2))
else:
    print('{} Es la temperatura maxima'.format(temperatura_3))

if temperatura_1 < temperatura_2 and temperatura_3:
    print('{} Es la temperatura minima'.format(temperatura_1))
elif temperatura_2 < temperatura_1 and temperatura_3:
    print('{} Es la temperatura minima'.format(temperatura_2))
else:
    print('{} Es la temperatura minima'.format(temperatura_3))

Suma = temperatura_1 + temperatura_2 + temperatura_3
promedio = Suma / 3
print('El promedio es: {}'.format(promedio))


