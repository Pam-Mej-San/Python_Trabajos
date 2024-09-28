#Escribe un programa que verifique si el archivo archivo_para_eliminar.txt
#existe. Si existe, elimínalo; si no, muestra un mensaje diciendo que no
#existe.
#

import os

archivito= 'Archivo_eliminado.txt'

if os.path.exists(archivito):
    os.remove(archivito)
    print(f'Archivo''{archivito} '' ha sido eliminado')
else:
    print(f'El archivo {archivito} ya valió')

