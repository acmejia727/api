

from rest_framework import serializers
from .models import User
from rest_framework.fields import SerializerMethodField
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.HyperlinkedModelSerializer):
    nombre = serializers.CharField(source='first_name')
    apellido = serializers.CharField(source='last_name')
  
    class Meta:
        model = User
        fields = ['id', 'nombre', 'apellido', 'cedula', 'email','url',]
        extra_kwargs = {
            'url': {'view_name': 'user_detail'}
        }


class UserDetailSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField(source='first_name')
    apellido = serializers.CharField(source='last_name')
    class Meta:
        model = User
        fields = ['id', 'nombre', 'apellido', 'cedula', 'email','imagen',"entidad"]

class RegisterSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField(source='first_name')
    apellido = serializers.CharField(source='last_name')
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'nombre', 'apellido',"cedula","imagen","entidad")
        extra_kwargs = {
            'nombre': {'required': True},
            'apellido': {'required': True},
           # 'email': {'required': False}
        }

    def validate(self, attrs):
        try:
            email = attrs['imagen']
        except KeyError:
            attrs['imagen'] = ''
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Los campos de la contraseña no coinciden."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            cedula=validated_data['cedula'],
            imagen=validated_data['imagen'],
            entidad=validated_data['entidad'],
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user

class UpdateUserSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField(source='first_name')
    apellido = serializers.CharField(source='last_name')

    class Meta:
        model = User
        fields = ('password',  'nombre', 'apellido',"imagen","entidad")
        
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'imagen': {'required': False},
        }

    def validate(self, attrs):
        try:
            email = attrs['imagen']
        except KeyError:
            attrs['imagen'] = ''

        return attrs


    def partial_update(self, instance, validated_data):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)