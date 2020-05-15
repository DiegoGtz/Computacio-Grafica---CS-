import cv2 
import numpy as np
from matplotlib import pyplot as plt 
import	 math 

def operador_logaritmo(img1,c):
	imagen = img1 + ".jpg"
	img  = cv2.imread(imagen,0)
	width, height = img.shape[:2]
	_w 			= width
	_h 			= height	
	_matriz 	= np.array(img)
	_matrizOUT 	= []
	_n	= [] 

	for y in range(0, _w):
		_matrizOUT.append([])
		for x in range(0,_h):
			_token2 = _matriz[y][x]
			_resultado = c* math.log(1 + _token2, 10)
			_matrizOUT[y].append(_resultado)
	Result = np.array(_matrizOUT)
	salidaImg = "operador_logaritmo100" + imagen
	print salidaImg
	cv2.imwrite(salidaImg,Result)
		
if __name__ == "__main__":
	imagen = 'log_1'
	#c = 40
	#c = 30
	c = 70
	#c = 90
	#c = 98
	#c = 30
	#c = 100
	#c = 105
	#c = 150
	#c = 180

	operador_logaritmo(imagen,c)
