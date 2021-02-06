#Autor Juan Horacio Rivera Peña 
import random

def f(x): #Funcion f(x)

    return -x**2+5*x+3

def Convertir(M,m): #De binario a decimal
    z=[0,0,0,0,0] 
    for i in range(0,5):
        for j in range(0,12):
            z[i]=z[i]+M[i][j]*pow(2,m[j])

    return z

numeros=[[1,1,1,1,0,0,1,0,1,0,1,0], #Matriz de los 5 individuos
         [0,1,1,0,0,0,1,1,1,0,1,0],
         [0,0,0,0,0,1,1,1,1,0,1,0],
         [1,0,0,1,0,1,1,1,0,0,0,0],
         [1,0,0,0,0,0,1,1,1,0,1,0]]

potencias=[1,0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10] #Matriz para elevar a las potencias binarias

for i in range(0,5): #Llenar aleatoriamente las matrices de 1 y 0
    for j in range(0,12):
        numeros[i][j]=random.randint(0,1)


NuDecimal=Convertir(numeros,potencias) #5 numeros en decimal 

for i in range(0,5): #Imprimir los numeros en formato tabla
    print("Cromosomoas {}: {}\tNumero x: {}\t Valor de f(x): {}".format(i+1,numeros[i],NuDecimal[i],f(NuDecimal[i])))



