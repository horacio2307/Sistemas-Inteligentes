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