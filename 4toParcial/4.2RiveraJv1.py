#Rivera Peña Juan Horacio
import cv2
import numpy as np
 
#Cargamos la imagen:
img = cv2.imread("2_figuras.png")
 
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #Convertir a HSV
 
red_min = np.array([5,100,100]) #Rojos bajos
red_max = np.array([20, 255, 255]) #Rojos altos
 
mask = cv2.inRange(hsv, red_min, red_max) #Detectamos los píxeles que estén dentro de los rangos:

cv2.imshow("Original", img)
cv2.imshow("MascaraRojo", mask)
 
cv2.waitKey(0)
