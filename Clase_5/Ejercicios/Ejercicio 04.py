#Crea una lista de diccionarios, 
#donde cada diccionario representa un
#estudiante con las siguientes claves:
# Nombre
# Edad
# Calificaciones (que es una lista de números)
# 2. Imprime el nombre y las calificaciones del 
# primer estudiante en la lista

Estudiantes= [
     {
    'Nombre': 'Coryn Hyuk',
    'Edad': 32,
    'Calificaciones': [99,88,100]
    },
     {
    'Nombre': 'Daniela Chavez',
    'Edad': 30,
    'Calificaciones': [90,100,100]
    },
    {
    'Nombre': 'Hiruki Yamada',
    'Edad': 28,
    'Calificaciones': [89,90,95]
    }
]

Alumno_1= Estudiantes[0]
print ('\n Nombre de primer estudiante:', Alumno_1 ['Nombre'])
print ('\n Calificaciones de primer estudiante:', Alumno_1 ['Calificaciones'],'\n' )

