#Computacion Grafica- UNSA
#Laboratorio2
#Contrast Stretching

import cv2 
import numpy as np
from matplotlib import pyplot as plt
from math import floor
#####################################


def Histograma(imagen):
	img = cv2.imread(imagen ,0)
	hist = cv2.calcHist([img], [0], None, [256], [0, 256])
	plt.plot(hist, color='gray' )

	plt.xlabel('intensidad de iluminacion')
	plt.ylabel('cantidad de pixeles')
	plt.show()
	cv2.destroyAllWindows()	


def Outlier_Contrast_Stretching(img, width, height, a,b, Low, High):
	_w 			= width
	_h 			= height	
	_matriz 	= np.array(img)
	_matrizOUT 	= []
	_Paleta 	= [] 
	for y in range(0, _h):
		for x in range(0,_w):
			_token = _matriz[y][x]
			_Paleta.append(_token)		
	_Paleta.sort()
	 
	c = _Paleta[int((_w*_h)*(Low/100.0))]
	d = _Paleta[int((_w*_h)*(High/100.0))]
	#print c, d

	_div =((b - a )/ (d - c )) 
	print (_div)
	int(b)

	for y in range(0, _h):
		_matrizOUT.append([])
		for x in range(0,_w):
			_token2 = _matriz[y][x]	
			_resultado = (int(_token2) - int(c))*int(_div) + int(a)
			_matrizOUT[y].append(_resultado)

			if(_resultado > 255):
				_resultado = 255
			if(_resultado < 0 ):
				_resultado = 0
	_toNP = np.array(_matrizOUT)
	cv2.imwrite("Outlier_Contrast_Stretching7.jpg",_toNP)

if __name__ == "__main__":
    
	#Obtenemos el Histograma de la imagen
	imagen = 'contr2.jpg'
	#Histograma(imagen)

	#Stretching 
	a,b = 0, 255


	img  = cv2.imread(imagen,0)


	
	#Histograma('Contrast_Stretching.jpg')

	#Add_Outliers(img, 0 ,0 ,9)

	Constrast = 'Add_Outliers.jpg'

	img2  = cv2.imread(Constrast,0)
	width2, height2 = img2.shape[:2]
	lowpercent,highpercent = 5,95
	Outlier_Contrast_Stretching(img2,width2,height2,a,b,lowpercent,highpercent)