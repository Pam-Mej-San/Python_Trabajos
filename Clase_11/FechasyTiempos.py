
#Fechas y Tiempos con el Módulo datetime
#• Objetivo: Trabajar con fechas y tiempos utilizando el módulo
#datetime.
#• Descripción: Calcula la edad de una persona y muestra la fecha
#actual en diferentes formatos.
#• Instrucciones:
#✓ Solicita al usuario su fecha de nacimiento en formato
#DD/MM/AAAA.
#✓ Calcula su edad.
#✓ Muestra la fecha actual en los siguientes formatos:
#Día-Mes-Año.
#Mes/Día/Año.
#Año/Mes/Día.
##

from datetime import datetime

def calcular_edad(fecha_nacimiento):
    # Calcula la edad a partir de la fecha de nacimiento
    hoy = datetime.now()
    edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return edad

def mostrar_fecha_actual():
    # Obtiene la fecha actual
    hoy = datetime.now()
    
    # Muestra la fecha en diferentes formatos
    formato_1 = hoy.strftime('%d-%m-%Y')  # Día-Mes-Año
    formato_2 = hoy.strftime('%m/%d/%Y')  # Mes/Día/Año
    formato_3 = hoy.strftime('%Y/%m/%d')  # Año/Mes/Día
    
    print(f'Fecha actual en formato Día-Mes-Año: {formato_1}')
    print(f'Fecha actual en formato Mes/Día/Año: {formato_2}')
    print(f'Fecha actual en formato Año/Mes/Día: {formato_3}')

def main():
    # Solicitar al usuario su fecha de nacimiento
    fecha_nacimiento_str = input('Ingresa tu fecha de nacimiento (DD/MM/AAAA): ')
    
    # Convertir la cadena ingresada en un objeto datetime
    try:
        fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, '%d/%m/%Y')
        edad = calcular_edad(fecha_nacimiento)
        print(f'Tu edad es: {edad} años')
        
        # Mostrar la fecha actual en diferentes formatos
        mostrar_fecha_actual()
    except ValueError:
        print('El formato de la fecha es incorrecto. Asegúrate de usar DD/MM/AAAA.')

# Ejecutar el programa
if __name__ == '__main__':
    main()
