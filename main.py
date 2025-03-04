import pygame as pg
import moderngl as mgl
import sys
from model import *
from camera import Camera
from light import Light
from mesh import Mesh
from scene import Scene

class GraphicsEngine:
    def __init__(self, win_size=(1200, 700)):
        pg.init()

        self.WIN_SIZE = win_size
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        pg.display.set_mode(self.WIN_SIZE, flags=pg.OPENGL | pg.DOUBLEBUF)
        pg.event.set_grab(True)
        pg.mouse.set_visible(False)

        self.ctx = mgl.create_context()
        self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE)

        self.clock = pg.time.Clock()
        self.time = 0
        self.delta_time = 0

        self.light = Light()
        self.camera = Camera(self)
        self.mesh = Mesh(self)
        self.scene = Scene(self)

        # Variável para rastrear o tipo atual do modelo
        self.current_model_type = 'moon-diffuse'

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.mesh.destroy()
                pg.quit()
                sys.exit()

            if event.type == pg.KEYDOWN and event.key == pg.K_t:
                self.toggle_model()

    def toggle_model(self):
        # Alternar textura da lua:
        if self.current_model_type == 'moon-diffuse':  # Se já é 'moon-diffuse',
            self.current_model_type = 'moon-bump'  # então se torna 'moon-bump'.
        else:
            self.current_model_type = 'moon-diffuse'  # Se não, se torna 'moon-diffuse'.

        # Remover apenas a lua, mantendo todos os outros objetos
        self.remove_moondiffuse_moonbump()

        # Adicionar o modelo correspondente
        if self.current_model_type == 'moon-diffuse':
            self.scene.add_object(MoonDiffuse(self))
        elif self.current_model_type == 'moon-bump':
            self.scene.add_object(MoonBump(self))

    def remove_moondiffuse_moonbump(self):
        # Filtrar os objetos da cena, removendo apenas os modelos de luas:
        self.scene.objects = [obj for obj in self.scene.objects if
        not isinstance(obj, (MoonDiffuse, MoonBump))]

    def render(self):
        self.ctx.clear(color=(0.08, 0.16, 0.18))
        self.scene.render()
        pg.display.flip()

    def get_time(self):
        self.time = pg.time.get_ticks() * 0.001

    def run(self):
        while True:
            self.get_time()
            self.check_events()
            self.camera.update()
            self.render()
            self.delta_time = self.clock.tick(60)

if __name__ == '__main__':
    app = GraphicsEngine()
    app.run()
