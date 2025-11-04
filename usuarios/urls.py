from django.urls import path
from . import views
from .views import registrar_usuario, login_view, UsuarioList

urlpatterns = [
    path('', views.UsuarioList.as_view(), name='usuarios_list'),
    path('usuarios/', views.UsuarioList.as_view(), name='usuarios-list'),
    path('login/', views.login_view, name='login'),
    path('registrar/', views.registrar_usuario, name='registrar_usuario'),
]