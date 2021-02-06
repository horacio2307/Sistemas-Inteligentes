#Rivera Peña Juan Horacio
import cv2
import numpy as np
 
#Cargamos la imagen:
img = cv2.imread("Imagen.png")

img = cv2.resize(img, (0,0), fx=0.285, fy=0.2)
img2 = cv2.resize(img, (0,0), fx=0.75, fy=0.75)
img3 = cv2.resize(img, (0,0), fx=0.75, fy=0.75)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #Convertir a HSV
hsv2 = cv2.cvtColor(img3,cv2.COLOR_BGR2HSV)
rojos_min = np.array([75,100,100])
rojos_max = np.array([125,255,255])
verdes_min = np.array([30,100,100]) #Rojos bajos
verdes_max = np.array([70, 255, 255]) #Rojos altos

mask = cv2.inRange(hsv, verdes_min, verdes_max) #Detectamos los píxeles que estén dentro de los rangos:
img3 = cv2.inRange(hsv2,rojos_min,rojos_max)
img3 = cv2.Canny(img3,50,150)

# Detectamos los bordes con Canny
canny = cv2.Canny(mask, 50, 150)
gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
canny2 = cv2.Canny(gray, 10, 150)

#Encontramos los contornos
cnt = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)[0] 
cnts,_ = cv2.findContours(canny2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#Calculamos el Area
AreaRec=cv2.contourArea(cnt[0])*pow(40/117,2)
print("\nEl area del rectangulo es {} mm^2\n".format(AreaRec))

posiciones=[]
#Eliminamos los que no necesitamos
for c in cnts:
    #Calculamos el Area
    area=cv2.contourArea(c)
    if(area>100):
        posiciones.append(c)

#Imprimmimos los valores buenos
print("Circularidad de los elementos :")
for c in posiciones:
    #Calculamos el Area y perimetro
    area=cv2.contourArea(c)*pow(40/117,2)
    perimetro=cv2.arcLength(c,True)*40/117
    Circularidad=4*3.1415*area/perimetro/perimetro
    print("La circularidad es {}".format(Circularidad))

epsilon = 0.01*cv2.arcLength(cnts[4],True)
approx = cv2.approxPolyDP(cnts[4],epsilon,True)
_,_,w,h = cv2.boundingRect(approx)
aspect_ratio = float(w)/h
print("\naspect_ratio del Cuadrado",aspect_ratio)

cv2.imshow("Original",img)
cv2.imshow("Rectangulo", canny)
cv2.imshow("Figuras",canny2)
cv2.imshow("Cuadrado",img3)
cv2.waitKey(0)
cv2.destroyAllWindows()