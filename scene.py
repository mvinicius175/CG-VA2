from model import *

class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.load()

        # self.skyboxDay = SkyBox(app, vao_name='skybox-day', texture_id='skybox-day')
        self.skyboxNight = SkyBox(app, vao_name='skybox-night', texture_id='skybox-night')
        # self.skyboxSpace = SkyBox(app, vao_name='skybox-space', texture_id='skybox-space')
        # self.skyboxMountain = SkyBox(app, vao_name='skybox-mountain', texture_id='skybox-mountain')


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

        add(Cat(app, pos=(0, -4, 10), rot=(-90, 0, 0)))
        # D-Rex
        add(DRex(app, pos=(10, -4, 10), scale=(5, 5, 5)))
        add(DRexEyes(app, pos=(10, -4, 10), scale=(5, 5, 5)))


    def render(self):
        keys = pg.key.get_pressed()
        for object in self.objects:
            object.render()

        self.skyboxNight.render()


