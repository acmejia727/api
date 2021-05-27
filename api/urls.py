
from django.contrib import admin
from django.urls import include, path
from .views import *

urlpatterns = [
    
    path('user/',UserList.as_view()),
    path('user/<int:pk>/',UserDetail.as_view(),name='user_detail'),    
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('update_profile/', UpdateProfileView.as_view(), name='auth_update_profile'),
    path('', include('rest_auth.urls')),   
    
]
