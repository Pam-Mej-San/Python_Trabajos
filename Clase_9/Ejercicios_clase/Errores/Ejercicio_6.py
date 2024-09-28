#Crea un programa que solicite al usuario que ingrese un número. Si el
#usuario ingresa algo que no es un número, muestra un mensaje de error
#usando try/except.

try:
    numerito=int(input('Dame un numerito:'))
    print(f'El numerito que ingresaste es: {numerito}')

except ValueError:
    print('Este no es un numerito válido')
