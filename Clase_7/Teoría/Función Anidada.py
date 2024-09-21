#Ejemplo 1- básico función anidada
def funcion_externa(x):
    def función_interna(y):
        return y+10
    return función_interna(x) #Llamada a la función interna

#LLamada a la función externa
resultado= funcion_externa(5)
print(f'Resultado de la función_externa(5): {resultado}')

#Ejemplo 2- Closure

def crearmulti(factor):
    def multi (x):
        return x * factor
    return multi 

duplicar= crearmulti(2)
triplicar= crearmulti(3)

print(f'Duplicar 10: {duplicar(10)}')
print(f'Duplicar 10: {triplicar (10)}')


