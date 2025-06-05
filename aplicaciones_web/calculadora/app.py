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
        if "btn_su" in formulario:
            return render.calculadora(n1+n2)
        elif "btn_re" in formulario:
            return render.calculadora(n1-n2)
        elif "btn_mu" in formulario:
            return render.calculadora(n1*n2)
        elif "btn_di" in formulario:
            try:
                return render.calculadora(round(float(n1)/float(n2),2))
            except ZeroDivisionError:
                return render.calculadora(0)
        else:
            return render.calculadora(0)

if __name__ == "__main__":
    app.run()
