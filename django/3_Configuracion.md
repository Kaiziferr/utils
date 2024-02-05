# Configuracion
---



1. Create settings folder in the main folder
2. Create the workflow environment config files, for example base, deploy, development, test, ...
3. Include in the files of settings the code lines necessary to execute the project in the new setting from the file original
   - **Base (base file   settings)**
       - BASE_DIR
       - SECRET_KEY
       - INSTALLED_APPS
       - MIDDLEWARE
       - ROOT_URLCONF
       - TEMPLATES
       - WSGI_APPLICATION
       - AUTH_PASSWORD_VALIDATORS
       - LANGUAGE_CODE     (Puede que dependiendo del programador, se trabaje con otras configuraciones de idiomas y zona horaria)
       - TIME_ZONE     
       - USE_I12N
       - USE_TZ
       - DEFAULT_AUTO_FIELD
   - **Development File**
       - DEBUG
       - ALLOWED_HOSTS
       - DATABASE
       - STATIC_URL
    - **Deployment File**

5. In the file manage.py is modified the run path of config file

```py
def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'employees.settings')
                              :
def main():
  """Run administrative tasks."""
  os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'employees.settings.local')
```


# Aplicaciones
---
6. (Opcional) Create a folder where is have save the **apps**.
7. When is create an app is must configure the file app, add the name of folder the apps.
  
```py
# name = <folder apps>.aplication creado.

class DepartamentoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'applications.departamento'
```
8. Modificar con la ruta de las aplicaciones 
```py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Apps
    'departamentos.departamentos',
    'empleados.empleados'
]
```

# Tamplates
---
9. Crear una carpeta template que almacene todos los templates de todas las apps y los genericos.
- Se debe modificar en el archivo de la configuraciòn base.
```py
BASE_DIR = Path(__file__).resolve().parent.parent.parent

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
# URLS

10 Por cada aplicaciòn y dependiendo de la necesidad se crea un archivo urls, el cual administrara las url de la aplicaciòn. En el archivo url principal se debe configurar con el include

```py
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('aplications.home.urls'))
]
```

# Admin
---
Registrar el modelo para acceder o gestionarlo desde el admin.
```py
from django.contrib import admin
from models import Prueba

# Register your models here.

admin.site.register(Prueba)
```

# Migrations
En la carpeta se Migrations se encuentran las migraciones detectadas por el sistema.
Solo tendra en cuenta los cambios de las apps que esten instaladas en INSTALLED_APPS
- migrations
    - 0001_initial.py 

# Static Files
---
Configuracion de archivos estaticos (normalmente desde la base local)
```py
STATIC_URL = 'static/' 
STATICFILES_DIRS = [os.path.join(BASE_DIR ,'static')]
```
En el archivo html:
```html
{% load static %}
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{% static 'prueba.css' %}">
    <title>Document</title>
</head>
<body>
    <h1 class="ejemplo1">Hello everybody</h1>
    <h1 class="ejemplo2">Hello everybody</h1>
</body>
</html>
```

