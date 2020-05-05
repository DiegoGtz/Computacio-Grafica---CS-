import cv2 
import numpy as np
img  = cv2.imread("thresh1.PNG")
print img.shape
alto, ancho = img.shape[:2]
matriz3= np.array(img)
print matriz3
matriz = []
print alto, ancho
min, max =120, 160
for y in range(0, alto):
	matriz.append([])
	for x in range(0,ancho):
		b = img.item(y, x, 0)
		g = img.item(y, x, 1)
		r = img.item(y, x, 2)
		if (b > min and b <max)  and (g > min and g <max ) and (r > min and r <max):
			matriz[y].append(255)#Blanco
		else:
			matriz[y].append(0)#Negro
matriz2 = np.array(matriz)
print matriz2
cv2.imwrite("thresh1OUT.jpg",matriz2)
