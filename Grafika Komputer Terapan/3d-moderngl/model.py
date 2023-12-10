import numpy as np
import glm
import pygame as pg

class Cube:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx
        self.vbo = self.get_vbo()
        self.shader_program = self.get_shader_program('default') # nama shader
        self.vao = self.get_vao()
        self.m_model = self.get_model_matrix()
        self.texture = self.get_texture(path='textures/img.png')
        self.on_init()
    
    # load texture untuk gambar kotak kayu
    def get_texture(self, path):
        texture = pg.image.load(path).convert()
        texture = pg.transform.flip(texture,flip_x=False, flip_y=True)
        texture = self.ctx.texture(size=texture.get_size(), components=3, data=pg.image.tostring(texture, 'RGB'))
        return texture
    
    def update(self):
        rotation_speed = 0.05
        rotation_axis = glm.vec3(0, 0, 1)  # x,y,z

        # pembuatan matriks rotasi
        c = glm.cos(rotation_speed)
        s = glm.sin(rotation_speed)
        t = 1 - c

        rotation_matrix = glm.mat4(
            glm.vec4(t * rotation_axis.x * rotation_axis.x + c, t * rotation_axis.x * rotation_axis.y - s * rotation_axis.z, t * rotation_axis.x * rotation_axis.z + s * rotation_axis.y, 0.0),
            glm.vec4(t * rotation_axis.x * rotation_axis.y + s * rotation_axis.z, t * rotation_axis.y * rotation_axis.y + c, t * rotation_axis.y * rotation_axis.z - s * rotation_axis.x, 0.0),
            glm.vec4(t * rotation_axis.x * rotation_axis.z - s * rotation_axis.y, t * rotation_axis.y * rotation_axis.z + s * rotation_axis.x, t * rotation_axis.z * rotation_axis.z + c, 0.0),
            glm.vec4(0.0, 0.0, 0.0, 1.0)
        )

        # menerapkan matriks model dengan rotasi
        self.m_model = rotation_matrix * self.m_model

        # # pembuatan matriks translasi
        translation_speed = 0.1
        translation = glm.vec3(1, 0, 0)  # x, y, z
        translation_matrix = glm.mat4(
            glm.vec4(1, 0, 0, 0),
            glm.vec4(0, 1, 0, 0),
            glm.vec4(0, 0, 1, 0),
            glm.vec4(translation_speed * translation.x, translation_speed * translation.y, translation_speed * translation.z, 1)
        )

        # menerapkan matriks model dengan translasi
        self.m_model = translation_matrix * self.m_model


        self.shader_program['m_model'].write(self.m_model)
        self.shader_program['m_view'].write(self.app.camera.m_view)

    def get_model_matrix(self):
        m_model = glm.mat4()
        return m_model
    
    def on_init(self):
        # texture
        self.shader_program['u_texture_0'] = 0
        self.texture.use()
        # mvp
        self.shader_program['m_proj'].write(self.app.camera.m_proj)
        self.shader_program['m_view'].write(self.app.camera.m_view)
        self.shader_program['m_model'].write(self.m_model)

    def render(self):
        self.update()
        self.vao.render()

    # menghapus semua object yang dibuat
    def destroy(self):
        self.vbo.release()
        self.shader_program.release()
        self.vao.release()
    
    # vertex array object (setelah vbo dan shader)
    def get_vao(self):
        vao = self.ctx.vertex_array(self.shader_program, 
                                                # buffer format   nama atribut
                                    [(self.vbo, '2f 3f', 'in_texcoord_0', 'in_position')])
        return vao

    def get_vertex_data(self):
        vertices = [(-1,-1,1), (1,-1,1), (1,1,1), (-1,1,1),
                    (-1,1,-1), (-1,-1,-1), (1,-1,-1), (1,1,-1)]
        indices = [
            (0,2,3), (0,1,2),
            (1,7,2), (1,6,7),
            (6,5,4), (4,7,6),
            (3,4,5), (3,5,0),
            (3,7,4), (3,2,7),
            (0,6,1), (0,5,6)]
        
        vertex_data = self.get_data(vertices, indices)

        tex_coord = [(0,0), (1,0), (1,1), (0,1)]
        tex_coord_indices = [(0,2,3), (0,1,2),
                             (0,2,3), (0,1,2),
                             (0,1,2), (2,3,0),
                             (2,3,0), (2,0,1),
                             (0,2,3), (0,1,2),
                             (3,1,2), (3,0,1)]
        tex_coord_data = self.get_data(tex_coord, tex_coord_indices)

        vertex_data = np.hstack([tex_coord_data, vertex_data])
        return vertex_data
    
    @staticmethod
    def get_data(vertices, indices):
        data = [vertices[ind] for triangle in indices for ind in triangle]
        return np.array(data, dtype='f4')
    
    # vertex buffer object untuk dikirimkan ke memori gpu
    def get_vbo(self):
        vertex_data = self.get_vertex_data()
        vbo = self.ctx.buffer(vertex_data)
        return vbo
    
    # memanggil program shader
    def get_shader_program(self, shader_name):
        with open(f'shaders/{shader_name}.vert') as file:
            vertex_shader = file.read()

        with open(f'shaders/{shader_name}.frag') as file:
            fragment_shader = file.read()
        
        # compile shader di cpu agar bisa digunakan di gpu
        program = self.ctx.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)
        return program
