import cv2
import sys

img = cv2.imread('openPic.jpg',0)
cv2.imshow('Curso de OpenCV',img)

def cerrarVentana():
    cv2.destroyAllWindows()
    sys.exit()
k = cv2.waitKey(0)
if k == 27:
    cerrarVentana()