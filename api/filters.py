import django_filters
from .models import User
class UserFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(field_name='first_name',lookup_expr='icontains')
    apellido = django_filters.CharFilter(field_name='last_name',lookup_expr='icontains')
    class Meta:
        model = User
        fields = ['id', 'nombre', 'apellido', 'cedula', 'email',]