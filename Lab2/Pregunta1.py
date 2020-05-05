#Computacion Grafica- UNSA
#Laboratorio2
#Contrast Stretching

import cv2 
import numpy as np
from matplotlib import pyplot as plt
#####################################



def Histograma(imagen):
	img = cv2.imread(imagen ,0)
	hist = cv2.calcHist([img], [0], None, [256], [0, 256])
	plt.plot(hist, color='gray' )

	plt.xlabel('intensidad de iluminacion')
	plt.ylabel('cantidad de pixeles')
	plt.show()
	cv2.destroyAllWindows()	

def  Contrast_Stretching(width, height ,a , b ):
	_w = width
	_h = height



	print (_w +1 ,_h, a,b )



if __name__ == "__main__":
    
	#Obtenemos el Histograma de la imagen
	imagen = 'contr2.jpg'
	Histograma(imagen)

	#Stretching 
	a,b = 0, 255

	img  = cv2.imread(imagen,0)
	width, height = img.shape[:2]


	Contrast_Stretching(width,height,a,b)