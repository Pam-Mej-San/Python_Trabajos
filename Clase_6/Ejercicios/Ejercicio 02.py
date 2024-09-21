#Ejercicio de while y for
#Desarrolla un programa que haga lo siguiente:
#1. Usar un bucle while para pedir al usuario que ingrese números
#hasta que se ingrese el número 0.
#2. Usar un bucle for para calcular la suma de los números ingresados,excluyendo el 0.
#
print('Vamos a jugar con algunos números')
numeros=[]

while True:
    numero=int(input(f'Ingresa un número:'))
    if numero == 0:
        break
    else:
        numeros.append(numero)
    
suma=0

for num in numeros:
 suma+=num

print(f'La suma final de tus números es igual a: {suma}')
print('Hemos terminado')








