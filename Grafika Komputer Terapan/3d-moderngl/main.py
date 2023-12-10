import pygame as pg
import moderngl as mgl
import sys
from model import *
from camera import Camera

class GraphicsEngine:
    def __init__(self, win_size=(1000, 1000)):
        # inisialisasi modul pygame
        pg.init()
        # ukuran window
        self.WIN_SIZE = win_size
        # mengatur atribut opengl
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3) # versi major dari opengl yang akan digunakan
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3) # versi minor dari opengl yang akan digunakan (opengl 3.3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE) # profile masknya profile core akan menghiraukan fungsi yang deprecated/usang
        # membuat opengl context
        pg.display.set_mode(self.WIN_SIZE, flags=pg.OPENGL | pg.DOUBLEBUF)
        # mouse settings
        pg.event.set_grab(True)
        pg.mouse.set_visible(False)
        # detect dan pakai context opengl yang telah dibuat
        self.ctx = mgl.create_context()
        # self.ctx.front_face = 'cw'
        self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE)
        # membuat objek untuk tracking waktu (digunakan untuk framerate dan waktu delta)
        self.clock = pg.time.Clock()
        self.time = 0
        self.delta_time = 0
        # camera
        self.camera = Camera(self)
        # scene
        # self.scene = Triangle(self)
        self.scene = Cube(self)

    # fungsi cek event yang berlanngsung
    def check_events(self):
        for event in pg.event.get():
            # program akan berhenti jika user menekan tombol x atau tombol escape
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                # menghaous scene
                self.scene.destroy()
                pg.quit()
                sys.exit()
    
    def render(self):
        # framebuffer
        self.ctx.clear(color=(0.08, 0.16, 0.18)) # 0 - 255 = 0 - 1
        # render scene
        self.scene.render()
        # ganti buffer
        pg.display.flip()
    
    def get_time(self):
        self.time = pg.time.get_ticks() * 0.001

    def run(self):
        while True:
            self.get_time()
            self.check_events()
            self.camera.update()
            self.render()
            self.delta_time = self.clock.tick(30) # refresh rate 30 fps

if __name__ == '__main__':
    app = GraphicsEngine()
    app.run()