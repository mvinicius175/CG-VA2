# scene.py
import pygame as pg
from model import *


class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.load()

        self.skyboxMountain = SkyBox(app, vao_name='skybox-mountain', texture_id='skybox-mountain')

    def add_objects(self, obj):
        self.objects.append(obj)

    def load(self):
        app = self.app
        add = self.add_objects

        n, s = 50, 2
        for x in range(-n, n, s):
            for z in range(-n, n, s): # adicionando "cube" e 2 árvores:
                add(Cube(app, texture_id=1, pos=(x, -5, z)))
                add(Tree1(app, pos=(15, -4, -10), scale=(7, 7, 7)))
                add(Tree1(app, pos=(25, -4, -10), scale=(5, 5, 5)))
        # inicializando com lobo:
        add(WolfBody(app, pos=(-10, -4, -17), scale=(10, 10, 10), rot=(0, -140, 0)))
        add(WolfEyes(app, pos=(-10, -4, -17), scale=(10, 10, 10), rot=(0, -140, 0)))

    def render(self):
        keys = pg.key.get_pressed()
        for obj in self.objects:
            obj.render()

        self.skyboxMountain.render()
