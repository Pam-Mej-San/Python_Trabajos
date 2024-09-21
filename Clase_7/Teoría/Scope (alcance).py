#Scope: Alcance local y global en python
#Crear una variable global

x= 20
def funcion_local():
    x=10 #x es una variable local
    print(f'Valor de x dentro de la función local:{x}\n')

def funcion_global():
    #global x #Para modificar la variable global
    x=30
    print(f'Valor de x dentro de la función global: {x}\n')

funcion_local()
funcion_global()

print(f'Valor de x fuera de la función {x}\n')
