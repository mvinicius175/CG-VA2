import glm

class Light:

    def __init__(self, position=(40, -8, -170), color=(1, 1, 1)) -> None:
        self.position = glm.vec3(position)
        self.color = glm.vec3(color)
        #intensidade
        self.Ia = 0.0005 * self.color
        self.Id = 1.2 * self.color
        self.Is = 1.0 * self.color
