# Los tres ejemplos de escritura (TXT)

# Modo con 'w': para sobreescribir un archivo
with open('modo_w.txt', 'w') as file:
    file.write('Este archivo fue sobreescrito por el modo \'w\' ')
    file.write('Todo el contenido previo fue eliminado')
print('Archivo \'modo_txt\' creado con éxito')

#Modo 'a': Agrega contenido al archivo ya existente
with open('modo_a.txt', 'a') as file:
    file.write('Este archivo se le agregó el final con el modo \'a\' ')
    file.write('Todo el contenido previo no fue eliminado')
print('Archivo \'modo_txt\' modificado con éxito')

#Modo 'x': Agrega contenido al archivo ya existente

with open('modo_x.txt', 'x') as file:
    file.write('Este archivo fue creado con éxito usando la \'x\' ')
    file.write('Falla si ya no existe el archivo')
print('Archivo \'modo_txt\' creado con éxito')

