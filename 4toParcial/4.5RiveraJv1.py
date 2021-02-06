#Rivera Peña Juan Horacio
import numpy as np
import cv2
from matplotlib import pyplot as plt

#Cargar la mascara
imagen = cv2.imread('5_img1.jpeg', cv2.IMREAD_GRAYSCALE)
original = cv2.imread('5_img1.jpeg')
kernel = np.ones((3,3),np.uint8)


#Se aplica la transformacion: Erode
imagen = cv2.erode(imagen,kernel,iterations = 6)

#Se aplica la transformacion: Dilate
imagen = cv2.dilate(imagen,kernel,iterations = 4)

#Se aplica la transformacion: Closing
imagen = cv2.morphologyEx(imagen,cv2.MORPH_CLOSE,kernel)

#Se aplica la transformacion: Erode
imagen = cv2.erode(imagen,kernel,iterations = 3)

#Se aplica la transformacion: Dilate
imagen = cv2.dilate(imagen,kernel,iterations = 1)

#Se aplica la transformacion: mediana
imagen = cv2.medianBlur(imagen,3) 

#Se aplica la transformacion: Erode
imagen = cv2.erode(imagen,kernel,iterations = 3) # 

#Se aplica la transformacion: Dilate
imagen = cv2.dilate(imagen,kernel,iterations = 10)

#Se aplica la transformacion: mediana
imagen = cv2.medianBlur(imagen,7) 

#Se aplica la transformacion: Dilate
imagen = cv2.dilate(imagen,kernel,iterations = 1)

#Se aplica la transformacion: Erode
imagen = cv2.erode(imagen,kernel,iterations = 8)

#Se aplica la transformacion: mediana
imagen = cv2.medianBlur(imagen,7) 

#umbralizacion
t, imagen= cv2.threshold(imagen, 130, 255, cv2.THRESH_BINARY)

#Se aplica la transformacion: mediana
Resultado = cv2.medianBlur(imagen,19) 

#Mostrar el resultado y salir
#cv2.imshow('x', imagen)
cv2.imshow('resultado', Resultado)
cv2.imshow('Original',original)
cv2.imwrite('4.5RiveraJv1.JPG',Resultado)
cv2.waitKey(0)
cv2.destroyAllWindows()