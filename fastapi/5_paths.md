# GET
1. index
```
  @app.get('')
```
2. get all
```
  @app.get('')
```
3. get one element
```
  @app.get('/elements/{id_element}')
  def metodo(id_elemetn):
```

4. get More than one params
```
  @app.get('/elements/') query params
  def get_elements(🧑‍🚀:str, 🛰️:int)
```

# POST
1. Save for body
```
  from fastapi import FastAPI, Body
  @app.post('')
  def function(v1:int, v2:str, v3:str)

```
2. Save for class
```
from pydantic import BaseModel
@app.post('')
class <Name_Class>(BaseModel)
def function(v1:Name_Class)

```
# PUT
1. Update for body
```
  from fastapi import FastAPI, Body
  @app.put('/elements/{id_element}')
  def function(v1:int, v2:str, v3:str)
```
2. Update for class
```
from pydantic import BaseModel
@app.put('/elements/{id_element}')
class <Name_Class>(BaseModel)
def function(v1:Name_Class)

```
# DELETE
1. delete
```
  @app.put('/elements/{id_element}')
  def function()
```
