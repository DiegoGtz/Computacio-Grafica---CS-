import cv2 
import numpy as np
from matplotlib import pyplot as plt 
from math import floor 

def Histograma(imagen1):
	imagen = imagen1 + ".jpg"
	img = cv2.imread(imagen ,0)
	hist = cv2.calcHist([img], [0], None, [256], [0, 256])
	plt.plot(hist, color='gray' )

	plt.xlabel('intensidad de iluminacion')
	plt.ylabel('cantidad de pixeles')
	plt.show()
	cv2.destroyAllWindows()	

"""def ecualizacion_histograma(img1 ):
	imagen = img1 + ".jpg"
	img  = cv2.imread(imagen,0)
	width, height = img.shape[:2]
	_w 			= width
	_h 			= height	
	_matriz 	= np.array(img)
	_matrizOUT 	= []
	_n	= [] 
	_pix = width*height
	_L = 256
	for i in xrange(0,_L-1):
		_n.append(0);
	for y in range(0, _w):
		for x in range(0,_h):
			_token = _matriz[y][x]
			_n[_token] = _n[_token] + 1 
	for y in range(0, _w):
		_matrizOUT.append([])
		for x in range(0,_h):
			_token2 = _matriz[y][x]
			_tmp3 = 0
			for i in xrange(0,_token2+1):
				_tmp = float(_n[i])
				_tmp2 = float(_pix)
				_tmp3 = _tmp3 + (_tmp/_tmp2)
			newColor = int(_tmp3*(_L-1))
			_matrizOUT[y].append(newColor)
	Result = np.array(_matrizOUT)
	salidaImg = "ecualizacion_de_histograma" + imagen
	print salidaImg
	cv2.imwrite(salidaImg,Result)"""

def ecualizacion_histograma2(img1 ):
	imagen = img1 + ".jpg"
	img  = cv2.imread(imagen,0)
	width, height = img.shape[:2]
	_w 			= width
	_h 			= height	
	_matriz 	= np.array(img)
	_matrizOUT 	= []
	_n	= [] 
	_pix = width*height
	_L = 256
	_S = dict()
	for i in xrange(0,_L):
		_n.append(0);
	for y in range(0, _w):
		for x in range(0,_h):
			_token = _matriz[y][x]
			_n[_token] = _n[_token] + 1 
	_tmp3 = 0
	for n in xrange(0,_L):
		_tmp = float(_n[n])
		_tmp2 = float(_pix)
		_tmp3 = _tmp3 + (_tmp/_tmp2)		
		_res = int(_tmp3*(_L-1))
		_S[n] = _res
	for y in range(0, _w):
		_matrizOUT.append([])
		for x in range(0,_h):
			_token2 = _matriz[y][x]
			newColor = _S[_token2]
			_matrizOUT[y].append(newColor)
	Result = np.array(_matrizOUT)
	salidaImg = "ecualizacion_de_histograma" + imagen
	print salidaImg
	cv2.imwrite(salidaImg,Result)	
if __name__ == "__main__":
	imagen = 'ecualizacion_de_histogramaOUT'	
	#ecualizacion_histograma2(imagen)
	Histograma(imagen)