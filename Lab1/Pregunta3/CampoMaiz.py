import cv2 
import numpy as np
img  = cv2.imread("thresh3.png")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
alto, ancho =474,696 
matriz3= np.array(img)
matriz = []
print alto, ancho
for y in range(0, alto):
	matriz.append([])
	for x in range(0,ancho):
		b = hsv.item(y, x, 0)
		g = hsv.item(y, x, 1)
		r = hsv.item(y, x, 2)
		if  (b > 16 and b < 30 ) and (g > 76 and g <255 ) or (r >72 and r <210):
			matriz[y].append(0)
		else:
			matriz[y].append(255)
matriz2 = np.array(matriz)
print matriz2
cv2.imwrite("thresh3OUT.jpg",matriz2)
cv2.imshow("img", matriz2)
cv2.waitKey(0)