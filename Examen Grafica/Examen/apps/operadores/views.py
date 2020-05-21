from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from django.views.generic import CreateView
from django.core.files.storage import FileSystemStorage
from django.core.files.storage import Storage
from django.core.files.base import ContentFile

def inicio(request):
    return render(request,'Home.html')

class Operadores():
	def PageOperador(request):
		return render(request,'PageOperador.html')
	def ControladorOperador(request):

		id = request.POST['fase']
		myfile = request.FILES["file1"]
		fs = FileSystemStorage()
		filename = fs.save(myfile.name, myfile)
		file_name = fs.url(filename)
		return render(request,'ResulTOperador.html')
		
	