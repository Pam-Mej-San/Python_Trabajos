import random

# Función para mostrar un mensaje final
def mensaje_final():
    print("Lo has hecho muy bien, intenta de nuevo")

#🎮Función principal del juego
def jugar():
    # Datos del jugador
    nombre = input("Introduce tu nombre: ").capitalize()
    edad = int(input("Introduce tu edad: "))

    #🤔Verificar que el jugador tiene más de 18 años
    if edad < 18:
        print("Lo siento, debes tener más de 18 años para jugar.")
        return
    else:
        print("*** BIENVENIDO AL JUEGO DE TRIVIA DE PYTHON 🐍***")
        print(f"¡Hola {nombre}! Este es un juego de trivia. Es decir, que deberas responder y elegir la opcion correcta para sumar puntos. ¡Diviertete!") 
        print("Despues de tres intentos, el juego terminara")
    
    #Inicializar variables del juego
    vidas = 3
    puntuacion = 0

    # Preguntas y respuestas
    #debemos intentar hacer un diccionario o una lista de lista con varias opciones de respuesta
    #🔴intentar hacer preguntas con opciones de respuesta
    preguntas = [
        ("¿Cuál es la capital de Francia?", "París"),
        ("¿Qué es el ADN?", "Ácido desoxirribonucleico"),
        ("¿En qué año se descubrió América?", 1492),
        ("¿Cuál es el océano más grande del mundo?", "Océano Pacífico"),
        ("¿Quién escribió 'Cien años de soledad'?", "Gabriel García Márquez")
    ]
    
    #💡crear un indice [[]]
    
    #preguntas y respuestas
    
    #preguntas [1,2,3]
    #respuesta [1,2,3] 
    #la pregunta en el indice 1 debe coincider con la que respuesta en el indice 1 : Generar esta logica en una sola funcion

    # 🌀Mezclar las preguntas
    random.shuffle(preguntas)

    # Ciclo para mostrar preguntas y evaluar respuestas
    for pregunta, respuesta_correcta in preguntas: #esta parte tendria que modificarse
        #si se hace una lista de lista hay que modificar la logica del ciclo for usando los indices
        if vidas <= 0:
            break

        print("\nPregunta:", pregunta)
        respuesta_usuario = input("Tu respuesta: ").strip()

        if respuesta_usuario.lower() == respuesta_correcta.capitalize():
            print("¡Respuesta correcta!")
            puntuacion += 1
        else:
            print("Respuesta incorrecta.")
            vidas -= 1
            print(f"Te quedan {vidas} vidas.")

    # Mensaje final
    mensaje_final() 
# Ejecutar el juego
if __name__ == "__main__":
    jugar()
