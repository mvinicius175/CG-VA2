import numpy as np
import moderngl as mgl

class VBO:
    def __init__(self, ctx) -> None:
        self.vbos = {}
        self.vbos['cube'] = CubeVBO(ctx)
        self.vbos['skybox-day'] = SkyboxVBO(ctx)
        self.vbos['skybox-night'] = SkyboxVBO(ctx)
        self.vbos['skybox-space'] = SkyboxVBO(ctx)
        self.vbos['skybox-mountain'] = SkyboxVBO(ctx)

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
                              (3, 1, 2), (3, 0, 1),]
        text_coord_data = self.get_data(text_coord, text_coord_indices)

        normais = [( 0,  0,  1) * 6,
                   ( 1,  0,  0) * 6,
                   ( 0,  0, -1) * 6,
                   (-1,  0,  0) * 6,
                   ( 0,  1,  0) * 6,
                   ( 0, -1,  0) * 6,]
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
