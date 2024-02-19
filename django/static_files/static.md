1. Create a folder called static
  - In this folder will be the files statics as css, js
2. In the file local o the file settings, insert the next line
```md
STATIC_URL = 'static/' 
STATICFILES_DIRS = [os.path.join(BASE_DIR ,'static')]
```
this line config the file statics in the center path the DJANGO

3. In the file html call the static files

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
