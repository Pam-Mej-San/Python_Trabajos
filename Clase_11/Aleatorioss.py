#Generador de Números Aleatorios con el Módulo
#random
#• Objetivo: Trabajar con funciones de generación de números
#aleatorios del módulo random.
#• Descripción: Simula el lanzamiento de un dado y genera una
#lista de números aleatorios.
#• Instrucciones:
#✓ Simula el lanzamiento de un dado de 6 caras (números
#del 1 al 6) cinco veces.
#✓ Genera una lista de 10 números aleatorios entre 1 y 100.
#✓ Selecciona aleatoriamente un número de la lista
#generada.

import random

def simulador_dado_y_numeros_aleatorios():
    # Simular el lanzamiento de un dado de 6 caras cinco veces
    lanzamientos_dado = [random.randint(1, 6) for _ in range(5)]
    print('Resultados de los lanzamientos del dado:', lanzamientos_dado)

    # Generar una lista de 10 números aleatorios entre 1 y 100
    numeros_aleatorios = [random.randint(1, 100) for _ in range(10)]
    print('Lista de 10 números aleatorios entre 1 y 100:', numeros_aleatorios)

    # Seleccionar aleatoriamente un número de la lista de números aleatorios
    numero_seleccionado = random.choice(numeros_aleatorios)
    print('Número seleccionado aleatoriamente de la lista:', numero_seleccionado)

# Llamar a la función
if __name__ == '__main__':
    simulador_dado_y_numeros_aleatorios()
