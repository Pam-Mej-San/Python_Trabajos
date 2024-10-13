#
#• Objetivo: Practicar con las funciones matemáticas básicas del
#módulo math.
#• Descripción: Utiliza las funciones del módulo math para realizar
##operaciones matemáticas avanzadas.
#• Instrucciones: Solicita al usuario que ingrese un número
#decimal.
#Usa las siguientes funciones del módulo math para realizar diferentes
#cálculos:
#✓ math.ceil(): Redondear al entero superior.
#✓ math.floor(): Redondear al entero inferior.
#✓ math.sqrt(): Obtener la raíz cuadrada.
#✓ math.factorial(): Calcular el factorial (solo si es un
#número entero no negativo).
#✓ math.pow(): Elevar el número a la potencia de otro
#número.
#
#

import math

def operaciones_matemáticas():
    # Solicitar al usuario que ingrese un número decimal
    numero = float(input('Ingresa un número decimal: '))

    # Redondear al entero superior
    entero_superior = math.ceil(numero)
    print(f'Redondeo al entero superior: {entero_superior}')

    # Redondear al entero inferior
    entero_inferior = math.floor(numero)
    print(f'Redondeo al entero inferior: {entero_inferior}')

    # Obtener la raíz cuadrada
    if numero >= 0:
        raiz_cuadrada = math.sqrt(numero)
        print(f'Raíz cuadrada: {raiz_cuadrada}')
    else:
        print('No se puede calcular la raíz cuadrada de un número negativo.')

    # Calcular el factorial si es un número entero no negativo
    if entero_superior >= 0:
        factorial = math.factorial(entero_superior)
        print(f'Factorial de {entero_superior}: {factorial}')
    else:
        print('El número debe ser entero no negativo para calcular el factorial.')

    # Elevar a la potencia (elevando el número ingresado al cuadrado como ejemplo)
    potencia = math.pow(numero, 2)
    print(f'{numero} elevado al cuadrado: {potencia}')

# Llamar a la función
if __name__ == '__main__':
    operaciones_matemáticas()