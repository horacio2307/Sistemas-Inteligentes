#Rivera Peña Juan Horacio
import cv2
import numpy as np
 
#Cargamos la imagen:
img = cv2.imread("2_figuras.png")

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #Convertir a HSV

blue_min = np.array([60,100,100]) #Rojos bajos
blue_max = np.array([120, 255, 255]) #Rojos altos
 
canny = cv2.inRange(hsv, blue_min, blue_max) #Detectamos los píxeles que estén dentro de los rangos:

canny = cv2.dilate(canny, None, iterations=1)
canny = cv2.erode(canny, None, iterations=1)


#Detectamos los bordes con Canny
canny = cv2.Canny(canny, 50, 150)
 
cnts,_ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
epsilon = 0.01*cv2.arcLength(cnts[0],True)
approx = cv2.approxPolyDP(cnts[0],epsilon,True)
_,_,w,h = cv2.boundingRect(approx)
aspect_ratio = float(w)/h
print("aspect_ratio ",aspect_ratio)

cv2.imshow("original",img)
cv2.imshow("canny", canny)
cv2.waitKey(0)
cv2.destroyAllWindows()