# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Comparadores
# Ingrese dos palabras cualesquiera y realice las sigueintes
# comparaciones entre ellas
from cgitb import text
from contextlib import AbstractAsyncContextManager
from re import A


texto_1 = str(input('Ingrese la primera palabra:\n'))

texto_2 = str(input('Ingrese la segunda palabra:\n'))

# Compare cual de las dos palabras es mayor (alfabéticamente)
# Imprima en pantalla según corresponda

if texto_1 > texto_2:
    print('{} es mayor a {}'.format(texto_1,texto_2))
    #print(texto_1, 'es mayor a', texto_2.format(texto_1,texto_2))
else:
    print(texto_2, 'es mayor a', texto_1)

# Compare cual de las dos palabras tiene mayor
# cantidad de letras
# Imprima en pantalla según corresponda

if len(texto_1) > len(texto_2):
    print('{} tiene más letras que {}'.format(texto_1,texto_2))
else:
    print(texto_2, 'tiene más cantidad de letras')

# Verifique si la primera letra de la primera palabra
# es mayor a la primera letra de la segunda palabra
# Imprima en pantalla según corresponda

letra_texto_1 = texto_1[0]
letra_texto_2 = texto_2[0]

if letra_texto_1 > letra_texto_2:
    print('La primera letra de {} es mayor que {}'.format(texto_1,texto_2))
else:
    print('La primera letra de {} es mayor que {}'.format(texto_2,texto_1))

copia_texto_1 = texto_1  # Copia de la variable texto_1

# Verifique que copia_texto_1 es igual a texto_1
# Imprima en pantalla según corresponda

if texto_1 == copia_texto_1:
    print('{} es igual a {}'.format(texto_1,copia_texto_1))
else:
    print('{} no es igual a {}'.format(texto_1,copia_texto_1))

# Verifique que copia_texto_1 es distinta a texto_2
# Imprima en pantalla según corresponda

if copia_texto_1 != texto_2:
    print('{} es distinto a {}'.format(copia_texto_1,texto_2))
else:
    print('{} no es distinto a {}'.format(copia_texto_1,texto_2))
