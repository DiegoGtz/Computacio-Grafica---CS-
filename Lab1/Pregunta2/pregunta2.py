import cv2 
import numpy as np
img  = cv2.imread("thresh2.png")
alto, ancho = img.shape[:2]
matriz3= np.array(img)
matriz = []
print alto, ancho
min, max = 130, 150
for y in range(0, alto):
	matriz.append([])
	for x in range(0,ancho):
		b = img.item(y, x, 0)
		g = img.item(y, x, 1)
		r = img.item(y, x, 2)
		if (b > 130 and b <165)  and (g > 130 and g <165 ) and (r > 130 and r <165):
			matriz[y].append(255)
		else:
			matriz[y].append(0)
matriz2 = np.array(matriz)
print matriz2
cv2.imwrite("thresh1OUT.jpg",matriz2)
cv2.imshow("img", matriz2)
cv2.waitKey(0)