# Documentación

Base de datos y REST API capaz de gestionar un pequeño banco de usuarios.

#### Acceso a la versión en la nube

https://apiandres.herokuapp.com/

## Instalación

#### Requisitos
Mysql

###### Modificar en el archivo `banco_usuario/settings.py`



```python
DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'apidb',
            'USER': 'root',
            'PASSWORD': '*****',
            'HOST': '127.0.0.1',
            'PORT': '3306',
        }
    }
```
#### Ejecutar la API
1. Clone el repositorio: `git clone https://github.com/acmejia727/api.git`.
2. `cd` entrar `banco_usuario`
3. Instalar ` pip install virtualenv`
4. Crear un entorno con virtualenv ej: `venv`.
5. Acceder al entorno virtual: `venv`. comando linux: `source venv/bin/activate` o Windows:`venv\Scripts\activate`
6. Ejecutar ` pip install –r requirements.txt `
7. Ejecutar ` python manager.py migrate `
8. Ejecutar ` python manager.py runserver `


## Acceso API

También está habilitado la interfaz web para consultas al API, o puede acceder por medio de la URL usando Postman con la opciones from-data o usando JSON

### Creación de usuario

El sistema permite la creación de usuarios 

```node
POST /api/registro/
```

###### JSON

```json
{
    "username": "username",
    "password": "12345678",
    "password2": "12345678",
    "email": "andres@mail.com",
    "nombre": "andres",
    "apellido": "mejia",
    "cedula": 123456,
    "imagen": null,
    "entidad": "EPS"
}
```

### Iniciar sesión

Puede iniciar sesión con correo y contraseña. Debe retornar la información del usuario y el JSON Web Token 

```node
POST /api/login/
```

###### JSON

```json
{
    "email":"andres@mail.com",
    "password":"12345678"
}
```
El API devolverá un key token:
```json
{
    "key": "1a1c4fe345259d047f8b36990a25a14768c0f514"
}
```

### Listar usuarios

Para ingresar a las demás URL debe poseer el token, añada en el header Authorization y como valor ingrese el token. debe recordar debe poner la palabra Token y seguido el código

```node
'Authorization': 'Token 2a3de065381f08e29b38753929fa8ccc86d61932'
GET /api/usuario/
```

###### JSON

```json
{
    "email":"andres@mail.com",
    "password":"12345678"
}
```
El API devolverá el listado de usuarios, adicional un campo llamado 'url' el cual tiene la URL para acceder al Detalle de usuario :
```json
{
    
    "id": 1,
    "nombre": "",
    "apellido": "",
    "cedula": null,
    "email": "acmejia@gma.com",
    "url": "http://127.0.0.1:8000/api/user/1/"
    
}

```
###### Filtro de busqueda
Usando el método GET podemos filtrar usando la variables nombre , apellido, cedula y email
```node
'Content-Type': 'application/json', 
'Authorization': 'Token 2a3de065381f08e29b38753929fa8ccc86d61932'
GET /api/usuario/?nombre=andres&apellido=mejia
```

## Detalle de usuario
El usuario podrá visualizar el detalle de algún usuario en específico usando el [ID] del usuario en la lista de usuarios. 

```node
'Authorization': 'Token 2a3de065381f08e29b38753929fa8ccc86d61932'
GET /api/usuario/[ID]/
```

## Editar Usuario
El usuario podrá actualizar el detalle de algún usuario en específico usando el [ID] del usuario en la lista de usuarios. 

```node
'Authorization': 'Token 2a3de065381f08e29b38753929fa8ccc86d61932'
PATCH /api/usuario/actualizar/[ID]/
```

```json
{
    "password": "123456",
    "nombre": "andres",
    "apellido": "mejia",
    "imagen": null,
    "entidad": "EPS"
}
```

#### Nota

Para subir las imágenes puede hacer uso de form-data