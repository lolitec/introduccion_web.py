# 2. Templates

Ejemplo básico del uso de un template en web.py

```python
import web

urls = (
    '/', 'Index'
)
render = web.template.render('templates')
app = web.application(urls, globals())

class Index:
    def GET(self):
        return render.index()

if __name__ == "__main__":
    app.run()
```

## 2.1 Render

Se crea el objeto render para preparar a Templator para que pueda almacenar archivos HTML (El nombre de la carpeta para los templates no tiene importancia mientras coincidan)

```python
render = web.template.render('templates')
```

## 2.2 Llamado

Se llama al objeto render seguido del nombre del archivo HTML dentro de la carpeta templates para su ejecución.

```python
class Index:
    def GET(self):
        return render.index()
```

## 2.3 Página index.html

Se crea la página principal de cualquier sitio web, dado que index.html es lo primero que buscan los programas para renderizar el sitio, es por asi decirlo la página de inicio.

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset='utf-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1'>
    <title>Hola mundo web.py</title>
</head>
<body>
    <h1>Hola mundo web.py</h1>
</body>
</html>
```

## 2.4 Tipo de documento

Esta linea define el tipo de documento y le dice al navegador que el archivo es un documento HTML.

```html
<!DOCTYPE html>
```

## 2.5 Lenguaje

Le indica al documento que tipo de lenguaje es el utilizado en el documento, esto es útil para apps de traducción o de lectura de voz.

```html
<html lang="es">
```

## 2.6 Lineamientos de la página

Se abre la sección head del documento la cual se usa para colocar datos que no se mostrarán directamente en la página.
El utf-8 permite que se muestren caractéres externos al idioma inglés, ya sea la ñ del español o alfabetos de distintos idiomas por ejemplo la letra rusa Ж.
La siguiente línea hace que el diseño de la página sea responsivo, es decir, que se ajuste a diferentes tamaños de pantalla.
Title es lo que se ve en la parte superior de la ventana o pestaña del navegador.

```html
<head>
    <meta charset='utf-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1'>
    <title>Hola mundo web.py</title>
</head>
```

## 2.7 Contenido de la página

Abre el cuerpo del documento, es decir, lo que se va a mostrar en la pantalla del navegador.
Se imprime en la página el texto "Hola mundo web.py" de tamaño h1.

```html
<body>
    <h1>Hola mundo web.py</h1>
</body>
```
