import web
import app

render = web.template.render("mvc/views/admin/") #ruta de las vistas

class Logout: #clase Index
    def GET(self):
        return web.seeother('/login')