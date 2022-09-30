from django.urls import path
from . import views

urlpatterns = [
    path('', views.quadro, name='quadro'),
    path('cadastrar_acidente/', views.cadastrar_acidente, name='cadastrar_acidente'),
    path('listar_acidente/', views.listar_acidente, name='listar_acidente'),
]
