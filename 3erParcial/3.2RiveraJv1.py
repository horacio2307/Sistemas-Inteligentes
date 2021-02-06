#Autor Rivera Peña Juan Horacio
import time, random

global w1,w2,phi,T,x1,x2

w1=random.uniform(-10,10)
w2=random.uniform(-10,10)
phi=random.uniform(-10,10)


def train(h):

    global w1,w2,phi,T,x1,x2
    print("Error en {}\n".format(h+1))
    a=[w1,w2,phi]
    #print("Los valores actuales son {}".format(a))
    a[0]=a[0]+T[h]*x1[h]
    a[1]=a[1]+T[h]*x2[h]
    a[2]=a[2]+T[h]*-1
    
    print("Los nuevos pesos son {}\n".format(a))
    return a

j=1
z=0
x1=[1,1,-1,-1]
x2=[1,-1,1,-1]
T=[0,0,0,0]
R=[0,0,0,0]
bandera=True
pesos=[0,0,0]

opcion=input("1--> Or   2--> And    Otro--> xor\t")

if(opcion=="1"):
    T=[1,1,1,-1]

elif(opcion=="2"):
    T=[1,-1,-1,-1]

else:
    T=[-1,1,1,-1]

print("Los pesos iniciales son w1={}, w2={}, phi={}\n".format(w1,w2,phi))

while(bandera):

    print("Prueba {}".format(j))
    
    for i in range(0,4):

        z=w1*x1[i]+w2*x2[i]-phi

        print("Renglon {}".format(i+1))
        if(T[i]==1):
            if(z>=0):            
                R[i]=1
            else:
                R[i]=0
        elif(T[i]==-1):
            if(z<0):
                R[i]=1
            else:
                R[i]=0
        print("{},\t\t{}".format(z,R[i]))
        time.sleep(1)
    if(R[0]+R[1]+R[2]+R[3]==4):
        bandera=False
    else:
        bandera=True
        if(R[0]==0):
            pesos=train(0)
        elif(R[1]==0):
            pesos=train(1)
        elif(R[2]==0):
            pesos=train(2)
        elif(R[3]==0):
            pesos=train(3)
    w1=pesos[0]
    w2=pesos[1]
    phi=pesos[2]
    j+=1

print("\nNeurona Entrenada :)")


