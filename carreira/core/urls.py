from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('',views.cadastro, name='cadastroPresenca'),
    path('listar',views.listar, name='listar')
]
