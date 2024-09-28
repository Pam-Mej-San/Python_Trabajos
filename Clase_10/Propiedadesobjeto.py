# 2. Propiedades de un objeto

#Definir la clase persona

class Persona:
    def __init__ (self, nombre, edad):
        #inicializar las propiedades del objeto
        self.nombre=nombre #propiedad nombre
        self.edad=edad   #propiedad edad


#Crear un objeto de la clase persona

persona1= Persona('Ana', 30)
persona2= Persona ('Sofía', 21)

#Acceder a las propiedades del objeto

print(persona1.nombre)
print(persona1.edad)

#Acceder a las propiedades del segundo objeto

print(persona2.nombre)
print(persona2.edad)

#La clase persona describe un objeto que si tiene propiedades como nombre y edad
#Al instanciar persona1 con valores específicos se crean atributos únicos que 'representan'
#el estado de ese objeto
#Se puede acceder a esas propiedades utilizando la anotación de punto, lo que permite 
#obtener información sobre la instancia creada
