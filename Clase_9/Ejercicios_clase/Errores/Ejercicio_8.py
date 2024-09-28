#Crea un programa que solicite el ingreso de un número entre 1 y 10. Si el
#número no está en ese rango, genera una excepción con raise.

numerito=int(input('Ingresa un numero que sea entre 1 y 10:'))

if numerito < 1 or numerito > 10:
    raise ValueError('El número debe estar entre 1 y 10')
else:
    print(f'El numero ingresado fue: {numerito}')

