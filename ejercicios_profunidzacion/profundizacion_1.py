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
Realice un programa que solicite por consola 2 números
Calcule la diferencia entre ellos e informe por pantalla
si el resultado es positivo, negativo o cero.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

numero_1 = int(input('Indique un número:'))
numero_2 = int(input('Indique otro número:'))

if numero_1 > 0:
    print('{} es positivo'.format(numero_1))
elif numero_1 < 0:
    print('{} es negativo'.format(numero_1))
else:
    print('{} es igual a cero'.format(numero_1))

if numero_2 > 0:
    print('{} es positivo'.format(numero_2))
elif numero_2 < 0:
    print('{} es negativo'.format(numero_2))
else:
    print('{} es igual a cero'.format(numero_2))