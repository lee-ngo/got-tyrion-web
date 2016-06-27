import web
# importing classes from various directories
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from sys import exit
from scene import Scene # imported before every inherited Scene

# from setup.engine import Engine
# from setup.map import Map
# urls has two parameters: the url and the class you will call to render
urls = (
    '/game', 'GameEngine',
    '/', 'Index',
)

app = web.application(urls, globals())

# creating sessions in the application
if web.config.get('_session') is None:
    store = web.session.DiskStore('session')
    session = web.session.Session(app, store, initializer={ 'scene': None })
    web.config._session = session # creates new session with no scene
else:
    session = web.config._session # stays in current session

render = web.template.render('templates/', base="layout")
# Python will now use layout as the base and send other pages through it

class Index(object):
    def GET(self): # first gets the form from hello-form
        # return render.hello_form() # asks you to submit information here
        # this is used to "setup" the session with starting values
        return render.introduction()
        web.seeother("/game")

class GameEngine(object):
    def GET(self): # get function for picking out correct scene
        if session.scene:
            return render.show_scene(scene=session.scene)
        else:
            return render.death() # create death.html template

    def POST(self):
        form = web.input(action=None)
        if session.scene and form.action:
            session.scene = session.scene.go(form.action)

        web.seeother('/game')
        # form = web.input(name="Nobody", action=None)
        # if form.name:
        #     your_name = form.name
        #     return render.introduction(your_name = your_name)
        # else:
        #     return "Whoops! Please put a greeting and name!"

if __name__ == "__main__":
    app.run()
