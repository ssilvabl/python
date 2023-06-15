# TUPLAS

# Definición: Las tuplas son lista inmutables, están optimizadas y se pueden declarar con o sin paréntesis
# Uso: nueva_tupla = ("hola", 12, 12.0)

nueva_tupla = ("hola", 1, 1, 12.0)
print(nueva_tupla)

# Acceder a índice
print(nueva_tupla[2])

# Convertir tupla en lista
nueva_lista = list(nueva_tupla)
print(type(nueva_lista))

# Convertir lista en tupla
nueva_tupla1 = tuple(nueva_lista)
print(type(nueva_tupla1))

# Validar si existe elemento en la tupla
print("hola" in nueva_tupla1)

# Contar mismo elemento en una tupla
print(nueva_tupla1.count(1))

# Contar elementos dentro de una tupla
print(len(nueva_tupla1))

#Tupla unitaria
tupla_unitaria = ("hola")

# Desempaquetado de tupla
saludo, num1, num2, num3 = nueva_tupla1

print(saludo, num2, num3, num1)
