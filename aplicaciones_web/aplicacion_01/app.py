import web

urls = (
    '/bienvenida', 'Index'
)
app = web.application(urls, globals())

class Index:
    def GET(self):
        return 'Hello mundo HTML y Python!'

if __name__ == "__main__":
    app.run()
