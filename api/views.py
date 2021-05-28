from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import UserSerializer,RegisterSerializer,UpdateUserSerializer,UserDetailSerializer
from .filters import UserFilter
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.db.models import Q
from rest_framework.decorators import api_view, permission_classes
from django.http import JsonResponse
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
from .models import User
# Create your views here.
class UserList(generics.ListAPIView):
    queryset  = User.objects.all()
    serializer_class = UserSerializer      
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilter
    filterset_fields =  ['id', 'first_name', 'last_name', 'cedula', 'email',]
    
   
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

class UserEmailDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        email = self.request.query_params.get("email", None)
        if not email:
            raise Http404
        return User.objects.filter(email=self.kwargs["email"])

class RegisterView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()    
    serializer_class = RegisterSerializer


class UpdateProfileView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UpdateUserSerializer

    
