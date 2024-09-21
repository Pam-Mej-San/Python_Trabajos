# Definir listas
# Lista vacía

lista_vacía=[]
print('Lista vacía:', lista_vacía)

# Lista de elementos iniciales

lista_iniciales=[1,2,3,4,5]
print('Lista de números:', lista_iniciales)

#Lista de cadenas

lista_cadenas=['manzana','banana', 'cereza']
print('Lista de cadenas:', lista_cadenas)

#Listas Mixta

lista_mix= [1, 'Pam', 'Maestra', 'Mayo', 96, {1,2,3,4}]

print('Lista mixta', lista_mix)

#Lista con elementos repetidos

lista_repeat=[0]*5

print('Lista de repetición:', lista_repeat)

#Lista a partir de otros iterables

cadena='hola'
lista_de_caracteres =list(cadena)

print('Lista a partir de otros iterables (cadena)', lista_de_caracteres)

cadena_2= 'Pamela'

lista_caracteres= list(cadena_2)

print('Lista a partir de otros iterables (cadena)', lista_caracteres)
