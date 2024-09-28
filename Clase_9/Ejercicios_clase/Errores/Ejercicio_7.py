#Crea un programa que pida al usuario ingresar su edad. Usa assert para
#verificar que la edad ingresada es mayor o igual a 18. Si no es así,
#muestra un mensaje de error.

dame_edad= int(input('Dame tu edad:'))
assert dame_edad>=18, 'Debes ser mayor de 18 para estar aquí'
print(f'Edad ingresada: {dame_edad}, sí puedes estar aquí')

