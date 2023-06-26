import numpy as np
arreglo = np.random.randint(0,101, size=(3,3))
# Copia del arreglo
arreglo2 = arreglo[:].copy()
# Promedio del arreglo
arreglo3 = np.mean(arreglo2)
# Elemento mayor del arreglo
arreglo4 = arreglo2.max()
# Elemento menor del arreglo
arreglo5 = arreglo2.min()
# Elementos diag principal
arreglo6 = arreglo2.diagonal()
# Mostrar todos los elementos
print("La lista original del arreglo es: ")
print(arreglo)
print("El promedio del arreglo es de: ", arreglo3)
print("El elemento mayor del arreglo es: ", arreglo4)
print("El elemento menor del arreglo es: ", arreglo5)
print("Los elementos de la diag principal son: ", arreglo6)
