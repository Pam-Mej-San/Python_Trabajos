# Definicmos una función: parámetros posicionales
# Con Nombre y predeterminados

def presentar_persona (Nombre, edad, ciudad='Desconocida', profesión= 'Desconocida'):
    print(f'Nombre : {Nombre}')
    print(f'Edad: {edad}')
    print(f'Ciudad : {ciudad}')
    print(f'Profesión : {profesión}')
    print()

# Ejemplos de llamadas a la función

#Usando argumentos posicionales

print('Ejemplo con argumentos posicionales:')
presentar_persona('Ana',30)

#Usando argumentos posicionales y con nombre
#Como veremos se pisan los datos
print('Ejemplo con argumentos posicionales y con nombre:')
presentar_persona('Luis', 25, ciudad='Madrid', profesión='Ingeniero')

#Usando todos los argumentos con nombre
print('Ejemplo con argumentos con nombre:')
presentar_persona(Nombre='Marta', edad=34, ciudad='Madrid', profesión='Ingeniera')



