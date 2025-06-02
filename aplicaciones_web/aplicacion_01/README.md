# 1. Hola Mundo

Ejemplo básico de web.py

```python
import web

urls = (
    '/', 'Index'
)
app = web.application(urls, globals())

class Index:
    def GET(self):
        return 'Hello mundo HTML y Python!'

if __name__ == "__main__":
    app.run()
```

## 1.1 Importar librerías

Esta línea permite importar **web.py** para utilizar los métodos para desarrollar aplicaciones web con python.

```python
import web
```

## 1.2

Cada linea permite manejar la ruta y la clase que controla cada una de las paginas web de la aplicación.

- '/' indica la ruta de acceso a la página web
- 'Index' indica el nombre de la clase que maneja el comportamiento de la página web. 
```python
urls = (
    '/, 'Index'
)
```

## 1.3


```python
app = web.application(urls, globals())
```