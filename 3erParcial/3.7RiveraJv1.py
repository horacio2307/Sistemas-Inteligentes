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
        a=random.random()
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

def mutar(x,a): #Mutar al bebex en el bit a
    if(x[a]==0):
        x[a]=1
    else:
        x[a]=0

def Buscar_Menos_Aptos(Vector_F): #Retorna las posiciones de los menos aptos

    y=[0,0,0,0,0]
    x=[0,0]
    y=sorted(Vector_F)
    for j in range (0,2):
        for i in range (0,5):
            if(y[j]==Vector_F[i]):
                x[j]=i
                Vector_F[i]=0
    x=sorted(x)
    return x
    



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

#Bebes 
bebe1=[0,0,0,0,0,0,0,0,0,0,0,0]
bebe2=[0,0,0,0,0,0,0,0,0,0,0,0] 

potencias=[1,0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10] #Matriz para elevar a las potencias binarias

for i in range(0,5): #Llenar aleatoriamente las matrices de 1 y 0
    for j in range(0,12):
        numeros[i][j]=random.randint(0,1)


NuDecimal=Convertir(numeros,potencias) #5 numeros en decimal 

for i in range(0,5): #Imprimir los numeros en formato tabla
    FuncionF[i]=f(NuDecimal[i])                        
    print("Cromosomoas {}: {}\t\tNumero x: {}\t\t Valor de f(x): {}".format(i+1,numeros[i],NuDecimal[i],FuncionF[i]))
print("\nEl valor promedio es {}\n".format(sumalista(FuncionF)/5))

for i in range(0,5): #Genera vector de porcentajes
    Porcentajes[i]=FuncionF[i]/sumalista(FuncionF)*100
    print("Porcentaje indiviudo {} = {}".format(i+1,Porcentajes[i]))


Padres=Ruleta(Recta(Porcentajes),10) #Obtiene 2 padres
print("\nLos padres son los inviduos {} y {}".format(Padres[0]+1,Padres[1]+1))

for i in range(0,5): #Imprimir los numeros de los padres en formato tabla
    if(i in Padres):
        print("Cromosomoas {}: {}\tNumero x: {}\t Valor de f(x): {}".format(i+1,numeros[i],NuDecimal[i],FuncionF[i]))

#Crear 2 bebes
Bit_Cruza = random.randint(1,10)

print("\nSe va a cruzar en el bit {}".format(Bit_Cruza+1))

for i in range(12):
    if i <= Bit_Cruza:
        bebe1[i]=numeros[Padres[0]][i]
        bebe2[i]=numeros[Padres[1]][i]
    else:
        bebe1[i]=numeros[Padres[1]][i]
        bebe2[i]=numeros[Padres[0]][i]        

print("Las crias sons las siguientes\nBebe 1 {}\nBebe 2 {}".format(bebe1,bebe2))

#Mutar?
p1=random.randint(0,100)
p2=random.randint(0,100)
print("\nProbablidades de mutacion del bebe1 {}% y del bebe2 {}%".format(p1,p2))
if(p1<=30 or p2<=30):
    if(p1<=30):
        Bit_mutar=random.randint(0,11)
        mutar(bebe1,Bit_mutar)
        print("El bebe 1 mutara en el bit ",Bit_mutar+1)
    if(p2<=30):
        Bit_mutar=random.randint(0,11)
        mutar(bebe2,Bit_mutar)
        print("El bebe 2 mutara en el bit ",Bit_mutar+1)

    print("Las crias sons las siguientes\nBebe 1 {}\nBebe 2 {}".format(bebe1,bebe2))

else:
    print("No hay mutacion")


#Buscar las posiciones de los individuos menos aptos
Vector_Menos_Aptos=Buscar_Menos_Aptos(FuncionF)
print("Los individuos menos aptos son los numeros {} y {}".format(Vector_Menos_Aptos[0]+1,Vector_Menos_Aptos[1]+1))

#Elitismo
numeros[Vector_Menos_Aptos[0]]=bebe1
numeros[Vector_Menos_Aptos[1]]=bebe2
print("\nLa nueva generacion es la siguiente")

#Nueva generacion
NuDecimal=Convertir(numeros,potencias) #5 numeros en decimal 

for i in range(0,5): #Imprimir los numeros en formato tabla
    FuncionF[i]=f(NuDecimal[i])                        
    print("Cromosomoas {}: {}\t\tNumero x: {}\t\t Valor de f(x): {}".format(i+1,numeros[i],NuDecimal[i],FuncionF[i]))

