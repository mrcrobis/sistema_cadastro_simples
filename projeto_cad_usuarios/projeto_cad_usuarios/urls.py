from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    # rota, view responsavel, nome ref
    path('', views.home, name='home'),
    path('usuarios/', views.usuarios, name='listagem_usuarios')
]
