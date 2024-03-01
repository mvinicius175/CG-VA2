from model import *

class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.load()


    def add_object(self, object):
        self.objects.append(object)

    def load(self):
        app = self.app
        add = self.add_object
        add(Cube(app))

    def render(self):
        for object in self.objects:
            object.render()
