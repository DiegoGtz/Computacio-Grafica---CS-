import cv2 
import numpy as np
from matplotlib import pyplot as plt 
import	 math 

def operador_Raise_to_power(img1,c,r):
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
			_resultado = c*math.pow(_token2,r)

			if(_resultado < 0) : 
				_resultado = 0
			elif(_resultado > 255):
				_resultado = 255
			_matrizOUT[y].append(_resultado)
	Result = np.array(_matrizOUT)

	salidaImg = "perador_Raise_to_power"+ str(c) +'_'+ str(r)+ imagen
	print salidaImg
	cv2.imwrite(salidaImg,Result)

if __name__ == "__main__":
	imagen = 'exp_5'
	#c, r = 0.1, 1.5
	#c,r = 0.05, 1.5
	#c,r = 0.01, 1.5
	#c,r = 1 , 0.9
	c,r = 0.5 , 0.9
	operador_Raise_to_power(imagen,c,r)