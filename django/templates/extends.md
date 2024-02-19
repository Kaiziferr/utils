1.   {% block <name_block> %} {% endblock <name_block> %} Permite establecer un espacio, para ingresar el contenido específico de los templates.
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>
        {% block title %}
        {% endblock title %}
    </title>
</head>
<body>
    <p>Todos me heredan</p>
    {% block body %}
    {% endblock body %}
</body>
</html>
```
2. {% extends <path> %} extends permite heredar los archivos del archivo base. 

```html
{% extends 'home/commun/base.html' %}
{% load static %}

{% block title %}
    Prueba para la herencia de base
{% endblock title %}

{% block body %}
    <h1>Aqui va el contenido 1</h1>
    <div class="grid-x">
        <div class="cell callout success">
            <h5>
                This is a callout
            </h5>
        </div>
    </div>
{% endblock body %}
```
