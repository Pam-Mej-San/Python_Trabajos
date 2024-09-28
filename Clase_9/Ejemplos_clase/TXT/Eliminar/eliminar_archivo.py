import os #importamos módulo 'os' para interactuar con el sistema operativo

#definimos el nombre del archivo que se quiere eliminar
nombre_archivo= 'archivo.txt'

#comprobar si el archivo existe en la ruta especificada
#La función if os.path.exists(nombre_archivo)
#devuelve True en caso de que el arvhico existe y
#False en caso contrario
if os.path.exists(nombre_archivo):
    #Si el archivo existe procederá a eliminarlo
    #y la función os.remove () elimina el archivo
    #en la ruta específica
    os.remove(nombre_archivo)
    print(f'Archivo',{nombre_archivo},'eliminado')
else:
 #si el archivo no existe informar al usuario
 #informar al usuario
    print(f'El Archivo',{nombre_archivo}, 'no existe')


