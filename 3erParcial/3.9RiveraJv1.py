#Autor: Juan Horacio Rivera Peña

import random
import numpy as np

poblacion = np.zeros((10, 13)) #Creamos una matriz de 10 x 13

for i in range(0,10):   #Asignamos  valores de -40 a 40
    for j in range(0,13):
        poblacion[i][j]=40*random.uniform(-1,1)

for i in range(0,10): #Imprimimos el valor de cada indiciduo
    print("Individuo :",i+1)
    print(poblacion[i])


