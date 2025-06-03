# 3. Templates con parámetros

Ejemplo de como se usan parámetros de web.py con html

```python
import web

urls = (
    '/', 'Index'
)
render = web.template.render('templates')
app = web.application(urls, globals())

class Index:
    def __init__(self):
        self.mensaje = "Este es un texto cualquiera"

    def GET(self):
        return render.index(self.mensaje)

if __name__ == "__main__":
    app.run()
```

```html
$def with(mensaje)
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>web.py</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.6/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4Q6Gf2aSP4eDXB8Miphtr37CMZZQ5oXLH2yaXMJ2w8e2ZtHTl7GptT4jmndRuHDT" crossorigin="anonymous">
  </head>
  <body>
    <h1>$mensaje</h1>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.6/dist/js/bootstrap.bundle.min.js" integrity="sha384-j1CDi7MgGQ12Z7Qab0qlWQ/Qqz24Gc6BM0thvEMVjHnfYGF0rmFCozFSxQBxwHKO" crossorigin="anonymous"></script>
  </body>
</html>
```

## 3.1 Envío de datos

Se añade una variable global a la clase Index en el método __init__, lo cual permite almacenar el texto que luego será enviado a la template HTML.

```python
def __init__(self):
        self.mensaje = "Este es un texto cualquiera"
```

## 3.2 Llamado con variable.

Ahora se pasa la variable global como argumento a render.index() y eso permite que el contenido del documento HTML cambie dependiendo del valor de esa variable.

```python
def GET(self):
        return render.index(self.mensaje)
```

## 3.3 Parámetros en HTML

Se le permite al archivo HTML recibir una variable que será insertada en el contenido usando el signo de $, en este ejemplo la variable se llama mensaje pero puede ser el nombre que sea.

```html
$def with(mensaje)
```

## 3.4 Uso de la variable

Se muestra el contenido de la variable indicado en el archivo de python mediante el signo de $.

```html
<h1>$mensaje</h1>
```