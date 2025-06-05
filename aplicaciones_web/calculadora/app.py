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
        print(formulario)
        n1 = formulario.inp_numero1
        n2 = formulario.inp_numero2
        if n1 == "":
            return render.calculadora("Falta el primer numero",0,0)
        elif n2 == "":
            return render.calculadora("Falta el segundo numero",0,0)
        else:
            operacion = formulario.btn_operacion
            n1 = int(n1)
            n2 = int(n2)
            if operacion == "suma":
                return render.calculadora(n1+n2,n1,n2)
            elif operacion == "resta":
                return render.calculadora(n1-n2,n1,n2)
            elif operacion == "multiplicacion":
                return render.calculadora(n1*n2,n1,n2)
            elif operacion == "division":
                try:
                    return render.calculadora(round(float(n1)/float(n2),2),n1,n2)
                except ZeroDivisionError:
                    return render.calculadora("Error, divison por 0")
            else:
                return render.calculadora(0)

if __name__ == "__main__":
    app.run()
