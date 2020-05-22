import math
import cv2 
import numpy as np
from matplotlib import pyplot as plt

def operador_raiz(c,b):
	img = cv2.imread("exp_5.jpg",0)
	print (img.shape)
	alto,ancho = img.shape

	print(alto,' << ',ancho)

	_matriz = np.array(img)
	_new_matriz = _matriz

	#for i in range(alto):
		#for j in range(ancho):
			#_new_matriz = c*(math.pow(b,_matriz)-1)
			
	_new_matriz = c*(math.pow(b,_matriz)-1)

	cv2.imwrite("exp5_"+str(c)+".jpg", _new_matriz)
	cv2.imshow('nueva.jpg', _new_matriz)

if __name__ == "__main__":
	operador_raiz(20,1.01)
