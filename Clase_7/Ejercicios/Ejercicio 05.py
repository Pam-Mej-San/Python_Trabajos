# Lista de nombres 
nombres = ['Santiago', 'Pedrito Pascal', 'Carlitos Pickles', 'Luis Miguel', 'Martin Martinez', 'María José', 'Juan el Bautista']

for indice, nombre in enumerate(nombres):
    # Mostrar el índice y el nombre
    print(f"Índice: {indice}, Nombre: {nombre}")

    if nombre[0] == 'A':
        continue

    if nombre == 'Carlitos Pickles':
        print("Nombre 'Carlitos Pickles' encontrado. Terminando la iteración.")
        break
