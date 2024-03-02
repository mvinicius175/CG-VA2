import glm
import pygame as pg

FOV = 50
NEAR = 0.1
FAR = 100
SPEED = 0.01
SENSITIVITY = 0.05


class Camera:
    def __init__(self, app, position = (0, 0, 4), yaw=-90, pitch=0):
        self.app = app
        self.aspect_ratio = app.WIN_SIZE[0] / app.WIN_SIZE[1]
        self.position = glm.vec3(position)
        self.up = glm.vec3(0, 1, 0)
        self.right = glm.vec3(1, 0, 0)
        self.forward = glm.vec3(0, 0, -1)
        self.yaw = yaw
        self.pitch = pitch
        self.m_view = self.get_view_matrix()
        # projeção da matriz
        self.m_proj = self.get_projection_matrix()

    def rotate(self):
        rel_x, rel_y = pg.mouse.get_rel()
        self.yaw += rel_x * SENSITIVITY
        self.pitch -= rel_y * SENSITIVITY
        self.pitch = max(-89, min(89, self.pitch))

    def update_camera_vectors(self):
        yaw, pitch = glm.radians(self.yaw), glm.radians(self.pitch)

        self.forward.x = glm.cos(yaw) * glm.cos(pitch)
        self.forward.y = glm.sin(pitch)
        self.forward.z = glm.sin(yaw) * glm.cos(pitch)

        self.forward = glm.normalize(self.forward)
        self.right = glm.normalize(glm.cross(self.forward, glm.vec3(0, 1, 0)))
        self.up = glm.normalize(glm.cross(self.right, self.forward))

    def update(self):
        self.move()
        self.rotate()
        self.update_camera_vectors()
        self.m_view = self.get_view_matrix()

    def move(self):
        APPROACH_LIMIT = 3.0
        velocity = SPEED * self.app.delta_time
        keys = pg.key.get_pressed()

        for obj in self.app.scene.objects:
            # Calcular a distância entre a câmera e o objeto
            distance = glm.length(self.position - obj.pos)
            if distance < APPROACH_LIMIT:
                # A câmera está muito próxima do objeto, ajustar a posição para manter a distância mínima
                direction = glm.normalize(self.position - obj.pos)
                self.position += direction * (APPROACH_LIMIT - distance)
                return # Não permitir mais movimentos neste frame

        if keys[pg.K_w]:
            self.position += self.forward * velocity
        if keys[pg.K_s]:
            self.position -= self.forward * velocity
        if keys[pg.K_d]:
            self.position += self.right * velocity
        if keys[pg.K_a]:
            self.position -= self.right * velocity
        if keys[pg.K_q]:
            self.position += self.up * velocity
        if keys[pg.K_e]:
            self.position -= self.up * velocity


    # def is_colliding_with_objects(self):
    #     for obj in self.app.scene.objects:
    #         obj_aabb = obj.get_aabb()
    #         camera_aabb = {
    #             'center': self.position,
    #             'size': glm.vec3(1, 1, 1)
    #         }

    #         if self.is_aabb_colliding(camera_aabb, obj_aabb):
    #             return True
    #     return False

    # @staticmethod
    # def is_aabb_colliding(aabb1, aabb2):
    #     # Verifica se duas AABBs estão colidindo
    #     return (
    #         abs(aabb1['center'].x - aabb2['center'].x) < (aabb1['size'].x + aabb2['size'].x) / 2 and
    #         abs(aabb1['center'].y - aabb2['center'].y) < (aabb1['size'].y + aabb2['size'].y) / 2 and
    #         abs(aabb1['center'].z - aabb2['center'].z) < (aabb1['size'].z + aabb2['size'].z) / 2
    #     )

    def get_view_matrix(self):
        return glm.lookAt(self.position, self.position + self.forward, self.up)

    def get_projection_matrix(self):
        return glm.perspective(glm.radians(FOV), self.aspect_ratio, NEAR, FAR)
