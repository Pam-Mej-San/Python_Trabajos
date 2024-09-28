#Crea un programa que guarde los siguientes datos en un archivo CSV
#alumnos.csv: ["Nombre", "Edad"], ["Ana", 23], ["Luis", 25]

import csv

with open ('datos.csv', 'w', newline='') as file:
    escribiendo= csv.writer(file)
    escribiendo.writerow(['Nombre', 'Edad'])
    escribiendo.writerow(['Ana', '23'])
    escribiendo.writerow(['Luis', '25'])

print('Tus datos han sido modificados')
    