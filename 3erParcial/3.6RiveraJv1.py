#Autor Juan Horacio Rivera Peña 
import random

#Funciones para el programa

def f(x): #Funcion f(x)

    return -x**2+5*x+3

def Convertir(M,m): #De binario a decimal
    z=[0,0,0,0,0] 
    for i in range(0,5):
        for j in range(0,12):
            z[i]=z[i]+M[i][j]*pow(2,m[j])

    return z

def sumalista(listaNumeros): #Suma de la lista
    laSuma = 0
    for i in listaNumeros:
        laSuma = laSuma + i
    return laSuma

def Recta(VectorPorcentajes): #Crear recta unitaria
    z=[0,0,0,0,0]
    z[0]=VectorPorcentajes[0]/100
    for i in range(1,5):
        z[i]=z[i-1]+VectorPorcentajes[i]/100

    print("\nLa recta de unitaria es la siguiente\n\tIndividuo {}\tIndividuo {}\tIndividuo {}\tIndividuo {}\tIndividuo {}\t".format(1,2,3,4,5))
    print(z,"\n")
    return z

def Ruleta(VectorRecta,n): #Tira la ruleta n veces y regresa 2 padres
    x=[0,0,0,0,0]
    y=[0,0,0,0,0]
    z=[0,0]
    for i in range(0,n):
        a=random.uniform(0,1)
        if(a<=VectorRecta[0]):
            x[0]=x[0]+1
            print("Ruleta = 1")
        elif(VectorRecta[0]<a and a<=VectorRecta[1]):
            x[1]=x[1]+1
            print("Ruleta = 2")
        elif(VectorRecta[1]<a and a<=VectorRecta[2]):
            x[2]=x[2]+1
            print("Ruleta = 3")
        elif(VectorRecta[2]<a and a<=VectorRecta[3]):
            x[3]=x[3]+1
            print("Ruleta = 4")
        elif(VectorRecta[3]<a):
            print("Ruleta = 5")
            x[4]=x[4]+1
    print("Resultados ",x)
    y=sorted(x,reverse=True)
    for j in range (0,2):
        for i in range (0,5):
            if(y[j]==x[i]):
                z[j]=i
                x[i]=0
                break
    z.sort()
    return z

#Terminan funciones    
#Inicia Programa

Porcentajes=[0,0,0,0,0] #Vector para la recta unitaria
FuncionF=[0,0,0,0,0]    #Vector para las probabilidades
Padres=[0,0]            #Vector para los padres
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
    FuncionF[i]=f(NuDecimal[i])                        
    print("Cromosomoas {}: {}\tNumero x: {}\t Valor de f(x): {}".format(i+1,numeros[i],NuDecimal[i],FuncionF[i]))

print("\nEl valor promedio es {}\n".format(sumalista(FuncionF)/5))

for i in range(0,5): #Genera vector de porcentajes
    Porcentajes[i]=FuncionF[i]/sumalista(FuncionF)*100
    print("Porcentaje indiviudo {} = {}".format(i+1,Porcentajes[i]))


Padres=Ruleta(Recta(Porcentajes),5) #Obtiene 2 padres
print("\nLos padres son los inviduos {} y {}".format(Padres[0]+1,Padres[1]+1))

for i in range(0,5): #Imprimir los numeros en formato tabla
    if(i in Padres):
        print("Cromosomoas {}: {}\tNumero x: {}\t Valor de f(x): {}".format(i+1,numeros[i],NuDecimal[i],FuncionF[i]))

