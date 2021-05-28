
from django.contrib import admin
from django.urls import include, path
from .views import *

urlpatterns = [
    
    path('usuario/',UserList.as_view()),
    path('usuario/<int:pk>/',UserDetail.as_view(),name='user_detail'),    
    path('registro/', RegisterView.as_view(), name='auth_register'),
    path('usuario/actualizar/<int:pk>/', UpdateProfileView.as_view(), name='auth_update_profile'),
    path('', include('rest_auth.urls')),   
    
]
