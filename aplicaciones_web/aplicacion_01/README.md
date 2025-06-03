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

## 1.2 Rutas

Cada linea permite manejar la ruta y la clase que controla cada una de las paginas web de la aplicación.

- '/' indica la ruta de acceso a la página web
- 'Index' indica el nombre de la clase que maneja el comportamiento de la página web. 
```python
urls = (
    '/, 'Index'
)
```

## 1.3 Encapsular

Se crea un objeto de tipo web.application encapsulando las urls y permitiendo a web.py su uso global en el documento

```python
app = web.application(urls, globals())
```

## 1.4 Estructura basica

Se crea la estructura básica para cualquier página web de web.py.
Se crea la clase Index la cual se habia mencionado anteriormente, se le define el metodo GET, el cual es el encargado de mandar a llamar a la página para su renderizado y simplemente regresa el texto "Hello mundo HTML y Python!" a la página

```python
class Index:
    def GET(self):
        return 'Hello mundo HTML y Python!'
```

## 1.5 Ejecutar

Se comprueba si la variable main y name son iguales, la variable name es especial ya que toma el valor de donde se ejecuta, es decir, este código solo permite que se ejecute el archivo de forma directa ya que si no la variable name no tomara el valor de main y no se ejecutará la página.

```python
if __name__ == "__main__":
    app.run()
```
