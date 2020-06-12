from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from django.views.generic import CreateView
from django.core.files.storage import FileSystemStorage
from django.core.files.storage import Storage
from django.core.files.base import ContentFile

#####################################################

import cv2 
import numpy as np
from matplotlib import pyplot as plt 
import	 math 

def inicio(request):
    return render(request,'Home.html')

class Algoritmos ():


	def Thresholding(img1,min,max):
		imagen = img1
		img  = cv2.imread(imagen)
		alto, ancho = img.shape[:2]
		matriz3= np.array(img)
		matriz = []

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
		_toNP = np.array(matriz)
		salidaImg = "static/Thresholding" + imagen
		cv2.imwrite(salidaImg,_toNP)		
		return salidaImg


	def Outlier_Contrast_Stretching(img1, a,b, Low, High):
		imagen = img1 
		img  = cv2.imread(imagen,0)
		width, height = img.shape[:2]
		_w 			= width
		_h 			= height	
		_matriz 	= np.array(img)
		_matrizOUT 	= []
		_Paleta 	= [] 
		for y in range(0, _h):
			for x in range(0,_w):
				_token = _matriz[y][x]
				_Paleta.append(_token)		
		_Paleta.sort()
		c = _Paleta[int((_w*_h)*(Low/100.0))]
		d = _Paleta[int((_w*_h)*(High/100.0))]
		#print c, d
		_div =((b - a )/ (d - c )) 
		int(b)
		for y in range(0, _h):
			_matrizOUT.append([])
			for x in range(0,_w):
				_token2 = _matriz[y][x]	
				_resultado = (int(_token2) - int(c))*int(_div) + int(a)
				_matrizOUT[y].append(_resultado)

				if(_resultado > 255):
					_resultado = 255
				if(_resultado < 0 ):
					_resultado = 0
		_toNP = np.array(_matrizOUT)
		salidaImg = "static/Outlier_Contrast_Stretching" + imagen
		cv2.imwrite(salidaImg,_toNP)
		return salidaImg
	def Contrast_Stretching(img1,a , b ):
		imagen = img1 
		img  = cv2.imread(imagen,0)
		width, height = img.shape[:2]
		_w 			= width
		_h 			= height
		_matriz 	= np.array(img)
		_matrizOUT 	= []
		min, max 	= _matriz[0][0],_matriz[0][0]
		for y in range(0, _h):
			for x in range(0,_w):
				_token = _matriz[y][x] 	
				if(_token < min): 
					min = _token
				if(_token > max):
					max = _token
		c,d = min, max
		_div = (b - a )/ (d - c ) 
		for y in range(0, _h):
			_matrizOUT.append([])
			for x in range(0,_w):
				_token2 = _matriz[y][x]
				_resultado = (_token2 - c)*_div + a
				_matrizOUT[y].append(_resultado)
		_toNP = np.array(_matrizOUT)
		salidaImg = "static/Contrast_Stretching" + imagen
		cv2.imwrite(salidaImg,_toNP)
		return salidaImg
	def ecualizacion_histograma(img1):
		imagen = img1 
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
		for i in range(0,_L):
			_n.append(0);
		for y in range(0, _w):
			for x in range(0,_h):
				_token = _matriz[y][x]
				_n[_token] = _n[_token] + 1 
		_tmp3 = 0
		for n in range(0,_L):
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
		salidaImg = "static/ecualizacion_de_histograma" + imagen
		
		cv2.imwrite(salidaImg,Result)
		return salidaImg
	def operador_logaritmo(img1,c):
		imagen = img1 
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
		salidaImg = "static/operador_logaritmo100" + imagen
		cv2.imwrite(salidaImg,Result)
		return salidaImg
	def operador_Root(img1,c):
		imagen = img1
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
				_resultado = c*math.sqrt(_token2)
				if(_resultado < 0) : 
					_resultado = 0
				elif(_resultado > 255):
					_resultado = 255
				_matrizOUT[y].append(_resultado)
		Result = np.array(_matrizOUT)
		salidaImg = "static/operador_Root50" + imagen
		cv2.imwrite(salidaImg,Result)
		return salidaImg
	def operador_Raise_to_power(img1,c,r):
		imagen = img1 
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

		salidaImg = "static/operador_Raise_to_power"+ str(c) +'_'+ str(r)+ imagen
		
		cv2.imwrite(salidaImg,Result)
		return salidaImg
	def operador_Exponencial(img1,c,b):
		imagen = img1 
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
				_resultado = c*(math.pow(b ,_token2)-1)
				if(_resultado < 0) : 
					_resultado = 0
				elif(_resultado > 255):
					_resultado = 255
				_matrizOUT[y].append(_resultado)
		Result = np.array(_matrizOUT)
		salidaImg = "static/operador_Exponencial"+ str(c) +'_'+ str(b)+ imagen
		cv2.imwrite(salidaImg,Result)
		return salidaImg

	def pixel_adition(imagen1,imagen2):
		img1 = cv2.imread(imagen1)
		img2 = cv2.imread(imagen2)
		img1 = img1.astype(int)
		img2 = img2.astype(int)

		alto1,ancho1 = img1.shape[:2]
		alto2,ancho2 = img2.shape[:2]
		
		print(alto1,' ',ancho1)
		print(alto2,' ',ancho2)
		alto = 0
		ancho = 0

		if alto1<alto2:
			alto=alto1
		else:
			alto=alto2
		if ancho1<ancho2:
			ancho=ancho1
		else:
			ancho=ancho2

		for i in range(alto):
			for j in range(ancho):
				img1[i][j][0] = img1[i][j][0]/2+img2[i][j][0]/2
				img1[i][j][1] = img1[i][j][1]/2+img2[i][j][1]/2
				img1[i][j][2] = img1[i][j][2]/2+img2[i][j][2]/2

				img1[i][j][0] = img1[i][j][0] + 20
				img1[i][j][1] = img1[i][j][1] + 20
				img1[i][j][2] = img1[i][j][2] + 20
		
		salidaImg = "static/Adition.jpg"
		cv2.imwrite(salidaImg,img1)
		return salidaImg

	def pixel_sustraction(imagen1,imagen2):
		img1 = cv2.imread(imagen1,0)
		img2 = cv2.imread(imagen2,0)
		img1 = img1.astype(int)
		img2 = img2.astype(int)
		alto1,ancho1 = img1.shape
		alto2,ancho2 = img2.shape
		if alto1<alto2:
			alto=alto1
		else:
			alto=alto2
		if ancho1<ancho2:
			ancho=ancho1
		else:
			ancho=ancho2
		for i in range(alto1):
			for j in range(ancho1):
				img1[i][j] = abs(img2[i][j]-img1[i][j])
				img1[i][j]=img1[i][j]+105
		img_out=img1
		for i in range(alto):
		    for j in range(ancho):
		        if ( 70 < img1[i,j] and img1[i,j] < 130):
		            img_out[i,j]=255
		        else:
		            img_out[i,j]=0

		salidaImg1 = "static/prueba_salida.png" +imagen1 
		cv2.imwrite(salidaImg1,img_out)
		return salidaImg1

	def multiplication(imagen1,c):
		img1 = cv2.imread(imagen1)

		img1 = img1.astype(int)

		alto1,ancho1 = img1.shape[:2]
		
		for i in range(alto1):
			for j in range(ancho1):

				img1[i][j][0] = img1[i][j][0] * c
				img1[i][j][1] = img1[i][j][1] * c
				img1[i][j][2] = img1[i][j][2] * c

		salidaImg = "static/MultiplicacionOUT" + imagen1
		cv2.imwrite(salidaImg,img1)
		return salidaImg
	def blending(imagen1,imagen2,x):
		img1 = cv2.imread(imagen1)
		img2 = cv2.imread(imagen2)
		img1 = img1.astype(float)
		img2 = img2.astype(float)

		alto1,ancho1 = img1.shape[:2]
		alto2,ancho2 = img2.shape[:2]
		
		alto = 0
		ancho = 0

		if alto1<alto2:
			alto=alto1
		else:
			alto=alto2
		if ancho1<ancho2:
			ancho=ancho1
		else:
			ancho=ancho2

		for i in range(alto):
			for j in range(ancho):
				img1[i][j][0] = (x * img1[i][j][0]/2)+((1-x)*img2[i][j][0]/2)
				img1[i][j][1] = (x * img1[i][j][1]/2)+((1-x)*img2[i][j][1]/2)
				img1[i][j][2] = (x * img1[i][j][2]/2)+((1-x)*img2[i][j][2]/2)

		salidaImg = "static/Blending" + imagen1 + imagen2
		cv2.imwrite(salidaImg,img1)
		return salidaImg

	def pixel_division(imagen1,imagen2):
		print (imagen1,imagen2)
		img1 = cv2.imread(imagen1,0)
		img2 = cv2.imread(imagen2,0)
		alto,ancho = img1.shape

		for i in range(alto):
			for j in range(ancho):
				img1[i][j] = (img1[i][j]/img2[i][j])*30

		newMin=0
		newMax=255
		mini=0
		maxi=30
		for i in range(alto):
			for j in range(ancho):
				img1[i][j] = (img1[i][j]-mini)*((newMax-newMin)/(maxi-mini))+newMin

		img_out=img1
		for i in range(alto):
		    for j in range(ancho):
		        #if (img[i][j]<130):
		        if ( 50 < img1[i,j] and img1[i,j] < 215):
		            img_out[i,j]=255
		        else:
		            img_out[i,j]=0


		salidaImg = "static/Div" + imagen1 + imagen2
		cv2.imwrite(salidaImg,img_out)
		return salidaImg
	def Thresholding1(img1, alto, ancho ):
		img_out=img1
		for i in range(alto):
			for j in range(ancho):
			    if ( 0< img1[i,j] and img1[i,j] < 150):
			        img_out[i,j]=255
			    else:
			        img_out[i,j]=0
		return img_out
	def Ope_Logicos(imagen1,imagen2,operador):
		img1 = cv2.imread(imagen1,0)
		img2 = cv2.imread(imagen2,0)
		img1 = img1.astype(int)
		img2 = img2.astype(int)
		alto1,ancho1 = img1.shape
		alto2,ancho2 = img2.shape

		print (alto1, alto2)
		############################################
		T_img1 = Algoritmos.Thresholding1(img1,alto1,ancho1)
		T_img2 = Algoritmos.Thresholding1(img2,alto2,ancho2)
		  #cv2.imwrite('t_img1.png',T_img1)
		  #cv2.imwrite('t_img2.png',T_img2)
		###########################################
		for i in range(alto1):
		  for j in range(ancho1):

		  	if(operador == "AND"):
		  		token = np.bitwise_and(T_img1[i][j],T_img2[i][j])
		  	elif(operador == "OR"):
		  		token = np.bitwise_or(T_img1[i][j],T_img2[i][j])
		  	elif(operador =="XOR"):
		  		token = np.bitwise_xor(T_img1[i][j],T_img2[i][j])
		  	if(token < 0):
		  		token = 0
		  	elif(token > 255):
		  		token = 255
		  	img1[i][j] = token

		salidaImg = "static/MultiplicacionOUT" + imagen1  
		cv2.imwrite(salidaImg,img1)
		return salidaImg

