#Desarrolla un programa que haga lo siguiente:
#1. Usar un bucle for con range para iterar sobre los números del 1 al 20.
#2. Usar continue para saltar los números divisibles por 3.
##3. Usar break para detener la iteración si se encuentra un número
#mayor que 15.
#4. Crear un set con los números restantes y verificar si algún número
#es par.

numeritos=[]
for numero in range(1, 21):
    if numero % 3 ==0:
        continue

    if numero > 15:
        break
    numeritos.append(numero)

numerosset=set(numeritos)
parpar = any(numero % 2 == 0 for numero in numeritos)

print("Números válidos:", numeritos)
print("Set de números válidos:", numerosset)
print("¿Hay algún numerito par en el set?", parpar)