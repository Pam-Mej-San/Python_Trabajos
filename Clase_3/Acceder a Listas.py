
mi_lista=['a','b','c','d','e']

#Acceso a Sublistas (Slicing) / Cortar pues...

print('Sublista (índice 1 a 3)', mi_lista[1:4])
print('Sublista (índice 3)', mi_lista[:3])
print('Sublista (índice 2 al final)', mi_lista[2:])

print('////////////////////////////////////////////////')

#Acceso con paso a Sublistas 

print('Sublista (índice a 2)', mi_lista[::2])
print('Sublista (índice 2 en rango)', mi_lista[1:4:2])


print('////////////////////////////////////////////////')

#Iteración a través de la lista 

print('Iteración a través de la lista:')

for elemento in mi_lista:
    print(elemento)

