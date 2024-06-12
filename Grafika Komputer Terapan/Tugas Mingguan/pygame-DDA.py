import pygame
import sys

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('Algoritma DDA')
        self.screen = pygame.display.set_mode((500,500))
        self.surface = pygame.Surface((500,500))
        # self.surface.fill((0,0,255))

        self.clock = pygame.time.Clock()
    def run(self):
        cursor_position = []
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    print(event.pos)
                    cursor_position.append(event.pos)

            self.screen.fill((0,0,0))
            self.screen.blit(self.surface, (0,0))


            if len(cursor_position) == 2:
                print(cursor_position)
                x1 = cursor_position[0][0]
                x2 = cursor_position[1][0]
                y1 = cursor_position[0][1]
                y2 = cursor_position[1][1]

                dx = x2 - x1
                dy = y2 - y1

                if abs(dx) > abs(dy):
                    r = abs(dx)
                else:
                    r = abs(dy)
                    
                try:
                    xr = dx/r
                    yr = dy/r
                except:
                    continue

                i = 0

                x = []
                y = []

                x.append(round(x1))
                y.append(round(y1))
                while i < r:
                    x1 = x1 + xr
                    y1 = y1 + yr
                    x.append(round(x1))
                    y.append(round(y1))
                    i +=1

                for i in range(len(x)):
                    self.surface.set_at((x[i],y[i]), "white")
                cursor_position.pop(0)

            pygame.display.update()
            self.clock.tick(60) # 60fps

Game().run()