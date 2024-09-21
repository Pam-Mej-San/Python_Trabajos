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
        print("Despues de tres intentos, el juego terminará")
    
    #Inicializar variables del juego
vidas = 3
puntuacion = 0


preguntas = {
        0: {'pregunta': '¿Cuál es la capital de Francia?',
            'opciones': ['París', 'Londres', 'Berlín', 'Madrid'],
            'respuesta_correcta': 'París'
        },
        1: {'pregunta':'¿Qué es el ADN?',
            'opciones': ['Ácido ', 'Ácido ribonucleico', 'Proteína', 'Carbohidrato'],
            'respuesta_correcta': 'Ácido '
        },
        2: {
            'pregunta':'¿En qué año se descubrió América?',
            'opciones': ['1492', '1500', '1607', '1620'],
            'respuesta_correcta': '1492'
        },
        3:{
            'pregunta': '¿Cuál es el océano más grande del mundo?',
            'opciones': ['Océano Pacífico', 'Océano Atlántico', 'Océano Índico', 'Océano Ártico'],
            'respuesta_correcta': 'Océano Pacífico'
        
        }

    }




#Mezclar las preguntas
indices= list(preguntas.keys())
random.shuffle(indices)

# Ciclo para mostrar preguntas y evaluar respuestas
for idx in preguntas:
        if vidas <=0:
         break
pregunta_info=preguntas[idx]
pregunta = pregunta_info['preguntas']
opciones= pregunta_info['opciones']
respuesta_correcta = pregunta_info['respuesta_correcta']

print('\n Pregunta',pregunta)
for i, opcion in enumerate(opciones,1):
    print(f'{i}.{opcion}')

#Obtener respuesta del usuario y validar
respuesta_usuario= (input('Elige el número de tu respuesta'))
        
if respuesta_usuario.isdigit():
    respuesta_usuario=int(respuesta_usuario)-1
    if 0<= respuesta_usuario < len(opciones):
        if opciones[respuesta_usuario].strip().capitalize()== respuesta_correcta:
            print('¡Así es!')
            puntuacion+=1
        else: 
            print('Incorrecto')
            vidas-=1
            print(f'Te quedan {vidas} vidas')
    else:
        print('Nope. Te quitaremos otra vida')
        vidas -=1
        print(f'Te quedan {vidas} vidas')
else: 
    print('No es válido. Te quitaremos otra vida')
    vidas-=1
    print(f'Te quedan {vidas} vidas')



# Mensaje final
mensaje_final() 
print(f'Tu puntuación final es: {puntuacion}')

# Ejecutar el juego
if __name__ == "__main__":
    jugar()