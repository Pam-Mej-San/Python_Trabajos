#Crear un diccionario
#1. Crea un diccionario que represente una base de datos de empleados
#de una empresa. El diccionario debe tener:
#o nombre_empresa
#o empleados, que es una lista de diccionarios, donde cada
#diccionario representa un empleado con:
#▪ id_empleado
#▪ nombre
#▪ departamento
#▪ salario
#2. Escribe una función que busque y actualice el salario de un
#empleado dado su id_empleado. La función debe:
#o Buscar el empleado por su id_empleado.
#o Actualizar el salario del empleado a un nuevo valor
#proporcionado.
#o Imprimir la información del eempleado después de la actualización.
#


diccionario={
    'NOMBRE DE EMPRESA':'Mexi',
    'Empleados':[
        { 'ID':3312,'Nombre': 'Hidalgo', 'Departamento':'Libros', 'Salario':15000},
        { 'ID':3313,'Nombre': 'Emiliano', 'Departamento':'Juguetes', 'Salario':15000},
        { 'ID':3312,'Nombre': 'Porfirio', 'Departamento':'Dictaduras', 'Salario':100000}]
}

print('\n',diccionario,'\n')

def actu_salario(id_nombre,nuevo_salario):
    empleado_encontrado=False
    for empleado in diccionario['Empleados']:
        if empleado ['id_empleado']== 'id_empleado':
            empleado['Salario']=nuevo_salario
            print('Info del Empleado actualizado:')
            print(f'ID:{empleado['id_empleado']}')
            print(f'Nombre:{empleado['Departamento']}')
            print(f'Departamento:{empleado['Departamento']}')
            empleado_encontrado= True,
    else:
        print('Empleado no se encuentra en esta base de datos')
    