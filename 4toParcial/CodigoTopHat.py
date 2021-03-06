import numpy as np
import cv2
 
#Cargar la mascara
imagen = cv2.imread('mask.png',0)
 
#Crear un kernel de '1' de 3x3
kernel = np.ones((9,9),np.uint8)
 
#Se aplica la transformacion: Top Hat
transformacion = cv2.morphologyEx(imagen,cv2.MORPH_TOPHAT,kernel)
 
#Mostrar el resultado y salir
cv2.imshow('resultado',transformacion)
cv2.waitKey(0)
cv2.destroyAllWindows()
