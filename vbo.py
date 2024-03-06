import numpy as np
import moderngl as mgl
import pywavefront


class VBO:
    def __init__(self, ctx) -> None:
        self.vbos = {}
        self.vbos['cube'] = CubeVBO(ctx)
        self.vbos['skybox-day'] = SkyboxVBO(ctx)
        self.vbos['skybox-night'] = SkyboxVBO(ctx)
        self.vbos['skybox-space'] = SkyboxVBO(ctx)
        self.vbos['skybox-mountain'] = SkyboxVBO(ctx)
        self.vbos['d-rex'] = DRexVBO(ctx)
        self.vbos['d-rex-eyes'] = DRexEyesVBO(ctx)
        self.vbos['wolf-body'] = WolfBody(ctx)
        self.vbos['wolf-eyes'] = WolfEyes(ctx)
        self.vbos['tree-1'] = Tree1(ctx)
        self.vbos['moon'] = Moon(ctx)

    def destroy(self):
        [vbo.destroy() for vbo in self.vbos.values()]


class BaseVbo:

    def __init__(self, ctx) -> None:
        self.ctx = ctx
        self.vbo = self.get_vbo()
        self.format: str = None
        self.attrib: str = None

    def get_vertex_data(self): ...

    def get_vbo(self):
        vertex_data = self.get_vertex_data()
        vbo = self.ctx.buffer(vertex_data)
        return vbo

    def destroy(self):
        self.vbo.release()


class DRexVBO(BaseVbo):  # D-rex - parte 1
    def __init__(self, ctx):
        super().__init__(ctx)
        self.format = '2f 3f 3f'
        self.attribs = ['in_textcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/d-rex/D_REX.obj', cache=True, parse=True)
        obj = objs.materials['D_Rex_MAT']
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data


class DRexEyesVBO(BaseVbo):  # D-rex - parte 2
    def __init__(self, ctx):
        super().__init__(ctx)
        self.format = '2f 3f 3f'
        self.attribs = ['in_textcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/d-rex/D_REX.obj', cache=True, parse=True)
        obj = objs.materials['Eye_MAT']
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data


class WolfBody(BaseVbo):  # Lobo - parte 1
    def __init__(self, ctx):
        super().__init__(ctx)
        self.format = '2f 3f 3f'
        self.attribs = ['in_textcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/wolf/Wolf_One_obj.obj', cache=True, parse=True)
        obj = objs.materials['Wolf_Body']
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data


class WolfEyes(BaseVbo):  # Lobo - parte 2
    def __init__(self, ctx):
        super().__init__(ctx)
        self.format = '2f 3f 3f'
        self.attribs = ['in_textcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/wolf/Wolf_One_obj.obj', cache=True, parse=True)
        obj = objs.materials['Wolf_Eyes']
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data


class Tree1(BaseVbo):  # Árvore
    def __init__(self, ctx):
        super().__init__(ctx)
        self.format = '2f 3f 3f'
        self.attribs = ['in_textcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/trees/tree_bonus.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data


class Moon(BaseVbo):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.format = '2f 3f 3f'
        self.attribs = ['in_textcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/moon/moon 2k.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data


class CubeVBO(BaseVbo):
    def __init__(self, ctx) -> None:
        super().__init__(ctx)
        self.format = '2f 3f 3f'
        self.attribs = ['in_textcoord_0', 'in_normal', 'in_position']

    @staticmethod
    def get_data(vertices, indices):
        data = [vertices[ind] for triangle in indices for ind in triangle]
        return np.array(data, dtype='f4')

    def get_vertex_data(self):
        vertices = [(-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1),
                    (-1, 1, -1), (-1, -1, -1), (1, -1, -1), (1, 1, -1),]

        indices = [(0, 2, 3), (0, 1, 2),
                   (1, 7, 2), (1, 6, 7),
                   (6, 5, 4), (4, 7, 6),
                   (3, 4, 5), (3, 5, 0),
                   (3, 7, 4), (3, 2, 7),
                   (0, 6, 1), (0, 5, 6)]

        vertex_data = self.get_data(vertices, indices)
        # Textura
        text_coord = [(0, 0), (1, 0), (1, 1), (0, 1)]
        text_coord_indices = [(0, 2, 3), (0, 1, 2),
                              (0, 2, 3), (0, 1, 2),
                              (0, 1, 2), (2, 3, 0),
                              (2, 3, 0), (2, 0, 1),
                              (0, 2, 3), (0, 1, 2),
                              (3, 1, 2), (3, 0, 1)]
        text_coord_data = self.get_data(text_coord, text_coord_indices)

        normais = [( 0,  0,  1) * 6,
                   ( 1,  0,  0) * 6,
                   ( 0,  0, -1) * 6,
                   (-1,  0,  0) * 6,
                   ( 0,  1,  0) * 6,
                   ( 0, -1,  0) * 6]
        normais = np.array(normais, dtype='f4').reshape(36, 3)

        vertex_data = np.hstack([normais, vertex_data])
        vertex_data = np.hstack([text_coord_data, vertex_data])

        return vertex_data


class SkyboxVBO(BaseVbo):
    def __init__(self, ctx) -> None:
        super().__init__(ctx)
        self.format = '3f'
        self.attribs = ['in_position']

    @staticmethod
    def get_data(vertices, indices):
        data = [vertices[ind] for triangle in indices for ind in triangle]
        return np.array(data, dtype='f4')

    def get_vertex_data(self):
        vertices = [(-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1),
                    (-1, 1, -1), (-1, -1, -1), (1, -1, -1), (1, 1, -1),]

        indices = [(0, 2, 3), (0, 1, 2),
                   (1, 7, 2), (1, 6, 7),
                   (6, 5, 4), (4, 7, 6),
                   (3, 4, 5), (3, 5, 0),
                   (3, 7, 4), (3, 2, 7),
                   (0, 6, 1), (0, 5, 6)]

        vertex_data = self.get_data(vertices, indices)
        vertex_data = np.flip(vertex_data, 1).copy(order='C')

        return vertex_data
