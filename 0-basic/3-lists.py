# LISTAS


# Uso: nombreLista = [elemento1, elemento2, etc]

# Lista de nombres
listaNombres = ["santiago", "valentina", "juan", "maria", "pedro"]
# Imprimir todos los elementos de la lista
print(listaNombres[:])

# Imprimir un índice en particular
print(listaNombres[2])

# Imprimir en un rango (num1:donde comienza el rango : num2:donde termina el rango y excluye el índice indicado)
print(listaNombres[0:2])
print(listaNombres[:2])
print(listaNombres[1:2])
print(listaNombres[1:])

# Función para agregar elemento a una lista
# Uso: nombreLista.append(elementoAAñadir) -> se agrega al final de la lista
# Uso: nombreLista.insert(indice del lugar al que se va a añadir, elementoAAñadir) -> se agrega en una posición en específico
# Uso: nombreLista.extend([elemento, elemento2]) -> Agregar múltiples elementos

# Aladir elemento a la lista
listaNombres.append(1999)
print(listaNombres[:])

listaNombres.insert(2, "laura")
print(listaNombres)

listaNombres.extend(["santi", "miguel", 21])
print(listaNombres)

# Buscar indice utilizando el elemento (sólo devuelve el indice del primer elemento que coincida)
# Uso: listaNombres.index("santi") -> devuelve el indice en el que está el elemento "santi"

print(listaNombres.index("valentina"))

# Valdiar si un elemento existe en una lista
# Uso: print("elementoABuscar" in listaNombres) -> devuelve True o False

statusValidate = "santi" in listaNombres
print(statusValidate)

# Remover elementos de la lista
# Uso: listaNombres.remove(elementoAEliminar)
# Uso: listaNombres.pop() -> Elimina el último elemento de la lista

listaNombres.remove("santiago")
print(listaNombres)

# Unir listas
listaNombres2 = ["ana", "maria", "sefue"]
listaNombres3 = listaNombres + listaNombres2
print(listaNombres3)

# Multiplicar listas
listaNombres4 = ["ana", "maria", "sefue"] * 4
print(listaNombres4)
