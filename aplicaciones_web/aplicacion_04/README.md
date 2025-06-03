# 4. Sitio web

Ejemplo básico de un sitio web con web.py

```python
import web

urls = (
    '/', 'Index',
    '/bienvenida', 'Bienvenida'
)
render = web.template.render('templates')
app = web.application(urls, globals())

class Index:
    def __init__(self):
        self.mensaje = "Este es el index"

    def GET(self):
        return render.index(self.mensaje)

class Bienvenida:
    def __init__(self):
        pass

    def GET(self):
        mensaje = "Esta es la bienvenida"
        return render.bienvenida(mensaje)

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
    <a href="/bienvenida" target="_self">Bienvenida!</a>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.6/dist/js/bootstrap.bundle.min.js" integrity="sha384-j1CDi7MgGQ12Z7Qab0qlWQ/Qqz24Gc6BM0thvEMVjHnfYGF0rmFCozFSxQBxwHKO" crossorigin="anonymous"></script>
  </body>
</html>
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
    <a href="/" target="_self">Index!</a>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.6/dist/js/bootstrap.bundle.min.js" integrity="sha384-j1CDi7MgGQ12Z7Qab0qlWQ/Qqz24Gc6BM0thvEMVjHnfYGF0rmFCozFSxQBxwHKO" crossorigin="anonymous"></script>
  </body>
</html>
```

## 4.1 Página adicional

Se crea el contenido necesario para la nueva página web del sitio, siendo esto su ruta y su clase con el contenido necesario en la misma.

```python
urls = (
    '/', 'Index',
    '/bienvenida', 'Bienvenida'
)

class Bienvenida:
    def __init__(self):
        pass

    def GET(self):
        mensaje = "Esta es la bienvenida"
        return render.bienvenida(mensaje)
```

## 4.2 Vincular ambas páginas

Se crea un hipervínculo desde una página a la otra utilizando la ruta determinada a cada una de ellas.

```html
<a href="/bienvenida" target="_self">Bienvenida!</a>
<a href="/" target="_self">Index!</a>
```