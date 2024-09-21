#Operadores Lógicos
#Definimos distintas variables para ver para usar en las comparaciones

a=10
b=5
c=15
d=8

#Operador AND

resultado_and= (a>b) and (c>d)
#Ambas tienen que ser verdadero para que salga 'true'

print(f'Resultado de (a>b) and (c>d)= {resultado_and}')

# 10 es mayor que 5 por eso sale 'true'
# 15 es mayor que 8 por eso sale 'true'

#Operador OR

resultado_or= (a<b) or (c>d)

print(f'Resultado de (a<b) and (c>d)= {resultado_and}')

# El operador OR permite que si una de las condiciones se cumple,
# debe ser verdadera para que el resultado sea 'true'

# 10 no es mayor que 5 por eso sale pero 15 sí es mayor que 8 por eso sale 'true'

#Operador NOT

resultado_not= not(a<b)

print(f'Resultado de (a<b)= {resultado_not}')

# Hay una predisposición negativa, es por eso que se pone 'not'

#Combinación de los operadores lógicos

resultado_combo=(a>b) and (not (c<b)) or (b<c)

print(f'Resultado de combo= {resultado_combo}')

# (a > b) es 'true' porque 10 es mayor a 5
# (c > d) es 'false' porque 8 es menor a 15 y esto se suma al not (false)
# (a > b) y (c < d) es 'true' + and + True or True resulta 'true'





