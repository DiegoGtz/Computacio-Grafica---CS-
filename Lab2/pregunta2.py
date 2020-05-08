import cv2 
import numpy as np
from matplotlib import pyplot as plt
from math import floor
def Histograma(imagen):
	img = cv2.imread(imagen ,0)
	hist = cv2.calcHist([img], [0], None, [256], [0, 256])
	plt.plot(hist, color='gray' )

	plt.xlabel('intensidad de iluminacion')
	plt.ylabel('cantidad de pixeles')
	plt.show()
	cv2.destroyAllWindows()	
def Add_Outliers(img,x,y,_tam):
	_matriz = np.array(img)
	x,y = _matriz[x],_matriz[y]
	cout = 0
	for y in  range(0,_tam):
		for x in range(0,_tam):
			_matriz[x][y] = 0 
			cout += 1 
	cv2.imwrite("Add_Outliers.jpg",_matriz)

if __name__ == "__main__":
    
	imagen = 'contr2.jpg'
	a,b = 0, 255
	img  = cv2.imread(imagen,0)

	Histograma('Contrast_Stretching.jpg')
	Add_Outliers(img, 0 ,0 ,9)
	Constrast = 'Add_Outliers.jpg'