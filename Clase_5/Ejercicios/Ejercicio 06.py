#1. Crea un diccionario que contenga información sobre una escuela. La
#escuela tiene:
#o Nombre
#o Año de fundación
#o Lista de clases, donde cada clase es un diccionario con:
#▪ Nombre de la clase
#▪ Lista de estudiantes, donde cada estudiante es un diccionario con:
#▪ Nombre
#▪ Edad
#2. Imprime el nombre del primer estudiante de la primera clase.
#Datos de escuela
escuela = {
    'Nombre': 'Lewis',
    'Año': 2010,
    'Materias': [
        {
            'Materia': 'Literatura',
            'Alumnos': [
                {'Alumno': 'Anaís', 'Edad': 19},
                {'Alumno': 'Andrés', 'Edad': 22},
                {'Alumno': 'Mateo', 'Edad': 20}
            ]
        },
        {
            'Materia':'Física',
            'Alumnos': [
                {'Alumno': 'Bernard', 'Edad': 20},
                {'Alumno': 'Bianca', 'Edad': 21},
                {'Alumno': 'Benjamín', 'Edad': 18}
            ]
        },
        {
            'Materia':'Idioma',
            'Alumnos': [
                {'Alumno': 'Clive', 'Edad': 21},
                {'Alumno': 'Coraline', 'Edad': 20},
                {'Alumno': 'Casiodoro', 'Edad': 22}
            ]
        }
    ]
}
primer_estudiante=escuela ['Materias'][0]['Alumnos'][0]['Alumno']
print('El primer alumno de la primera clase es:', primer_estudiante)