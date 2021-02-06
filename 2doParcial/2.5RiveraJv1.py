#Autor Juan Horacio Rivera Peña 

from tkinter import *

ventana =Tk()
c=Canvas(ventana,width=700,height=400)
ventana.geometry("700x400") 
ventana.title("Grafica Difusa           Juan Horacio Rivera Peña            Sistemas Inteligentes")

def dibujar(c):
    c.create_line(50, 50, 50, 350, 650, 350,width=2.0)

    c.create_line(50,75,200,75,290,350,650,350,fill="blue")
    c.create_line(50,350,140,350,290,75,440,75,530,350,650,350,fill="green")
    c.create_line(50,350,440,350,560,75,650,75,fill="red")
    c.create_line(500,350,500,75)
    coord = 440-60,75,440+60,350
    arc = c.create_arc(coord, start=0, extent=-90, fill="red")
    coord = 560-60,75,560+60,350
    arc = c.create_arc(coord, start=90, extent=90, fill="red")

dibujar(c)
c.place(x=0,y=0)

ventana.mainloop()