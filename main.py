import web #utiliza la libreria de web.py

web.config.debug = False # Desactiva el modo de depuraciondepuración 

urls = ( # urls que contendra nuestra pagina
    "/", "Index",
    "/count", "count",
    "/reset", "reset",
)

app = web.application(urls, locals()) # Direcciona las rutas

# Crea una carpeta donde van a guardarse las sesiones.
session = web.session.Session(app, web.session.DiskStore("carpeta_sessions"), initializer={"count": 0}) # El conteo de las sesiones inician en 0

class Index: # Primer pagina, ruta raiz.
    def GET(self):
        return """ 
        <h1> Manejo de sessiones con web.py</h1>
        <h4>Escribir /count para mostrar el conteo de sesiones.</h4>
        <h4>Escribir /reset para restablecer el conteo de sesiones.</h4>
        """ # Codigo HTML que se mostrara


class count: # Segunda pagina, ruta /count
    def GET(self):
        session.count += 1 #Añade una sesion
        return "Conteo total de sesiones: " + str(session.count) #Muestra el total de sesiones

class reset: #Tercera pagina, ruta /reset
    def GET(self):
        session.kill() # Borra el conteo de sesiones
        return "Reset" #Muestra el mensaje reset

if __name__ == "__main__": # Inicia la pagina web
    app.run()