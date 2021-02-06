#Rivera Peña Juan Horacio
import cv2
import numpy as np
import math
#Capturar video

def lectura():
  video = cv2.VideoCapture(0) 
  #Rangos minimos de azul
  azulBajo = np.array([100,100,20], np.uint8)
  azulAlto = np.array([125,255,255], np.uint8)
  x=[]
  y=[]

  print("Presione s para dejar de grabar")
  #Ciclo del video
  while True:
    ret, captura = video.read()
    if ret==True:

      #Invertir el video
      captura = cv2.flip(captura,1)
      #Convertir el video a HSV y obtener los colores azules  
      capturaHSV = cv2.cvtColor(captura, cv2.COLOR_BGR2HSV)
      mask = cv2.inRange(capturaHSV, azulBajo, azulAlto)
      
      contornos,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
      for c in contornos:
        area=cv2.contourArea(c)
        if area >=1000 :
          M = cv2.moments(c)
          if (M["m00"]==0): M["m00"]=1
          x1 = int(M["m10"]/M["m00"])
          y1 = int(M['m01']/M['m00'])
          x.append(x1)
          y.append(y1)
          #print("{},{}".format(x,y))
          NC = cv2.convexHull(c)
          cv2.drawContours(captura, [NC], 0, (255,0,0), 3)

      cv2.imshow('Original', captura)
      #cv2.imshow('Video',mask)

      if cv2.waitKey(1) & 0xFF == ord('s'):
        xf=len(x)-1
        x0=x[0]
        y0=y[0]
        x1=x[xf]
        y1=y[xf]
        imagen=np.zeros(captura.shape,dtype=np.uint8)
        imagen=cv2.line(imagen,(x0,y0),(x1,y1),(255,0,0),3)
        if ((x1-x0)is not 0):
          theta=float(math.atan((y0-y1)/(x1-x0))*180/3.14)
        else:
          theta=90
        print("Angulo de trayectoria: {}°".format(theta))
        cv2.imshow("Trayectoria",imagen)
        cv2.waitKey(0)
        break
  video.release()
  cv2.destroyAllWindows()

while True:
  lectura()
  Respuesta=input("Ingrese 1 para otra lectura: -->")
  if Respuesta!="1": break

print("Fin del programa")
