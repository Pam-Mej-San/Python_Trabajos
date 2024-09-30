#
#Crea una clase Habitacion con atributos como numero, tipo, y
#precio. Luego, crea una clase Hotel que contenga una lista de
#habitaciones y métodos para reservar, cancelar y mostrar
#habitaciones disponibles
#

# Creación de clase Habitación
class Habitación:
    def __init__(self, numero, tipo, precio):
        self.numero = numero  # Atributo
        self.tipo = tipo      # Atributo
        self.precio = precio  # Atributo
        self.disponible = True # Atributo que nos indica si la habitación está disponible

    def __str__(self):
        return f'Habitación {self.numero}: Tipo: {self.tipo}, Precio: {self.precio}, Disponible: {self.disponible}'

# Clase Hotel
class Hotel:
    def __init__(self):
        self.habitaciones = []  # Una lista vacía para meter habitaciones
    
    def nueva_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)  # Función para agregar habitación

    def habitaciones_disponibles(self):
        disponibles = []  # Lista vacía para agregar habitaciones disponibles

        for hab in self.habitaciones:  # Revisa las habitaciones en la lista
            if hab.disponible: 
                disponibles.append(str(hab))  # Agregamos una cadena

        if len(disponibles) == 0:  # Identifica si está vacía o no
            return 'No hay habitaciones disponibles por el momento'
        
        return disponibles
    
    # Método para reservación
    def reservar(self, num_habit):
        for hab in self.habitaciones:  # Bucle para las habitaciones
            if hab.numero == num_habit:  # Verificamos si la habitación coincide
                if hab.disponible:  # Revisamos si la habitación está disponible
                    hab.disponible = False  # Marcarla como no disponible
                    return f'Tu habitación {num_habit} ya está reservada.'  # Mensaje de reservación
                else:  # En caso contrario...
                    return f'Habitación {num_habit} ya no está disponible.'  # No se puede reservar

        return f'Habitación {num_habit} no encontrada.'  # Si no se encuentra la habitación

    # Método para la cancelación
    def cancelar_reserva(self, num_habit):
        for hab in self.habitaciones:
            if hab.numero == num_habit:  # Verificamos si la habitación coincide
                if not hab.disponible:  # Verificamos si la habitación está reservada
                    hab.disponible = True  # Marcarla como disponible
                    return f'Tu reserva de la habitación {num_habit} ha sido cancelada.'  # Mensaje de cancelación
                else:  # En caso contrario...
                    return f'Habitación {num_habit} no está reservada.'  # No hay reserva para cancelar
        
        return f'Habitación {num_habit} no se encuentra en el sistema.'  # Si no se encuentra la habitación

# Crear instancias para las habitaciones
habit1 = Habitación(140, 'Doble', 2000)
habit2 = Habitación(141, 'Suite', 5000)
habit3 = Habitación(142, 'Normal', 1000)

# Instancia del hotel
hotel = Hotel()

# Agregar nuevas habitaciones
hotel.nueva_habitacion(habit1)
hotel.nueva_habitacion(habit2)
hotel.nueva_habitacion(habit3)

print('-'*40)

# Mostrar habitaciones disponibles
print(hotel.habitaciones_disponibles())
print('-'*40)

# Reservar una habitación
print(hotel.reservar(141))  #  apartamos esta

print('-'*40)

# Mostrar habitaciones disponibles después de la reserva
print(hotel.habitaciones_disponibles()) 

print('-'*40)

# Cancelar la reserva
print(hotel.cancelar_reserva(140))

print('-'*40)

# Mostrar habitaciones disponibles después de cancelar la reserva
print(hotel.habitaciones_disponibles())

print('-'*40)

