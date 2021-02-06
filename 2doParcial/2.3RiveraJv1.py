#Autor Juan Horacio Rivera Peña

from tkinter import *

def lee_numero():
   while True:
       print("Escribe el valor de la temperatura: [15,35] ")
       entrada = input("Un valor fuera del rango para el programa :")
       try:
           entrada = int(entrada)
           return entrada
       except ValueError:
           print("La entrada es incorrecta: escribe un numero")

ventana =Tk()
c=Canvas(ventana,width=700,height=400)
ventana.geometry("700x400") 
ventana.title("Grafica Difusa           Juan Horacio Rivera Peña            Sistemas Inteligentes")

def dibujar(c):
    c.create_line(50, 50, 50, 350, 650, 350,width=2.0)

    c.create_line(50,75,200,75,290,350,650,350,fill="blue")
    c.create_line(50,350,140,350,290,75,440,75,530,350,650,350,fill="green")
    c.create_line(50,350,440,350,560,75,650,75,fill="red")
    
dibujar(c)
c.place(x=0,y=0)
t=lee_numero()-15
tpx=50+30*t
while(t>=0 and t<=20):
    dibujar(c)
    c.create_line(tpx,75,tpx,350,width=1.5,fill="yellow")
    c.place(x=0,y=0)
    t=lee_numero()-15
    tpx=50+30*t
    c.delete("all")

print("Cierre la ventana porfavor :D")
ventana.mainloop()



