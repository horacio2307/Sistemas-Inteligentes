#Autor Juan Horacio Rivera Peña

from tkinter import *

def lee_numero():
   while True:
       entrada = input("Escribe el valor de la temperatura: [15,23] ")
       try:
           entrada = int(entrada)
           return entrada
       except ValueError:
           print("La entrada es incorrecta: escribe un numero")

ventana =Tk()
c=Canvas(ventana,width=700,height=400)
ventana.geometry("700x400") 
ventana.title("Grafica Difusa           Juan Horacio Rivera Peña            Sistemas Inteligentes")

c.create_line(50, 50, 50, 350, 650, 350,width=2.0)

c.create_line(50,75,200,75,290,350,650,350,fill="blue")
c.create_line(50,350,140,350,290,75,440,75,530,350,650,350,fill="green")
c.create_line(50,350,440,350,560,75,650,75,fill="red")

c.place(x=0,y=0)

b = m = a = 0

t=lee_numero()

while(t<15 or t>23 ):
    print("Usted ingreso un valor invalido")
    t=lee_numero()

if(t<18):
    b=1
    m = 0

if(t>=18 and t<20):
    b=1
    m=(t-18)/(23-18)

if(t>=20):
    b=1-(t-20)/(23-20)
    m=(t-18)/(23-18)

print("GpBajo= ",b,"\n")
print("GpMedioo= ",m,"\n")
print("GpAlto= ",a,"\n")

ventana.mainloop()