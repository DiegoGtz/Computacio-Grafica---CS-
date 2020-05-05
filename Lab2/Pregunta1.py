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

def  Contrast_Stretching(img,width, height ,a , b ):
	_w = width
	_h = height

	_matriz = np.array(img)
	_matrizOUT = []

	min, max = _matriz[0][0],_matriz[0][0]

	for y in range(0, _h):
		for x in range(0,_w):
			_token = _matriz[y][x] 	
			if(_token < min): 
				min = _token
			if(_token > max):
				max = _token

	c,d = min, max


	#Aplicando la Formula 
	#(F[x,y] - c)*(b-a)/(d-c) + a

	# (b-a) /(d-c)
	_div = (b - a )/ (d - c ) 


	#Aplicando la formula en cada F[x,y]

	for y in range(0, _h):
		_matrizOUT.append([])
		for x in range(0,_w):
			_token2 = _matriz[y][x]
			_resultado = (_token2 - c)*_div + a
			_matrizOUT[y].append(_resultado)
	_toNP = np.array(_matrizOUT)
	cv2.imwrite("Contrast_Stretching.jpg",_toNP)
		



if __name__ == "__main__":
    
	#Obtenemos el Histograma de la imagen
	imagen = 'contr2.jpg'
	#Histograma(imagen)

	#Stretching 
	a,b = 0, 255

	img  = cv2.imread(imagen,0)
	width, height = img.shape[:2]


	Contrast_Stretching(img,width,height,a,b)