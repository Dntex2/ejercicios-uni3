import numpy as np
# Arreglo original
arreglo = np.random.randint(0,101, size =10)
# Copia del arreglo
arreglo2 = arreglo[:].copy()
# Arreglo mayor
arreglo3 = arreglo2.max()
# Arreglo menor
arreglo4 = arreglo2.min()
# Suma de los elementos
arreglo5 = arreglo2.sum()
# Promedio de los elementos
arreglo6 = np.mean(arreglo2)
#Mostrar todos los elementos
print("El arreglo original es: ", arreglo)
print("El valor mayor del arreglo es: ",arreglo3)
print("El valor menor del arreglo es: ",arreglo4)
print("La suma de todos los elemntos del arreglo es: ",arreglo5)
print("El promedio del arreglo es: ",arreglo6)