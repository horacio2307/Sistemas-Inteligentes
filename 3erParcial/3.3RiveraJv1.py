#Entrenar: encontrar los pesos correctos para RNA
#Este programa solo realiza una RNA vacia (sin entrenamiento)
#Pseudocodigo para una XOR

import math

def sumatoria2w(w1,w2,wb,x1,x2):
    s=x1*w1+x2*w2+b*wb
    f=1.0/(1.0+math.exp(-1.0*s))
    return f
def sumatoria3w(w1,w2,w3,wb,x1,x2,x3):
    s=x1*w1+x2*w2+x3*w3+b*wb
    f=1.0/(1.0+math.exp(-1.0*s))
    return f
y=0
b=-1.0
w1N0co=16.15539073
w2N0co=-14.82760190
wbN0co=-5.69685459
w1N1co=11.76634848
w2N1co=-15.25581836
wbN1co=5.14601722
w1N2co=11.76634848
w2N2co=-15.25581836
wbN2co=5.14601722
w1N0cs=-16.50473833
w2N0cs=19.38564062
w3N0cs=19.38564062
wbN0cs=-10.61537742
#pulso de la capa de entrada
xa=float(input("dame x1:"))
xb=float(input("dame x1:"))
N0ce=xa
N1ce=xb
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

print(y)