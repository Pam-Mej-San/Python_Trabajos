# Contar Ocurrencias de Elementos en un Diccionario Anidado
# 1. Crea un diccionario que contenga información sobre tres clubes deportivos, cada uno con una lista de jugadores
# Cada jugador es un diccionario con las claves: nombre y edad.
# 2. Cuenta cuántos jugadores en total tienen cada uno de los clubes

clube= [
    { 'Club A': 'Jitomates',
        'Jugadores':{'Roberto': 20,
                       'Clarisa': 19, 
                       'Gertrude':22,
                       'Lauren': 24}
    },
     { 'Club B': 'Warriors',
        'Jugadores': {'Marcos': 30, 
                        'María': 25,
                        'Jerob':24}},
     {'Club C': 'Omega',
        'Jugadores': {'Sara': 28, 
                       'Matusalén':101,
                       'Ichabod':42,
                       'Corazón':32} },
]

Lista_1= len(clube[0]['Jugadores'])
Lista_2= len(clube[1]['Jugadores'])
Lista_3= len(clube[2]['Jugadores'])


print(f'\n{clube[0]["Club A"]} tiene {Lista_1} jugadores.')
print(f'\n{clube[1]["Club B"]} tiene {Lista_2} jugadores.')
print(f'\n{clube[2]["Club C"]} tiene {Lista_3} jugadores.\n')
