from django.conf.urls import url, include
from apps.operadores.views import Operadores

from django.urls import path

app_name = 'operadores'
urlpatterns=[


	path('Operador/',Operadores.PageOperador, name = 'PageOperador'),
	path('Analizador2/',Operadores.ControladorOperador, name = 'ControladorOperador')


]