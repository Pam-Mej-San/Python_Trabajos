#Crea un programa que abra un archivo notas.txt, lea su contenido, y lo
#muestre en la consola. Usa el bloque with para asegurarte de que el
#archivo se cierra automáticamente.

#Crear archivo
with open ('notas.txt', 'w') as file:
    content =file.write('\nAquí comenzó todo\n')
    print('-'*12)
print(content)

#Añadir contenido

with open ('notas.txt','a') as file:
    content= file.write ('\n Esta linea se añadió con add \n')

#Leer archivo
with open ('notas.txt', 'r') as file:
    content =file.read()
print(content)


