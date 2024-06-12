import pygame
import sys
import copy

class Game:

    def __init__(self):
        pygame.init()

        pygame.display.set_caption('Algoritma Scaling')
        self.screen = pygame.display.set_mode((1366,768))

        self.screen.fill((0,0,0))
        # pygame.draw.lines(self.screen, 'white', True, new_points)
        # pygame.display.flip()

        self.clock = pygame.time.Clock()


    def run(self, points, scaling_x, scaling_y):
        old_points = copy.deepcopy(points)
        x = 1
        y = 1

        # def centroid(vertices):
        #     x, y = 0, 0
        #     n = len(vertices)
        #     signed_area = 0
        #     for i in range(len(vertices)):
        #         x0, y0 = vertices[i]
        #         x1, y1 = vertices[(i + 1) % n]
        #         # shoelace formula
        #         area = (x0 * y1) - (x1 * y0)
        #         signed_area += area
        #         x += (x0 + x1) * area
        #         y += (y0 + y1) * area
        #     signed_area *= 0.5
        #     x /= 6 * signed_area
        #     y /= 6 * signed_area
        #     return x, y

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            if x <= scaling_x:
                for tup in range(len(points)):
                    points[tup][0] *= x
                x+=1

            if y <= scaling_y:
                for tup in range(len(points)):
                    points[tup][1] *= y
                y+=1
        
            
            pygame.time.delay(1000)
            self.screen.fill((0,0,0))

            pygame.draw.lines(self.screen, 'white', True, points)

            if x <= scaling_x or y <= scaling_y:
                points = copy.deepcopy(old_points)
            pygame.display.update()
            self.clock.tick(60) # 60fps


print("Program Scaling")
print("""Kelompok 9
Muhammad Daffa Deli Junior Irawan - 152022003
Bagus Anugrah - 152022029
""")

banyak_points = int(input("Masukkan banyak titik: "))
points = []

for i in range(1, banyak_points+1):
    x = int(input(f"Koordinat x dari point {i}: "))
    y = int(input(f"Koordinat y dari point {i}: "))
    points.append([x,y])

print()

scaling_x = int(input("Banyak scaling x: "))
scaling_y = int(input("Banyak scaling y: "))

Game().run(copy.deepcopy(points), scaling_x, scaling_y)