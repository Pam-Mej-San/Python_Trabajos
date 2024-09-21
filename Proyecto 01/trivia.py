
#Bienvenida

import random

preguntas = [
    {
        "pregunta": "¿Qué palabra clave se usa para definir una función en Python?",
        "opciones": 
        ("a) def", "b) function", "c) func", "d) define"),
        "respuesta_correcta": "a"
    },
    {
        "pregunta": "¿Cómo se llama el tipo de datos que almacena una secuencia de caracteres?",
        "opciones": 
        ("a) list", "b) tuple", "c) str", "d) dict"),
        "respuesta_correcta": "c"
    },
    {
        "pregunta": "¿Qué operador se usa para la comparación de igualdad en Python?",
        "opciones": 
        ("a) =", "b) ==", "c) ===", "d) =="),
        "respuesta_correcta": "b"
    },
    {
        "pregunta": "¿Cómo se importa un módulo en Python?",
        "opciones": 
        ("a) include", "b) require", "c) import", "d) load"),
        "respuesta_correcta": "c"
    },
    {
        "pregunta": "¿Qué palabra clave se usa para definir una función en Python?",
        "opciones": 
        ("a) def", "b) function", "c) func", "d) define"),
        "respuesta_correcta": "a"
    },
    {
        "pregunta": "¿Qué palabra clave se usa para definir una función en Python?",
        "opciones": 
        ("a) def", "b) function", "c) func", "d) define"),
        "respuesta_correcta": "a"
    },
    {
        "pregunta": "¿Qué palabra clave se usa para definir una función en Python?",
        "opciones": 
        ("a) def", "b) function", "c) func", "d) define"),
        "respuesta_correcta": "a"
    },
    {
        "pregunta": "¿Qué palabra clave se usa para definir una función en Python?",
        "opciones": 
        ("a) def", "b) function", "c) func", "d) define"),
        "respuesta_correcta": "a"
    },
    {
        "pregunta": "¿Qué palabra clave se usa para definir una función en Python?",
        "opciones": 
        ("a) def", "b) function", "c) func", "d) define"),
        "respuesta_correcta": "a"
    },
    {
        "pregunta": "¿Qué palabra clave se usa para definir una función en Python?",
        "opciones": 
        ("a) def", "b) function", "c) func", "d) define"),
        "respuesta_correcta": "a"
    }
]

def bienvenida():
    print('¡Bienvenid@ al juego de trivias sobre Python!')
    bienvenida=print('¿Estas list@?')

def triviatime():
    puntuacion = 0
    error=0 
    total = len(preguntas)

    for pregunta in preguntas: 
        muestra_pregunta(pregunta) 
        respuesta = obtener_respuesta()
        if respuesta == pregunta['respuesta_correcta']: 
            print('¡Correcto!')
            puntuacion = puntuacion + 1
        else:
            print('Incorrecto')
            error=error+1
            if error == 3:
                break
    print(f'\nTu puntuación final es {puntuacion} de {total}.')

def muestra_pregunta(pregunta):
    print(pregunta['pregunta'])
    for opcion in pregunta['opciones']:
        print(opcion)

def obtener_respuesta():
    respuesta = input('Tu respuesta (a, b, c, d): ')
    return respuesta.strip().lower()

#Hace que las preguntas se alternen
random.shuffle(preguntas)

nombre= (input('Primero necesitamos tu Nombre:'))
edad=int(input('Ahora necesitamos tu Edad:'))
if edad < 18:
    print(f'Lo siento, {nombre}, solo podrás jugar hasta que tengas 18 :(, ¡Cuídate!')
else:
    bienvenida()
    triviatime()

