#Rivera Peña Juan Horacio
import cv2
import numpy as np
 
#Cargamos la imagen:
img = cv2.imread("2_figuras.png")

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #Convertir a HSV

red_min = np.array([5,100,100]) #Rojos bajos
red_max = np.array([20, 255, 255]) #Rojos altos
 
mask = cv2.inRange(hsv, red_min, red_max) #Detectamos los píxeles que estén dentro de los rangos:

#Crear un kernel de '1' de 3x3
kernel = np.ones((3,3),np.uint8)
 
#Se aplica la transformacion: Opening
mask = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)

#Detectamos los bordes con Canny
canny = cv2.Canny(mask, 50, 150)
 

cnts,_ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

perimetro=cv2.arcLength(cnts[0],True)
print("El perimetro es {}".format(perimetro))

#Calculamos el Area
area=cv2.contourArea(cnts[0])
print("El area es {}".format(area))

Circularidad=4*3.1415*area/perimetro/perimetro
print("La circularidad es",Circularidad)

cv2.imshow("original",img)
cv2.imshow("canny", canny)
cv2.waitKey(0)
cv2.destroyAllWindows()