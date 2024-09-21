#Ejemplo 01 del uso de return

def calcular_cuadrado(numero):
    return numero*numero
resultado=calcular_cuadrado(4)

print('Ejemplo básico de return:')
print(f'El cuadrado de 4 es:{resultado}\n')

#Ejemplo 02: Retorno de multiples valores

def obtener_datos():
    nombre= 'Ana'
    edad= 30
    return nombre, edad #Esto hará que retorne los valores ocmo tupla
#Asignamos los valores a una variable
nombre,edad=obtener_datos()
print('Ejemplo-2 Retorno de múltiples valores:')
print(f'Nombre: {nombre}, Edad: {edad}')
print()

#Ejemplo 3- Return con CONDICIONAL
def clasificar_numero(numero):
    if numero > 0:
        return 'Positivo'
    elif numero < 0:
        return 'Negativo'
    else:
        return 'Cero'
    
resultado_1=clasificar_numero(10)
resultado_2=clasificar_numero(-5)
resultado_3=clasificar_numero (0)


print('Ejemplo 3- Sin return:')
print(f'El número 10 es {resultado_1}')
print(f'El número -5 es {resultado_2}')
print(f'El número 0 es {resultado_3}')

#Ejemplo de SIN RETURN
def mostrar_mensaje():
    print('Esta función no retorna valor.')
resultado=mostrar_mensaje()
print('Ejemplo 4: Sin return')
print(f'Valor retornado {resultado} \n')
