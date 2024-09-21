#Diccionario dentro de una Lista
#1.Crea una lista de diccionarios donde cada diccionario 
# representa unproducto en una tienda, con claves:
#  Nombre
#  Precio
#  Cantidad en stock
#2. Imprime el nombre y el precio del segundo producto en la lista.

lista_super = [
    {'Producto':'Manzana',
        'Precio': 20,
        'Cantidad en stock': 712
    },
    {
        'Producto':'Cereal',
        'Precio': 25,
        'Cantidad en stock': 4000
    },
    {
        'Producto':'Leche',
        'Precio': 44,
        'Cantidad en stock': 4000
    }
]

segundo_producto= lista_super[1]['Producto']
precio_segundo_producto= lista_super[1]['Precio']

print('\n El segundo producto de la lista del super es,', [segundo_producto], 'y cuesta', [precio_segundo_producto],'pesos\n')