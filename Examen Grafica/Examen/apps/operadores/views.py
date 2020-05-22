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
				#print(c,_token2)
				_resultado = c*math.sqrt(_token2)
				#print(_resultado)
				if(_resultado < 0) : 
					_resultado = 0
				elif(_resultado > 255):
					_resultado = 255
				_matrizOUT[y].append(_resultado)
		Result = np.array(_matrizOUT)
		#print(Result)
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


class Operadores():

		
	def PageOperador(request):
		tipo = request.POST['fase']
		if(tipo == "O.Logaritmico"):
			return render(request,'PageOperador.html',{"labels":tipo})

		if(tipo == "O.Raiz"):
			return render(request,'PageOperador.html',{"labels":tipo})
		if(tipo == "O.Exponencial"):
			return render(request,'Operador_Exponencial.html',{"labels":tipo})	
		if(tipo == "O.RaiseToPower"):
			return render(request,'RaiseToPower.html',{"labels":tipo})
	
	



	def ControladorOperador(request):

		#id = request.POST['fase']
		tipo = request.POST['Tipo']
		myfile = request.FILES["file1"]
		fs = FileSystemStorage()
		filename = fs.save(myfile.name, myfile)
		file_name = fs.url(filename)
	
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
			
		return render(request,'ResulTOperador.html')



	