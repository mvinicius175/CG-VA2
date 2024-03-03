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

    def update(self):...

    def get_model_matrix(self):
        m_model = glm.mat4()
        # translação
        m_model = glm.translate(m_model, self.pos)
        # rotação
        m_model = glm.rotate(m_model, self.rot.z, glm.vec3(0, 0, 1))
        m_model = glm.rotate(m_model, self.rot.y, glm.vec3(0, 1, 0))
        m_model = glm.rotate(m_model, self.rot.x, glm.vec3(1, 0, 0))
        # escala
        m_model = glm.scale(m_model, self.scale)
        return m_model

    def render(self):
        self.update()
        self.vao.render()

class ExtendedBaseModel(BaseModel):
    def __init__(self, app, vao_name='cube', texture_id=0, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, texture_id, pos, rot, scale)
        # self.aabb = self.get_aabb()
        self.on_init()

    def update(self):
        self.texture.use()
        self.program['camPos'].write(self.camera.position)
        self.program['m_view'].write(self.camera.m_view)
        self.program['m_model'].write(self.m_model)

    def on_init(self):
        # Textura
        self.texture = self.app.mesh.texture.textures[self.texture_id]
        self.program['u_texture_0'] = 0
        self.texture.use()

        self.program['m_proj'].write(self.camera.m_proj)
        self.program['m_view'].write(self.camera.m_view)
        self.program['m_model'].write(self.m_model)
        # Iluminação
        self.program['light.position'].write(self.app.light.position)
        self.program['light.Ia'].write(self.app.light.Ia)
        self.program['light.Id'].write(self.app.light.Id)
        self.program['light.Is'].write(self.app.light.Is)

class Cube(ExtendedBaseModel):
    def __init__(self, app, vao_name='cube', texture_id=0, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, texture_id, pos, rot, scale)
        # self.aabb = self.get_aabb()

#! D-Rex
class DRex(ExtendedBaseModel):
    def __init__(self, app, vao_name='d-rex', texture_id='d-rex', pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, texture_id, pos, rot, scale)
class DRexEyes(ExtendedBaseModel):
    def __init__(self, app, vao_name='d-rex-eyes', texture_id='d-rex-eyes', pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, texture_id, pos, rot, scale)

#! Wolf
class WolfBody(ExtendedBaseModel):
    def __init__(self, app, vao_name='wolf-body', texture_id='wolf-body', pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, texture_id, pos, rot, scale)
class WolfClaws(ExtendedBaseModel):
    def __init__(self, app, vao_name='wolf-claws', texture_id='wolf-body', pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, texture_id, pos, rot, scale)
class WolfEyes(ExtendedBaseModel):
    def __init__(self, app, vao_name='wolf-eyes', texture_id='wolf-eyes', pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, texture_id, pos, rot, scale)
class WolfFur(ExtendedBaseModel):
    def __init__(self, app, vao_name='wolf-fur', texture_id='wolf-fur', pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, texture_id, pos, rot, scale)

#! Trees
class Tree1(ExtendedBaseModel):
    def __init__(self, app, vao_name='tree-1', texture_id='tree-1', pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, texture_id, pos, rot, scale)

class Cat(ExtendedBaseModel):
    def __init__(self, app, vao_name='cat', texture_id='cat', pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, texture_id, pos, rot, scale)

class SkyBox(BaseModel):
    def __init__(self, app, vao_name, texture_id,
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, texture_id, pos, rot, scale)
        # self.aabb = self.get_aabb()
        self.on_init()

    def on_init(self):
        self.texture = self.app.mesh.texture.textures[self.texture_id]
        self.program['u_texture_skybox'] = 0
        self.texture.use(location=0)

        self.program['m_proj'].write(self.camera.m_proj)
        self.program['m_view'].write(glm.mat4(glm.mat3(self.camera.m_view)))

    def update(self):
        self.program['m_view'].write(glm.mat4(glm.mat3(self.camera.m_view)))


    # def get_aabb(self):
    #     center = glm.vec3(self.pos)
    #     size = glm.vec3(self.scale)
    #     return {
    #         'center': center,
    #         'size': size
    #     }

    # def get_aabb_corners(self):
    #     half_size = self.aabb['size'] / 2
    #     min_point = self.aabb['center'] - half_size
    #     max_point = self.aabb['center'] + half_size
    #     return min_point, max_point
