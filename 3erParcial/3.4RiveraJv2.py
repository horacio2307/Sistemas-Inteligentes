#Autor Juan Horacio Rivera Peña
#Entrenamiento del perceptron 
import random,time

x1=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
x2=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
T=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
pesos=[0,0,0]
w1=random.uniform(-10,10)
w2=random.uniform(-10,10)
phi=random.uniform(-10,10)

def train(x):

    a=[w1,w2,phi]
    a[0]=a[0]+T[x]*x1[x]
    a[1]=a[1]+T[x]*x2[x]
    a[2]=a[2]-T[x]
    
    #print("Los nuevos pesos son {}\n".format(a))
    return a


def proceso():

    if(z>=0):
        y=1
            
    else:
        y=-1

    return y

print("Los pesos iniciales son w1={}, w2={}, phi={}".format(w1,w2,phi))
for i in range(0,15):

    if(i<10):
        print("\nPrueba ",i+1)
        x1[i]=int(input("Dame x1(peso):"))
        x2[i]=int(input("Dame x2(estatura):"))
        T[i]=int(input("Dame T(H --> 1  M --> -1 u Otro):\t"))
        if(T[i]!=1):
            T[i]=-1

        z=w1*x1[i]+w2*x2[i]-phi

        y=proceso()

        if(y==1):
            print("Hombre")
        else:
            print("Mujer")

        if(y!=T[i]):
            print("!Error! Se necesita entrenar\t")
            j=0
            pesos=train(i)
            w1=pesos[0]
            w2=pesos[1]
            phi=pesos[2]
            while (j<i):
                
                z=w1*x1[j]+w2*x2[j]-phi
                y=proceso()
                if(T[j]==y):
                    j=j+1
                else:
                    pesos=train(j)
                    w1=pesos[0]
                    w2=pesos[1]
                    phi=pesos[2]
                    j=0
                    print("w1={}, w2={}, phi={}".format(w1,w2,phi))
                    time.sleep(0.5)
                

        
        if(i==9):
            print("Los pesos finales son w1={}, w2={}, phi={}".format(w1,w2,phi))

    else:
        print("\nPrueba ",i+1)
        x1[i]=int(input("Dame x1(peso):"))
        x2[i]=int(input("Dame x2(estatura):"))
        z=w1*x1[i]+w2*x2[i]-phi

        y=proceso()

        if(y==1):
            print("Hombre")
        else:
            print("Mujer")

print("Prubas finalizadas")
