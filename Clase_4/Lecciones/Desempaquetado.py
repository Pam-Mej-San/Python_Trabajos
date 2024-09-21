#Ejemplo Básico de Tuplas
#Crear una tupla con varios datos

mi_tupla=(1, 'Python', 3.14)

#Desempaquetar la tupla en tres variables
numero, lenguaje, pi = mi_tupla

#Mostrar el valor de cada variable después del desempaquetado

print('Número:', numero)  #Imprime el Número 1
print('Lenguaje:', lenguaje) #Imprime el Lenguaje
print('Valor de pi:', pi) #Imprime el valor de Pi

#Explicación: Aquí, cada valor en la tupla se  asigna a una variable correpsondiente
#El primer valor de la tupla (1) se asigna a 'número'
#El segundo valor ('Python') se asigna a la 'Lenguaje'
#El tercer valor (3.14) se asigna a 'pi'

#Ejemplo 2: Cuando el Número de Variables no Coincide con el Número de elementos
# Crear una tupla con 3 elementos

mi_tupla=(1,'Python', 3.14) 

#Intentar desempaquetar en dos variables (resultará en error)
# número, Lenguaje= mi_tupla #Esto causará un ValueError: too many values to unpack (expected 2)
#Explicación: Como hay tres elementos en la tupla y solo dos variables, Python generará un error
#La cantidad de variables debe coincidir con la cantidad de elementos en la tupla

# Ejemplo 3: Desempaquetado con el Operador
#Crear una tupla con varios elementos
mi_tupla=(1,'Python',3.14, 'Tuplas', 'Desempaquetado')

#Desmpaquetar la tupla con el operador * para capturar varios elementos 
primer_elemento,*resto= mi_tupla

#Mostrar los resultados del desempaquetado

print('\n Pimer elemento:', primer_elemento) #Imprime: Primer elemento:1
print('Resto de los elementos:', resto)

#Imprime: Resto de los elementos ['Python' 3.14, 'Tuplas', 'Desempaquetado']
#Explicación: Aquí, el primer valor de la tupla (1), se asigna a 'primer_elemento'
#El resto de los valores se capturan en la lista 'resto' utilizando el operador '*'
#Esto permite manejar un número variable de elementos en la tupla


