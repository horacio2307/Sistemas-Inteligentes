#Autor: Juan Horacio Rivera Peña
import random
import numpy as np
import math


def sumatoria2w(w1,w2,wb,x1,x2):
    s=x1*w1+x2*w2-wb
    f=1.0/(1.0+math.exp(-1.0*s))
    return f
def sumatoria3w(w1,w2,w3,wb,x1,x2,x3):
    s=x1*w1+x2*w2+x3*w3-wb
    f=1.0/(1.0+math.exp(-1.0*s))
    return f

def Neurona(Individuo): #Funcion que regresa el total de aciertos de un Individuo

    x1=[0,0,1,1]
    x2=[0,1,0,1]
    y=0
    z=0
    w1N0co=Individuo[0]
    w2N0co=Individuo[1]
    wbN0co=Individuo[2]
    w1N1co=Individuo[3]
    w2N1co=Individuo[4]
    wbN1co=Individuo[5]
    w1N2co=Individuo[6]
    w2N2co=Individuo[7]
    wbN2co=Individuo[8]
    w1N0cs=Individuo[9]
    w2N0cs=Individuo[10]
    w3N0cs=Individuo[11]
    wbN0cs=Individuo[12]
    for i in range(0,4):
        N0ce=x1[i]
        N1ce=x2[i]
        #pulso de la capa de oculta
        N0co=sumatoria2w(w1N0co,w2N0co,wbN0co,N0ce,N1ce) 
        N1co=sumatoria2w(w1N1co,w2N1co,wbN1co,N0ce,N1ce) 
        N2co=sumatoria2w(w1N2co,w2N2co,wbN2co,N0ce,N1ce) 
        #pulso de la capa de salida
        N0cs=sumatoria3w(w1N0cs,w2N0cs,w3N0cs,wbN0cs,N0co,N1co,N2co) 
        if (N0cs<0.5):
            y=0
        else:
            y=1
        
        if y == XOR[i]:

            z+=1

       
        #print("{} XOR {} = {}".format(x1[i],x2[i],y))

    return z #Regresa el numero de acieros x individuo

def sumalista(listaNumeros): #Suma de la lista
    laSuma = 0
    for i in range(0,NuIndividuos):
        laSuma += listaNumeros[i]
    return laSuma  

NuIndividuos = 100
iteracion = 0
Limite = 1
poblacion = np.zeros((NuIndividuos, 13)) #Creamos poblacion Inicial
XOR = np.array([0,1,1,0])
Aciertos = np.zeros(NuIndividuos)
probabilidades = np.zeros(NuIndividuos)
Fin = False
Posicion=0

for i in range(0,NuIndividuos): #Creamos poblacion Inicial
    for j in range(0,13):
        poblacion[i][j]=40*random.uniform(-1,1)

while iteracion < Limite :
    for i in range (0,NuIndividuos):#Calcular aciertos
        Aciertos[i]=Neurona(poblacion[i])
        #print("Aciertos Individuo {}\t = {}".format(i+1,Aciertos[i]))
        if Aciertos[i] == 4 and Fin == False: #Si encuentra 4 aciertos Fin=True
            Fin = True
            Posicion=i
    
    #Si encontro 4 aciertos el programa termina
    if Fin == True :
        iteracion=Limite
        print("El individuo {} tiene 4 aciertos".format(Posicion+1))

    #Sino el programa sigue
    else:
        
        #Calcular probabilidades
        
        for i in range(0,NuIndividuos):

            probabilidades[i]=Aciertos[i]/sumalista(Aciertos)
            print("Probabilidad Individuo {} \t= {}".format(i+1,probabilidades[i]))

        print("La suma de probabilidades es \t=",sumalista(probabilidades))

        #Aumenta la iteracion
        iteracion+=1

print("Fin del programa")




