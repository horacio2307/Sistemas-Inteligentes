#Autor Juan Horacio Rivera Peña
import time
e=[[99,99,99,99,99],
   [99,0 ,99,0 ,99],    
   [99,0 ,99,0 ,99],
   [99,0 ,0 ,0 ,99],
   [99,99,99,99,99]]
#Posicion inicial
ra=ca=1
while(not(ra==1 and ca==3)):   #El mov es en cruz y no se puede mover en diagonal
    if(e[ra-1][ca]==0):        #arriba esta libre? 
        e[ra][ca]=99
        ra=ra-1
        ca=ca
    if(e[ra+1][ca]==0):        #abajo esta libre? 
        e[ra][ca]=99
        ra=ra+1
        ca=ca
    if(e[ra][ca+1]==0):        #dercha esta libre? 
        e[ra][ca]=99
        ra=ra
        ca=ca+1
    if(e[ra][ca-1]==0):        #izquierda esta libre?
        e[ra][ca]=99
        ra=ra
        ca=ca-1    
    for i in range (0,5):
        for j in range(0,5):
            print(e[i][j],"\t", end="")
        print()
    print("\n")                    
    time.sleep(1)
