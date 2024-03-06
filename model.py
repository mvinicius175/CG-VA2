import numpy as np
import glm
import pygame as pg


class BaseModel:
    def __init__(self, app, vao_name, texture_id, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        self.app = app
        self.pos = pos
        self.rot = glm.vec3([glm.radians(a) for a in rot])
        self.scale = scale
        self.m_model = self.get_model_matrix()
        self.texture_id = texture_id
        self.vao = app.mesh.vao.vaos[vao_name]
        self.program = self.vao.program
        self.camera = self.app.camera

    def update(self):
        pass

    def get_model_matrix(self):
        m_model = glm.mat4()
        m_model = glm.translate(m_model, self.pos)
        m_model = glm.rotate(m_model, self.rot.z, glm.vec3(0, 0, 1))
        m_model = glm.rotate(m_model, self.rot.y, glm.vec3(0, 1, 0))
        m_model = glm.rotate(m_model, self.rot.x, glm.vec3(1, 0, 0))
        m_model = glm.scale(m_model, self.scale)
        return m_model

    def render(self):
        self.update()
        self.vao.render()


class ExtendedBaseModel(BaseModel):
    def __init__(self, app, vao_name='cube', texture_id=0, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, texture_id, pos, rot, scale)
        self.on_init()

    def update(self):
        ground_height = 0  # Ajuste conforme necessário para a posição y do chão
        if self.pos[1] < ground_height:
            self.pos = (self.pos[0], ground_height, self.pos[2])
        self.on_update()
        self.texture.use()
        self.program['camPos'].write(self.camera.position)
        self.program['m_view'].write(self.camera.m_view)
        self.program['m_model'].write(self.m_model)

    def on_update(self):
        pass

    def on_init(self):
        self.texture = self.app.mesh.texture.textures[self.texture_id]
        self.program['u_texture_0'] = 0
        self.texture.use()

        self.program['m_proj'].write(self.camera.m_proj)
        self.program['m_view'].write(self.camera.m_view)
        self.program['m_model'].write(self.m_model)

        self.program['light.position'].write(self.app.light.position)
        self.program['light.Ia'].write(self.app.light.Ia)
        self.program['light.Id'].write(self.app.light.Id)
        self.program['light.Is'].write(self.app.light.Is)


class SkyBox(BaseModel):  # "skybox"
    def __init__(self, app, vao_name, texture_id, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, texture_id, pos, rot, scale)
        self.on_init()

    def on_init(self):
        self.texture = self.app.mesh.texture.textures[self.texture_id]
        self.program['u_texture_skybox'] = 0
        self.texture.use(location=0)

        self.program['m_proj'].write(self.camera.m_proj)
        self.program['m_view'].write(glm.mat4(glm.mat3(self.camera.m_view)))

    def update(self):
        self.program['m_view'].write(glm.mat4(glm.mat3(self.camera.m_view)))


class Cube(ExtendedBaseModel):  # "cube"
    def __init__(self, app, vao_name='cube', texture_id=0, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, texture_id, pos, rot, scale)
        self.ground_height = pos[1]

    def update(self):
        super().update()
        self.pos = (self.pos[0], self.ground_height, self.pos[2])


class Tree1(ExtendedBaseModel):  # Árvore
    def __init__(self, app, vao_name='tree-1', texture_id='tree-1', pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, texture_id, pos, rot, scale)


class WolfBody(ExtendedBaseModel):  # Lobo - parte 1
    def __init__(self, app,  scale=(10, 10, 10), pos=(-10, -4, -17), rot=(0, -140, 0)):
        super().__init__(app, vao_name='wolf-body', texture_id='wolf-body', pos=pos, rot=rot, scale=scale)

    def on_update(self):
        super().on_update()


class WolfEyes(ExtendedBaseModel):  # Lobo - parte 2
    def __init__(self, app, scale=(10, 10, 10), pos=(-10, -4, -17), rot=(0, -140, 0)):
        super().__init__(app, vao_name='wolf-eyes', texture_id='wolf-eyes', pos=pos, rot=rot, scale=scale)

    def on_update(self):
        super().on_update()


class DRex(ExtendedBaseModel):  # D-rex - parte 1
    def __init__(self, app, vao_name='d-rex', texture_id='d-rex', scale=(10, 10, 10), pos=(-10, -4, -17), rot=(0, -140, 0)):
        super().__init__(app, vao_name, texture_id, pos, rot, scale)

    def on_update(self):
        super().on_update()


class DRexEyes(ExtendedBaseModel):  # D-rex - parte 2
    def __init__(self, app, vao_name='d-rex-eyes', texture_id='d-rex-eyes', scale=(10, 10, 10), pos=(-10, -4, -17), rot=(0, -140, 0)):
        super().__init__(app, vao_name, texture_id, pos, rot, scale)

    def on_update(self):
        super().on_update()