class Operadores():
	def inicio(request):
		return render(request,'Home.html')
		
	def PageOperador(request):
		tipo = request.POST['fase']
		if(tipo == "Thresholding"):
			return render(request,'Thresholding.html',{"labels":tipo})
		elif(tipo == "Outlier_C.Stretching"):
			return render(request,'Outlier_Contrast_Stretching.html',{"labels":tipo})	
		elif(tipo == "Contrast_stretching"):
			return render(request,'Contrast_stretching.html',{"labels":tipo})		
		elif(tipo == "E.Histograma"):
			return render(request,'Ecualizacion_Histograma.html',{"labels":tipo})
		elif(tipo == "O.Logaritmico"):
			return render(request,'PageOperador.html',{"labels":tipo})
		elif(tipo == "O.Raiz"):
			return render(request,'PageOperador.html',{"labels":tipo})
		elif(tipo == "O.Exponencial"):
			return render(request,'Operador_Exponencial.html',{"labels":tipo})	
		elif(tipo == "O.RaiseToPower"):
			return render(request,'RaiseToPower.html',{"labels":tipo})
		elif(tipo == "Cascada"):
			return render(request,'Cascada.html',{"labels":tipo})		
		elif(tipo == "Add"):
			return render(request,'Addition.html',{"labels":tipo})	
		elif(tipo == "Subtraction"):
			return render(request,'Subtraction.html',{"labels":tipo})	
		elif(tipo == "Multiplicacion" ):
			return render(request,'Multiplicacion.html',{"labels":tipo})
		elif(tipo == "Blending" ):
			return render(request,'Blending.html',{"labels":tipo})
		elif(tipo == "Division" ):
			return render(request,'Division.html',{"labels":tipo})
		elif(tipo == "AND" ):
			return render(request,'OperadoresLogicos.html',{"labels":tipo})
		elif(tipo == "OR" ):
			return render(request,'OperadoresLogicos.html',{"labels":tipo})
		elif(tipo == "XOR" ):
			return render(request,'OperadoresLogicos.html',{"labels":tipo})

	def ControladorOperador(request):

		#id = request.POST['fase']
		tipo = request.POST['Tipo']
		myfile = request.FILES["file1"]
		#myfile2 = request.FILES["file2"]
		#print(myfile,myfile2)
		fs = FileSystemStorage()
		#fs2 = FileSystemStorage()
		filename = fs.save(myfile.name, myfile)
		#filename2 = fs2.save(myfile2.name, myfile2)
		file_name = fs.url(filename)
		#file_name2 = fs2.url(filename2)

		#print(file_name,file_name2)
		if(tipo == "Thresholding"):
			min1 = request.POST['min']
			max2 = request.POST['max']			
			resultado =  Algoritmos.Thresholding(file_name,int(min1),int(max2))
			return render(request,'ResulTOperador.html',{"labels2":tipo,"image":"/"+resultado} )

		if(tipo == "Outlier_C.Stretching"):
			a = request.POST['a']
			b = request.POST['b']
			Low = request.POST['Low']
			Max = request.POST['Max']
			resultado = Algoritmos.Outlier_Contrast_Stretching(file_name,int(a),int(b),int(Low),int(Max))

			return render(request,'ResulTOperador.html',{"labels2":tipo,"image":"/"+resultado} )
		if(tipo == "Contrast_stretching"):
			a = request.POST['a']
			b = request.POST['b']
			resultado = Algoritmos.Contrast_Stretching(file_name,int(a),int(b))

			return render(request,'ResulTOperador.html',{"labels2":tipo,"image":"/"+resultado} )

		if(tipo == "E.Histograma"):
			resultado = Algoritmos.ecualizacion_histograma(file_name)

			return render(request,'ResulTOperador.html',{"labels2":tipo,"image":"/"+resultado} )
		if(tipo == "O.Logaritmico"):
			c = request.POST['c']
			resultado = Algoritmos.operador_logaritmo(file_name,int(c))

			return render(request,'ResulTOperador.html',{"labels2":tipo,"image":"/"+resultado} )

		if(tipo == "O.Raiz"):
			c = request.POST['c']
			resultado = Algoritmos.operador_Root(file_name,int(c))

			return render(request,'ResulTOperador.html',{"labels2":tipo,"image":"/"+resultado} )
		if(tipo == "O.Exponencial"):
			c = request.POST['c']
			b = request.POST['b']
			
			resultado = Algoritmos.operador_Exponencial(file_name,float(c),float(b))
			return render(request,'ResulTOperador.html',{"labels2":tipo,"image":"/"+resultado} )	
		if(tipo == "O.RaiseToPower"):
			c = request.POST['c']
			r = request.POST['r']
			
			resultado = Algoritmos.operador_Raise_to_power(file_name,float(c),float(r))
			return render(request,'ResulTOperador.html',{"labels2":tipo,"image":"/"+resultado} )
		if(tipo == "Cascada"):

			a,b = 0 , 255 
			Resultado1 =  Algoritmos.Contrast_Stretching(file_name,a,b)
			Resultado2 = Algoritmos.ecualizacion_histograma(file_name)
			c = 70 
			Resultado3 = Algoritmos.operador_logaritmo(file_name,c)
			c =20
			Resultado4 = Algoritmos.operador_Root(file_name,c)
			c,b = 20 , 1.01
			Resultado5 = Algoritmos.operador_Exponencial(file_name,c,b)
			c, r = 0.1 , 1.5
			Resultado6 = Algoritmos.operador_Raise_to_power(file_name,c,r)

			return render(request,'Resultado_Cascada.html',{"labels2":tipo,
				"image":"/"+Resultado1,
				"image2":"/"+Resultado2,
				"image3":"/"+Resultado3,
				"image4":"/"+Resultado4,
				"image5":"/"+Resultado5,
				"image6":"/"+Resultado6,
				} )		


		if (tipo == "Add"):
			#return render(request,'Home.html')
			myfile2 = request.FILES["file2"]
			fs2 = FileSystemStorage()
			filename2 = fs2.save(myfile2.name, myfile2)
			file_name2 = fs2.url(filename2)
			resultado = Algoritmos.pixel_adition(file_name,file_name2)
		
			return render(request,'ResulTOperador.html',{"labels2":tipo,"image":"/"+resultado} )
		if (tipo == "Subtraction"):
			myfile2 = request.FILES["file2"]
			fs2 = FileSystemStorage()
			filename2 = fs2.save(myfile2.name, myfile2)
			file_name2 = fs2.url(filename2)
			resultado = Algoritmos.pixel_sustraction(file_name,file_name2)
			
			return render(request,'ResulTOperador.html',{"labels2":tipo,"image":"/"+resultado} )
		if (tipo == "Multiplicacion"):
			c = request.POST['c']
			resultado = Algoritmos.multiplication(file_name,int(c))
		
			return render(request,'ResulTOperador.html',{"labels2":tipo,"image":"/"+resultado} )
		if (tipo == "Blending"):
			#return render(request,'Home.html')
			x = request.POST['x']
			myfile2 = request.FILES["file2"]
			fs2 = FileSystemStorage()
			filename2 = fs2.save(myfile2.name, myfile2)
			file_name2 = fs2.url(filename2)
			resultado = Algoritmos.blending(file_name,file_name2,float(x))
			return render(request,'ResulTOperador.html',{"labels2":tipo,"image":"/"+resultado} )
		if (tipo == "Division"):
			#return render(request,'Home.html')
			myfile2 = request.FILES["file2"]
			fs2 = FileSystemStorage()
			filename2 = fs2.save(myfile2.name, myfile2)
			file_name2 = fs2.url(filename2)
			resultado = Algoritmos.pixel_division(file_name,file_name2)
		
			return render(request,'ResulTOperador.html',{"labels2":tipo,"image":"/"+resultado} )

		if (tipo == "AND"):
			#return render(request,'Home.html')
			myfile2 = request.FILES["file2"]
			fs2 = FileSystemStorage()
			filename2 = fs2.save(myfile2.name, myfile2)
			file_name2 = fs2.url(filename2)

			resultado = Algoritmos.Ope_Logicos(file_name,file_name2,tipo)
		
			return render(request,'ResulTOperador.html',{"labels2":tipo,"image":"/"+resultado} )
		if (tipo == "OR"):
			#return render(request,'Home.html')
			myfile2 = request.FILES["file2"]
			fs2 = FileSystemStorage()
			filename2 = fs2.save(myfile2.name, myfile2)
			file_name2 = fs2.url(filename2)
			resultado = Algoritmos.Ope_Logicos(file_name,file_name2,tipo)
		
			return render(request,'ResulTOperador.html',{"labels2":tipo,"image":"/"+resultado} )
		if (tipo == "XOR"):
			#return render(request,'Home.html')
			myfile2 = request.FILES["file2"]
			fs2 = FileSystemStorage()
			filename2 = fs2.save(myfile2.name, myfile2)
			file_name2 = fs2.url(filename2)
			resultado = Algoritmos.Ope_Logicos(file_name,file_name2,tipo)
		
			return render(request,'ResulTOperador.html',{"labels2":tipo,"image":"/"+resultado} )

		return render(request,'Home.html')



	