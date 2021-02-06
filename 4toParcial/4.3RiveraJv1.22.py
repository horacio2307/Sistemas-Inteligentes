#Rivera Peña Juan Horacio
import cv2
import numpy as np
 
#Cargamos la imagen:
img = cv2.imread("2_figuras.png")

#Detectamos los bordes con Canny
canny = cv2.Canny(img, 50, 150)

#Crear un kernel de '1' de 3x3
kernel = np.ones((3,3),np.uint8)
 
#Se aplica la transformacion: Opening
canny = cv2.morphologyEx(canny,cv2.MORPH_CLOSE,kernel)
 
cnts,_ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for c in cnts:
    perimetro=cv2.arcLength(c,True)
    print("\nEl perimetro es {}".format(perimetro))

    #Calculamos el Area
    area=cv2.contourArea(c)
    print("El area es {}".format(area))

    Circularidad=4*3.1415*area/perimetro/perimetro
    print("La circularidad es",Circularidad)

cv2.imshow("original",img)
cv2.imshow("canny", canny)
cv2.waitKey(0)
cv2.destroyAllWindows()