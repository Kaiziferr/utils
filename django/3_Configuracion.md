# Configuracion
---

1. Crear una carpeta de configuración
2. Crear un archivo base.py configuraciones basicas en comun de todos los entornos.

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

3. Crear un archivo llamado local.py => Configuración local

    - DEBUG
    - ALLOWED_HOSTS
    - DATABASE
    - STATIC_URL

4. Crear un archivo llamado prod.py => Configuración producción
5. En el archivo manage.py se modifica la ruta de ejecución del archivo de configuración 

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
6. (Opcional) Crear una carpeta donde se guardaran las aplicaciones **applications**.
7. Cuando se crea un app se debe configurar en el archivo **app.py** de la app, anexando la anexando el nombre del folder que contiene las apps.
  
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

