import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('thresh1.png',0)
hist = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.plot(hist, color='gray' )

plt.xlabel('intensidad de iluminacion')
plt.ylabel('cantidad de pixeles')
plt.show()
cv2.destroyAllWindows()
