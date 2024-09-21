#Ejercicio 2: Categoría de Edad con Operadores Lógicos
#Escribe un programa que clasifique a una persona en una categoría
#según su edad. Usa un condicional if tradicional con operadores
#lógicos (and, or) para las siguientes categorías

#"Niño" si la edad está entre 0 y 12 años.
#  "Adolescente" si la edad está entre 13 y 19 años.
#  "Adulto" si la edad está entre 20 y 64 años.
#  "Adulto Mayor" si la edad es 65 o más.

Edad=(float(input('Inserta tu edad: ')))

if Edad==0 or Edad<12:
    print('Eres un Peque')
if Edad==13 or Edad<=19:
    print('Eres un Adolescente')
if Edad==20 or Edad<=64:
    print('Eres un Adulto')
if  Edad>=65:
    print('Eres un Adulto mayor')
elif Edad<=0 or Edad>=100:
    print('Error')
else:
    print('Error')

print(Edad)
