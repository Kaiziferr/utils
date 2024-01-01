# Django
---

## Inicializar el proyecto
Create a nwe project
```sh
django-admin startproject <name_project>
```

## Help
Help menu
```sh
python manage.py help
```

## Runserver
Run server
```sh
python manage.py runserver
```

### Runserver other settings new file
Run server with other  setting file
```sh
- python manage.py runserver --settings=<path>

- python manage.py runserver --settings=empleado.settings.desarrollo

```

## Create apps
```sh
python manage.py startapp <name_app>

django-admin startapp <name_app>
```

## Migrations
### Detecta cambios en el modelo
```sh
python manage.py makemigrations
```
### Crear el modelo en la base de datos
Una vez detectado los cambios, se realiza la migraciòn, para crear el modelo
```sh
python manage.py migrate
```

**Migrate for an app**
```sh
 python manage.py migrate home
```


## Admin
### Create root
Permite crear un super usuario, para acceder al administrador
```sh
python manage.py createsuperuser
```
