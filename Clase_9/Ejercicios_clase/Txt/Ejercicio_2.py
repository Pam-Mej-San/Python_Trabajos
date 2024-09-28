#
#Crea un programa que escriba un texto en un archivo nuevo_archivo.txt. Si
#el archivo ya existe, debe sobrescribir su contenido.
#

with open ('nuevo_archivo.txt','w') as file:
    file.write('¿Ves que si se puede?')
    file.write('acabas de sumar otra línea')


with open ('mi_archivo.txt','a') as file:
    file.write('\n¿Ves que si se puede?\n')
    file.write('acabas de sumar otra línea\n')