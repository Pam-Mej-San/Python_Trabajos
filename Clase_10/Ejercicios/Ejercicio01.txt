# Estudiantes

#Hacemos la clase de Estudiantes para ver si aprobaron o no y cada aspecto con sus atributos necesarios
class Estudiante: 
    def __init__(self, nombre, edad, notas): 
        self.nombre = nombre #atributo de instancia
        self.edad = edad  #atributo de instancia
        self.notas = notas  #atributo de instancia

#Pero necesitamos ver sus promedios
    def promedio(self):
        if not self.notas:  # Verificamos si la lista de notas está vacía o ya tiene información
            return 0 #Aquí se le asigna cero de plano para que se tenga información, pero necesitamos una 
                    #función o algo para que la llame otra vez y la pueda leer en la información que le demos
                    #más adelante (info**)
        
        suma = sum(self.notas)  # Suma todas las notas de una sola vez
        return suma / len(self.notas)  # Calcula y retorna el promedio a lo que pusimos anteriormente

    def aprobado(self): #función para calificaciones que agreguemos a una lista de numeros (la info**)
        return self.promedio() >= 6.0  # Verifica si ha aprobado (osea si es más de 6 o no) [con lógica-matemática]

#Otra clase llamada 'Curso' para agregar estudiantes a la Clase 'Estudiantes'
class Curso:
    def __init__(self,nombres):
        self.nombres=nombres #se llama a los atributos que definamos como nombres en nuestros datos mas adelante
        self.estudiantes=[] #Aquí se hace el espacio para que los estudiantes de la clase Estudiantes
                            #pueda agregarse como una lista vacía
    
    def agregación(self,estudiante): #Aquí se agregan los atributos de la clase Estudiante 
        self.estudiantes.append(estudiante) #intentamos con la función append().

    def aprobados(self): #Con esto vamos a mencionar a los aprobados 
        print(f'\nEstudiantes aprobados en {self.nombres}:\n') #primero con un print
        for estudiante in self.estudiantes: # esto hace que el bucle recorra todo con el nombre de los estudiantes que pogamos más adelante
         if estudiante.aprobado(): #llama a la función de 'aprobado' para ver si pasa
            promedio=estudiante.promedio() #Aquí calcula
            print(f'{estudiante.nombre}, Edad: {estudiante.edad}, Promedio {promedio:0}\n') #finalmente se imprime el asunto

curso=Curso('Curso de Español') #instancia del curso

#Crear objetos para todo lo anterior
estudiante1=Estudiante ('Luis',17,[8,9,5]) 
estudiante2=Estudiante ('Pablo',20,[8,10,9])
estudiante3=Estudiante ('Osvaldo', 32, [5,7,8])


curso.agregación(estudiante1) #Agrega a Luis
curso.agregación(estudiante2) #Agrega a Pablo
curso.agregación(estudiante3) #Agrega a Osvaldo



curso.aprobados() # Muestra los estudiantes que ya aprobaron, si le pones otro 5 a Osvaldo, ya no lo muestra