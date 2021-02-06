#Autor Juan Horacio Rivera Peña
def promedio(i,j,a):
    
    suma=0
    for x in range (-1,2):

        for y in range (-1,2):

            suma=suma+a[i+x][j+y]

    suma=suma-a[i][j]

    suma/=8

    return suma 

m=[[1,2,1,2,0,1],
   [3,4,3,4,0,1],
   [5,6,5,6,0,1],
   [7,8,7,8,0,1],
   [7,8,7,8,0,1],
   [7,8,7,8,0,1]]

for c in range(1,5):
    for r in range(1,5):        
        print("El promedio de la posicion ",c,",",r," es ",promedio(c,r,m))
        
#Comenzando con el elemento 1,1 y terminando en 4,4
#Imprimir la coordenada del elemento y el promedio de sus 8 vecinos
#Utilizar forzosamente un metodo def () en dos for anidados
#Imprimir exactamente como esta debajo
#El promedio de la posicion 1,1 es 3.25
#El promedio de la posicion 1,2 es 3.75
