# Crear un diccionario

persona= {
  'nombre': 'Verónica',
  'edad': 25,
  'ciudad': 'Buenos Aires'
}
#Usar el método.get() para acceder a los elementos

nombre= persona.get('nombre')
edad= persona.get('edad')
ciudad=persona.get('ciudad')

#Imprimir

print('Nombre:', nombre)
print('Edad:', edad)
print('Ciudad', ciudad)

#intentar acceder a un clave que no existe usando.get

pais=persona.get('pais')
print('País:', pais) #Devuelve none

#Usar get con un valor predeterminado si la clave no existe
pais_con_valor_predeterminado= persona.get ('país', 'no especificado')
print('País (con valor predeterminado):', pais_con_valor_predeterminado)






