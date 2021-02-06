#Autor Juan Horacio Rivera Peña
from tkinter import *
import time, threading

ventana=Tk()
ventana.geometry("700x400") 
ventana.title("Grafica Difusa           Juan Horacio Rivera Peña            Sistemas Inteligentes")
c=Canvas(ventana,width=700,height=400)


def dibujar(c):
    c.create_line(100, 50, 100, 350, 600, 350,width=2.0)
    c.create_line(100,75,300,75,450,350,600,350,fill="blue")
    c.create_line(100,2175/7,300,2175/7,450,75,600,75,fill="red")
    c.place(x=0,y=0)



def ciclo():
    p=0 
    tem=0
    for i in range(0,101):
        dibujar(c)
        c.place(x=0,y=0)
        if(i<30):
            p=0
        else:
            p=15/40*(i-30)
        if(i>69):
            p=15
        tem=5+2*p
        print("tiempo: {}\tpresion: {}\t\ttemperatura: {}".format(i,p,tem))
        tpx=100+5*i
        l=c.create_line(tpx,75,tpx,350,width=1.5,fill="yellow")
        time.sleep(0.25)
        c.delete(l)
    l=c.create_line(tpx,75,tpx,350,width=1.5,fill="yellow")        
    print("Cierre la ventana porfavor :D")   
 
t1=threading.Thread(target=dibujar)
t2=threading.Thread(target=ciclo)
t1.start()
t2.start()
ventana.mainloop()
