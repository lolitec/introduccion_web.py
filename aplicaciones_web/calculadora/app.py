import web

urls = (
    '/', 'Index'
)
render = web.template.render('templates')
app = web.application(urls, globals())

class Index:
    def GET(self):
        return render.calculadora()
    
    def POST(self):
        formulario = web.input()
        n1 = int(formulario.inp_numero1)
        n2 = int(formulario.inp_numero2)
        return render.calculadora(n1+n2)

if __name__ == "__main__":
    app.run()
