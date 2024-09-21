#Ejercicio con range, enumerate, y break/continue
#Escribe un programa que:
#1. Itere sobre una lista de cadenas usando enumerate para mostrar el
#índice y el valor.
#2. Utilice continue para saltar cadenas vacías.
#3. Utilice break para detener la iteración si se encuentra una cadena
#con más de 5 caracteres.
#
# Lista de cadenas para probar
cadenas = ['Hola', 'labor', 'Olalá', 'Programación', 'Latinoamerica', 'Power']

for indice, cadena in enumerate(cadenas):
    if cadena == '':
        continue

    if len(cadena) > 5:
        print(f'Cadena con más de 5 caracteres encontrada: {cadena}. Fin del ciclo')
        break
    print(f'Índice: {indice}, Valor: {cadena} \n')
