#Leer un archivo TXT
#Crea un programa en Python que lea el contenido de un archivo
#mi_archivo.txt y muestre cada línea en la consola. El archivo tiene varias
#líneas de texto. Usa el método que prefieras para leer el archivo.

#leer

with open('mi_archivo.txt', 'r') as file:
    print('Así se lee un archivo txt: ')
    lineas=file.readlines()

for line in lineas:
    print(line.strip())
    print('-'*40)

