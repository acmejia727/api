
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [    
    path('usuario/',views.UserList.as_view()),
    path('usuario/<int:pk>/',views.UserDetail.as_view(),name='user_detail'),    
    path('registro/', views.RegisterView.as_view(), name='auth_register'),
    path('usuario/actualizar/<int:pk>/', views.UpdateProfileView.as_view(), name='auth_update_profile'),
    path('', include('rest_auth.urls')),   
    
]
