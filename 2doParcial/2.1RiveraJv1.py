#Autor Juan Horacio Rivera Peña

from tkinter import *

ventana =Tk()
c=Canvas(ventana,width=600,height=300)
ventana.geometry("620x330") 
ventana.title("Grafica Difusa           Juan Horacio Rivera Peña            Sistemas Inteligentes")

c.create_line(10, 10, 10, 300,width=2.0)
c.create_line(10,300, 600, 300,width=2.0)

c.create_line(10,75,120,75,160,300,fill="blue")
c.create_line(120,300,160,75,420,75,460,300,fill="green")
c.create_line(420,300,460,75,600,75,fill="red")

c.place(x=0,y=0)
ventana.mainloop()