#Autor: Juan Horacio Rivera Peña
a=[1,4,6,3]
print("El vector inical es")
print("(",a[0],",",a[1],",",a[2],",",a[3],")\n")
a0=a[0]
a1=a[1]
a2=a[2]
a3=a[3]
Mayor = Segundo = Tercer = Menor = 0

#a0 es el mayor

if((a0>a1 and a0>a2 and a0>a3) and (a1>a2 and a1>a3) and (a2>a3)):
    Mayor = a0
    Segundo = a1
    Tercero = a2
    Menor = a3

elif((a0>a1 and a0>a2 and a0>a3) and (a1>a2 and a1>a3) and (a2<a3)):
    Mayor = a0
    Segundo = a1
    Tercero = a3
    Menor = a2

elif((a0>a1 and a0>a2 and a0>a3) and (a1<a2 and a1<a3) and (a2>a3)):
    Mayor = a0
    Segundo = a2
    Tercero = a3
    Menor = a1

elif((a0>a1 and a0>a2 and a0>a3) and (a1<a2 and a2>a3) and (a1>a3)):
    Mayor = a0
    Segundo = a2
    Tercero = a1
    Menor = a3

elif((a0>a1 and a0>a2 and a0>a3) and (a1<a3 and a1<a3) and (a2>a1)):
    Mayor = a0
    Segundo = a3
    Tercero = a2
    Menor = a1

elif((a0>a1 and a0>a2 and a0>a3) and (a1<a3 and a1<a3) and (a2<a1)):
    Mayor = a0
    Segundo = a3
    Tercero = a1
    Menor = a2

#a1 es el mayor

elif((a1>a0 and a1>a2 and a1>a3) and (a0>a2 and a0>a3) and (a2>a3)):
    Mayor = a1
    Segundo = a0
    Tercero = a2
    Menor = a3

elif((a1>a0 and a1>a2 and a1>a3) and (a0>a2 and a0>a3) and (a2<a3)):
    Mayor = a1
    Segundo = a0
    Tercero = a3
    Menor = a2

elif((a1>a0 and a1>a2 and a1>a3) and (a3>a2 and a0<a3) and (a2<a0)):
    Mayor = a1
    Segundo = a3
    Tercero = a0
    Menor = a2

elif((a1>a0 and a1>a2 and a1>a3) and (a3>a2 and a0<a3) and (a2>a0)):
    Mayor = a1
    Segundo = a3
    Tercero = a2
    Menor = a0

elif((a1>a0 and a1>a2 and a1>a3) and (a3<a2 and a0<a2) and (a3>a0)):
    Mayor = a1
    Segundo = a2
    Tercero = a3
    Menor = a0

elif((a1>a0 and a1>a2 and a1>a3) and (a3<a2 and a0<a2) and (a3<a0)):
    Mayor = a1
    Segundo = a2
    Tercero = a0
    Menor = a3

#a2 es el mayor

elif((a2>a0 and a2>a1 and a2>a3) and (a0>a1 and a0>a3) and (a1>a3)):
    Mayor = a2
    Segundo = a0
    Tercero = a1
    Menor = a3

elif((a2>a0 and a2>a1 and a2>a3) and (a0>a1 and a0>a3) and (a1<a3)):
    Mayor = a2
    Segundo = a0
    Tercero = a3
    Menor = a1

elif((a2>a0 and a2>a1 and a2>a3) and (a3>a1 and a0<a3) and (a1<a0)):
    Mayor = a2
    Segundo = a3
    Tercero = a0
    Menor = a1

elif((a2>a0 and a2>a1 and a2>a3) and (a3>a1 and a0<a3) and (a1>a0)):
    Mayor = a2
    Segundo = a3
    Tercero = a1
    Menor = a0

elif((a2>a0 and a2>a1 and a2>a3) and (a3<a1 and a1>a3) and (a3>a0)):
    Mayor = a2
    Segundo = a1
    Tercero = a3
    Menor = a0

elif((a2>a0 and a2>a1 and a2>a3) and (a3<a1 and a1>a3) and (a3<a0)):
    Mayor = a2
    Segundo = a1
    Tercero = a0
    Menor = a3

#a3 es el mayor

elif((a3>a0 and a3>a1 and a3>a2) and (a0>a1 and a0>a2) and (a1>a2)):
    Mayor = a3
    Segundo = a0
    Tercero = a1
    Menor = a2

elif((a3>a0 and a3>a1 and a3>a2) and (a0>a1 and a0>a2) and (a1<a2)):
    Mayor = a3
    Segundo = a0
    Tercero = a2
    Menor = a1

elif((a3>a0 and a3>a1 and a3>a2) and (a1>a0 and a1>a2) and (a0<a2)):
    Mayor = a3
    Segundo = a1
    Tercero = a2
    Menor = a0

elif((a3>a0 and a3>a1 and a3>a2) and (a1>a0 and a1>a2) and (a0>a2)):
    Mayor = a3
    Segundo = a1
    Tercero = a0
    Menor = a2

elif((a3>a0 and a3>a1 and a3>a2) and (a2>a0 and a1<a2) and (a0>a1)):
    Mayor = a3
    Segundo = a2
    Tercero = a0
    Menor = a1

elif((a3>a0 and a3>a1 and a3>a2) and (a2>a0 and a1<a2) and (a0<a1)):
    Mayor = a3
    Segundo = a2
    Tercero = a1
    Menor = a0

a[0]=Menor
a[1]=Tercero
a[2]=Segundo
a[3]=Mayor

print("El vector reacomodado es :")
print("(",a[0],",",a[1],",",a[2],",",a[3],")")