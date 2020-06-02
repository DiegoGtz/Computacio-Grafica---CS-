import math
import cv2 
import numpy as np
from matplotlib import pyplot as plt


def pixel_sustraction(imagen1,imagen2):
  img1 = cv2.imread(imagen1,0)
  img2 = cv2.imread(imagen2,0)
  img1 = img1.astype(int)
  img2 = img2.astype(int)
  alto1,ancho1 = img1.shape
  alto2,ancho2 = img2.shape

  for i in range(alto1):
    for j in range(ancho1):

      token = abs(img2[i][j]-img1[i][j])

      if (token == 0):
        img1[i][j] = 0
        
      else:
        img1[i][j] = token
        
  cv2.imwrite('prueba_salida_sub111.jpg',img1)


def Outlier_Contrast_Stretching(img1, a,b, Low, High):
    imagen = img1 
    img  = cv2.imread(imagen,0)
    width, height = img.shape[:2]
    _w      = width-1
    _h      = height-1 
    _matriz   = np.array(img)
    _matrizOUT  = []
    _Paleta   = []
    for y in range(0, _w):
      for x in range(0,_h):
        _token = _matriz[y][x]
        _Paleta.append(_token)    
    _Paleta.sort()
    c = _Paleta[int((_w*_h)*(Low/100.0))]
    d = _Paleta[int((_w*_h)*(High/100.0))]
    #print c, d
    _div =((b - a )/ (d - c )) 
    int(b)
    for y in range(0, _w):
      _matrizOUT.append([])
      for x in range(0,_h):
        _token2 = _matriz[y][x] 
        _resultado = (int(_token2) - int(c))*int(_div) + int(a)
        _matrizOUT[y].append(_resultado)

        if(_resultado > 255):
          _resultado = 255
        if(_resultado < 0 ):
          _resultado = 0
    _toNP = np.array(_matrizOUT)
    salidaImg = "Outlier_Contrast_Stretching" + imagen
    cv2.imwrite(salidaImg,_toNP)


pixel_sustraction('sub_11.jpg','sub_10.jpg')

imagen = 'prueba_salida_sub.jpg'
a,b = 0, 255
Outlier_Contrast_Stretching(imagen, a,b, 5, 95)
