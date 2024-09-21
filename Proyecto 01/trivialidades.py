import random


# Lista de preguntas y respuestas en formato de tuplas
# Crear índice


questions_and_answers = [
    ["¿Cuál es la capital de Francia?", "París"],
    ["¿Cuál es el océano más grande del mundo?", "Océano Pacífico"],
    ["¿En qué año llegó el hombre a la luna?", "1969"],
    ["¿Cuál es el planeta más cercano al sol?", "Mercurio"],
    ["¿Quién escribió 'Cien años de soledad'?", "Gabriel García Márquez"]
]

indice=[
    


]

def get_user_info():
    """Obtiene el nombre y la edad del usuario y verifica si es mayor de edad."""
    name = input("¿Cuál es tu nombre? ")
    age = int(input("¿Cuántos años tienes? "))
    
    if age < 18:
        print("Lo siento, debes ser mayor de edad para jugar este juego.")
        return None, None
    
    return name, age

def play_trivia_game(user_name):
    """Ejecuta el juego de trivia."""
    score = 0
    num_questions = len(questions_and_answers)
    
# Barajar las preguntas
    random.shuffle(questions_and_answers)
    
    for question, correct_answer in questions_and_answers:
        print("\n" + question)
        user_answer = input("Tu respuesta: ").strip()
        
        if user_answer.lower() == correct_answer.lower():
            print("¡Correcto!")
            score += 1
        else:
            print(f"Incorrecto. La respuesta correcta es: {correct_answer}")
    
    print(f"\nGracias por jugar, {user_name}! Tu puntuación final es: {score} de {num_questions}")

def main():
    """Función principal del juego."""
    user_name, user_age = get_user_info()
    
    if user_name and user_age:
        play_trivia_game(user_name)

if __name__ == "__main__":
    main()
