#Ejemplo básico de un generador
#Generador que produce numeros del 1 al 5
#Definición del generador
#Palabra reservada para funciones: def

def contador ():
    #Itera sobre los números del 1 al 5
    for i in range (1,6): #itera sobre los números del 1 al 5 (no contempla el 6)
        yield i # #Produce el valor de i y pausa la ejecución

#Crear una instancia para el generador

gen= contador()# gen es un objeto generador

#Iterar sobre los valores producidos por el mismo generador
for numero in gen:
    print(numero) # Imprime cada uno de los números producido por e generador

#Ejemplo 2- Fibonacci
def fibonacci():
    a,b=0,1 #inicializa a los primeros dos números de la secuencia
    while True: #ciclo infinito para generar los números
        yield a #produce el valor de a y pausa la ejecución
        a,b = b,a + b #actualiza a y b para la siguiente iteración

gen= fibonacci () #gen es un objeto generador que produce números

#Obtener los primeros 10 números de fibonacci

for _ in range (10):
     print(next(gen)) #obtiene el siguiente numero en la secuencia
