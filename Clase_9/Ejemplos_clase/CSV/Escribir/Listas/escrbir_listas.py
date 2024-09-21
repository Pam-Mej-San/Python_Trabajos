import csv

#definimos los nombres de las columnas
fieldnames= ['Nombre','Edad', 'Ciudad']

#newline='' se utiliza para evitar lineas en blanco adicionales
#para algunos sistemas operativos.
with open('archivo.csv', 'w', newline='') as file:
    #creamos un objeto DictWriter
    #Se pasa el archivo y la lista de nombres de columnas (fieldnames)
    writer= csv.DictWriter(file, fieldnames=fieldnames)

    #escribir la fila de encabezados en el archivo csv
    #esto crea la primera fila con los nombres de las columnas
    writer.writeheader()

    #escribir una fila con los datos de un archivo csv
    #cada diccionario debe tener claves que coincidan con los nombres de las oclumnas
    writer.writerow({'Nombre':'Ana', 'Edad': '35', 'Ciudad': 'Buenos Aires'}) 

    #Escribir multiples filas de datos en el archivo csv
    writer.writerows ([
            {'Nombre':'Joel', 'Edad': '38', 'Ciudad': 'Oslo'},
            {'Nombre':'Alissa', 'Edad': '25', 'Ciudad': 'Vancouver'}
    ])