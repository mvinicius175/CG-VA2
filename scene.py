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
        # add(Cube(app, texture_id=0, pos=(0, 0, -1)))

        n, s = 50, 2
        for x in range(-n, n, s):
            for z in range(-n, n, s):
                add(Cube(app, texture_id=1, pos=(x, -5, z)))


    def render(self):
        for object in self.objects:
            object.render()
