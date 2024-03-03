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

        #! Floor
        n, s = 50, 2
        for x in range(-n, n, s):
            for z in range(-n, n, s):
                add(Cube(app, texture_id=1, pos=(x, -5, z)))

        add(Cat(app, pos=(20, -4, 10), rot=(-90, 0, 0), scale=(2, 2, 2)))
        #! D-Rex
        add(DRex(app, pos=(10, -4, -15), scale=(10, 10, 10), rot=(0, 40, 0)))
        add(DRexEyes(app, pos=(10, -4, -15), scale=(10, 10, 10), rot=(0, 40, 0)))
        #################################################################################
        add(DRex(app, pos=(40, -4, -35), scale=(8, 8, 8), rot=(0, 160, 0)))
        add(DRexEyes(app, pos=(40, -4, -35), scale=(8, 8, 8), rot=(0, 160, 0)))
        #################################################################################
        add(DRex(app, pos=(-40, -4, -35), scale=(15, 15, 15), rot=(0, -120, 0)))
        add(DRexEyes(app, pos=(-40, -4, -35), scale=(15, 15, 15), rot=(0, -120, 0)))
        #! Wolf
        add(WolfBody(app, pos=(-10, -4, -15), scale=(10, 10, 10), rot=(0,-140, 0)))
        add(WolfClaws(app, pos=(-10, -4, -15), scale=(10, 10, 10), rot=(0,-140, 0)))
        add(WolfEyes(app, pos=(-10, -4, -15), scale=(10, 10, 10), rot=(0,-140, 0)))
        add(WolfFur(app, pos=(-10, -4, -15), scale=(10, 10, 10), rot=(0,-140, 0)))
        ##################################################################################
        add(WolfBody(app, pos=(20, -4, -40), scale=(15, 15, 15), rot=(0,165, 0)))
        add(WolfClaws(app, pos=(20, -4, -40), scale=(15, 15, 15), rot=(0,165, 0)))
        add(WolfEyes(app, pos=(20, -4, -40), scale=(15, 15, 15), rot=(0,165, 0)))
        add(WolfFur(app, pos=(20, -4, -40), scale=(15, 15, 15), rot=(0,165, 0)))
        ##################################################################################
        add(WolfBody(app, pos=(-40, -4, 23), scale=(6, 6, 6), rot=(0,-45, 0)))
        add(WolfClaws(app, pos=(-40, -4, 23), scale=(6, 6, 6), rot=(0,-45, 0)))
        add(WolfEyes(app, pos=(-40, -4, 23), scale=(6, 6, 6), rot=(0,-45, 0)))
        add(WolfFur(app, pos=(-40, -4, 23), scale=(6, 6, 6), rot=(0,-45, 0)))
        ##################################################################################
        add(WolfBody(app, pos=(-30, -4, 30), scale=(6, 6, 6), rot=(0,-45, 0)))
        add(WolfClaws(app, pos=(-30, -4, 30), scale=(6, 6, 6), rot=(0,-45, 0)))
        add(WolfEyes(app, pos=(-30, -4, 30), scale=(6, 6, 6), rot=(0,-45, 0)))
        add(WolfFur(app, pos=(-30, -4, 30), scale=(6, 6, 6), rot=(0,-45, 0)))
        ##################################################################################
        add(WolfBody(app, pos=(-40, -4, 33), scale=(10,10,10), rot=(0,-50, 0)))
        add(WolfClaws(app, pos=(-40, -4, 33), scale=(10,10,10), rot=(0,-50, 0)))
        add(WolfEyes(app, pos=(-40, -4, 33), scale=(10,10,10), rot=(0,-50, 0)))
        add(WolfFur(app, pos=(-40, -4, 33), scale=(10,10,10), rot=(0,-50, 0)))
        #! Trees
        add(Tree1(app, pos=(0, -4, -10), scale=(5, 5, 5)))
        add(Tree1(app, pos=(10, -4, -10), scale=(5, 5, 5)))
        add(Tree1(app, pos=(17, -4, 6), scale=(5, 5, 5)))
        add(Tree1(app, pos=(6, -4, 6), scale=(5, 5, 5)))
        add(Tree1(app, pos=(26, -4, 20), scale=(5, 5, 5)))
        add(Tree1(app, pos=(40, -4, 20), scale=(5, 5, 5)))
        add(Tree1(app, pos=(35, -4, 25), scale=(5, 5, 5)))
        add(Tree1(app, pos=(-20, -4, 20), scale=(5, 5, 5)))
        add(Tree1(app, pos=(-10, -4, -10), scale=(5, 5, 5)))
        add(Tree1(app, pos=(-5, -4, 30), scale=(5, 5, 5)))
        add(Tree1(app, pos=(-13, -4, -20), scale=(5, 5, 5)))
        add(Tree1(app, pos=(-20, -4, 0), scale=(5, 5, 5)))
        add(Tree1(app, pos=(5, -4, 33), scale=(5, 5, 5)))
        add(Tree1(app, pos=(45, -4, 35), scale=(5, 5, 5)))
        add(Tree1(app, pos=(42, -4, 13), scale=(5, 5, 5)))


    def render(self):
        keys = pg.key.get_pressed()
        for object in self.objects:
            object.render()

        self.skyboxNight.render()


