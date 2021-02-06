#Autor Juan Horacio Rivera Peña 
r=[[0,0,0,0,0],
   [0,0,0,0,0],
   [0,0,0,0,0],
   [0,0,0,0,0],
   [0,0,0,0,0]]

def imprimir():
    for x in range(5):
        print(r[x],"\n")

def der(a,b):
    z=r[a][b]
    for x in range(b,5): #x ira a la derecha valor=j
        r[a][x]=z
        z+=1

def izq(a,b):
    z=r[a][b]
    x=b
    while(x>=0):   #x ira a la izquierda valor=j
        r[a][x]=z
        z+=1
        x-=1

def fila():

    z=0 #Abajo
    for x in range(i,5):
        r[x][j]=z
        z+=1

    z=0 
    x=i #Arriba
    while(x>=0):
        r[x][j]=z
        x-=1
        z+=1
i=j=10
while(not((i<5 and i>-1) and (j<5 and j>-1))):
    i=int(input("Ingrese la fila del 0: [0,4] "))
    j=int(input("Ingrese la columna del 0: [0,4] "))
    print("\n")
print()
fila()  
for x in range(0,5):
    der(x,j)
    izq(x,j)
imprimir()





