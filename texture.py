import pygame as pg
import moderngl as mgl

class Texture:
    def __init__(self, ctx):
        self.ctx = ctx
        self.textures = {}
        self.textures[0] = self.get_texture(path='textures/tree_texture.png')
        self.textures[1] = self.get_texture(path='textures/grass_texture1.png')
        self.textures[2] = self.get_texture(path='textures/grass_texture2.png')
        self.textures['cat'] = self.get_texture(path='objects/cat/20430_cat_diff_v1.jpg')
        self.textures['d-rex'] = self.get_texture(path='objects/d-rex/d-rex-body.png')
        self.textures['d-rex-eyes'] = self.get_texture(path='objects/d-rex/d-rex-eyes.png')
        self.textures['skybox-day'] = self.get_skybox_texture(dir_path='textures/skybox/day/', ext='png')
        self.textures['skybox-night'] = self.get_skybox_texture(dir_path='textures/skybox/night/', ext='png')
        self.textures['skybox-space'] = self.get_skybox_texture(dir_path='textures/skybox/space/', ext='png')
        self.textures['skybox-mountain'] = self.get_skybox_texture(dir_path='textures/skybox/mountain/', ext='png')


    def get_texture(self, path):
        texture = pg.image.load(path).convert()
        texture = pg.transform.flip(texture, flip_x=False, flip_y=True)
        texture = self.ctx.texture(size=texture.get_size(), components=3,
                                   data=pg.image.tostring(texture, 'RGB'))

        # MipMaps
        texture.filter = (mgl.LINEAR_MIPMAP_LINEAR, mgl.LINEAR)
        texture.build_mipmaps()
        texture.anisotropy = 32.0

        return texture

    def get_skybox_texture(self, dir_path, ext='png'):
        faces = ['right', 'left', 'top', 'bottom'] + ['front', 'back'][::-1]
        # textures = [pg.image.load(dir_path + f'{face}.{ext}').convert() for face in faces]
        textures = []
        for face in faces:
            texture = pg.image.load(dir_path + f'{face}.{ext}').convert()
            if face in ['right', 'left', 'front', 'back']:
                texture = pg.transform.flip(texture, flip_x=True, flip_y=False)
            else:
                texture = pg.transform.flip(texture, flip_x=False, flip_y=True)
            textures.append(texture)

        size = textures[0].get_size()
        texture_cube = self.ctx.texture_cube(size=size, components=3, data=None)

        for i in range(6):
            texture_data = pg.image.tostring(textures[i], 'RGB')
            texture_cube.write(face=i, data=texture_data)

        return texture_cube


    def destroy(self):
        [texture.release() for texture in self.textures.values()]
