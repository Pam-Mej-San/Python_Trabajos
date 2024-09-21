#Ejemplo 1 - Función de args
  #  ""
   # Ésta función acepta un número variable de argumentos numéricos y retrona su suma.
    #:para args:  Un número variable de argumentos numéricos.
    #:return: La suma de los argumentos
    #""


def sumar_numeros(*args):
    total= 0 
    for numero in args:
        total+=numero
    return total
print('Ejemplo 1- Función que usa args:')
print(f'Suma de 1,2,3: {sumar_numeros(1,2,3)}')
print(f'Suma de4,5,6,7,8: {sumar_numeros(4,5,6,7,8)}')
print()

#Ejemplo 2 -Función que usa *KWARGS
def mostrar_detalles(**kwargs):
    for clave,valor in kwargs.items():
        print(f'{clave}.{valor}')

print('Ejemplo 2- Función que usa KWARGS')
mostrar_detalles(Nombre=':Ana', Edad=30, Ciudad=':Madrid''\n')

#Ejemplo 3 - COmbinados
def mostrar_info_completa(*args,**kwargs):
    print('Argumentos no nombrados:')
    for arg in args:
        print(args)
    print('\nArgumentos nombrados')
    for clave , valor in kwargs.items():
        print(f'{clave}: {valor}')
print('Ejemplo 3 - combinados')
mostrar_info_completa(1,2,3, Nombre='Ana', Edad=30, Ciudad='Madrid')