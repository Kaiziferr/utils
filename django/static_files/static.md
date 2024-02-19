1. Create a folder called static
  - In this folder will be the files statics as css, js
2. In the file html call the static files

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
