#Rivera Peña Juan Horacio
import cv2
import numpy as np
 
#Cargamos la imagen:
img = cv2.imread("2_figuras.png")

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #Convertir a HSV

verdes_min = np.array([30,100,100]) #Rojos bajos
verdes_max = np.array([70, 255, 255]) #Rojos altos

mask = cv2.inRange(hsv, verdes_min, verdes_max) #Detectamos los píxeles que estén dentro de los rangos:

# Detectamos los bordes con Canny
canny = cv2.Canny(mask, 50, 150)
cv2.imshow("canny", canny)

#Encontramos los contornos
cnt = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)[0] 
#Calculamos el Area
area=cv2.contourArea(cnt[0])
print("El area es {} pixeles cuadrados".format(area))

cv2.imshow("original",img)
cv2.imshow("canny", canny)
cv2.waitKey(0)
cv2.destroyAllWindows()