from vbo import VBO
from shader_program import ShaderProgram


class VAO:
    def __init__(self, ctx) -> None:
        self.ctx = ctx
        self.vbo = VBO(ctx)
        self.program = ShaderProgram(ctx)
        self.vaos = {}

        #! Cube VAO
        self.vaos['cube'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['cube']
            )

        #! D-Rex VAO
        self.vaos['d-rex'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['d-rex']
            )
        self.vaos['d-rex-eyes'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['d-rex-eyes']
            )

        #! Cat VAO
        self.vaos['cat'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['cat']
            )

        #! Wolf VAO
        self.vaos['wolf-body'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['wolf-body']
            )
        self.vaos['wolf-claws'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['wolf-claws']
            )
        self.vaos['wolf-eyes'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['wolf-eyes']
            )
        self.vaos['wolf-fur'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['wolf-fur']
            )
        self.vaos['wolf-teeth'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['wolf-teeth']
            )

        #! Trees VAO
        self.vaos['tree-1'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['tree-1']
            )

        #! Moon VAO
        self.vaos['moon'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['moon']
            )

        #! Skybox-day VAO
        self.vaos['skybox-day'] = self.get_vao(
            program=self.program.programs['skybox'],
            vbo = self.vbo.vbos['skybox-day']
            )
        # Skybox-night VAO
        self.vaos['skybox-night'] = self.get_vao(
            program=self.program.programs['skybox'],
            vbo = self.vbo.vbos['skybox-night']
            )
        # Skybox-space VAO
        self.vaos['skybox-space'] = self.get_vao(
            program=self.program.programs['skybox'],
            vbo = self.vbo.vbos['skybox-space']
            )
        # Skybox-mountain VAO
        self.vaos['skybox-mountain'] = self.get_vao(
            program=self.program.programs['skybox'],
            vbo = self.vbo.vbos['skybox-mountain']
            )


    def get_vao(self, program, vbo):
        vao = self.ctx.vertex_array(program, [(vbo.vbo, vbo.format, *vbo.attribs)])
        return vao

    def destroy(self):
        self.vbo.destroy()
        self.program.destroy()
