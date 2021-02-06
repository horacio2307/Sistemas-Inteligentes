#Autor Juan Horacio Rivera Peña 
e=[[99,99,99,99,99],
   [99,0 ,99,0 ,99],    
   [99,0 ,99,0 ,99],
   [99,0 ,0 ,0 ,99],
   [99,99,99,99,99]]

r=[[0,0,0,0,0],
   [0,0,0,0,0],
   [0,0,0,0,0],
   [0,0,0,0,0],
   [0,0,0,0,0]]

def imprimir(a):
    for i in range (0,5):
        for j in range(0,5):
            print(a[i][j],"\t", end="")
        print()
    print("\n")                    

def menor(x,y,s):

    arriba=s[x][y-1]
    derecha=s[x+1][y]
    abajo=s[x][y+1]
    izquierda=s[x-1][y]

    if(arriba<derecha and arriba<abajo and arriba<izquierda):
        return 1

    if(derecha<arriba and derecha<abajo and derecha<izquierda):
        return 2
    
    if(abajo<arriba and abajo<derecha and abajo<izquierda):
        return 3
    
    if (izquierda<arriba and izquierda<derecha and izquierda<abajo):
        return 4

ri=int(input("Ingrese la fila del inicio: [0,4] "))
ci=int(input("Ingrese la columna del inicio: [0,4] "))
print("\n")
rm=int(input("Ingrese la fila del fin: [0,4] "))
cm=int(input("Ingrese la columna del fin: [0,4] "))
print("\n")
imprimir(e)
for i in range(5):
    for j in range(5):
        r[i][j]=abs(i-rm)+abs(j-cm)
for i in range(5):
    for j in range(5):
        if(r[i][j]>e[i][j]):
            e[i][j] = r[i][j]
imprimir(r)
imprimir(e)

z=10 
i=ri 
j=ci 

bandera=menor(i,j,e)

while(e[i][j]!=0):
    e[i][j]=z
    imprimir(e)
    if(bandera==1):
        j-=1

    elif(bandera==2):
        i+=1
    
    elif (bandera==3):
        j+=1

    elif (bandera==4):
        i-=1
    z+=1

    bandera=menor(i,j,e)
    
print("Llego a la meta :D")
        
