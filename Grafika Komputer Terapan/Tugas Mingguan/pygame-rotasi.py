import pygame
import sys
import math
import copy

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('Algoritma Rotasi')
        self.screen = pygame.display.set_mode((500,500))
        self.screen.fill((0,0,0))

        self.clock = pygame.time.Clock()

    def run(self, points, pivot_x, pivot_y, derajat):
        old_points = copy.deepcopy(points)
        derajat_radians = math.radians(derajat)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            pygame.draw.lines(self.screen, 'white', True, points)
            pygame.display.flip()
            pygame.time.delay(1000)

            for tup in range(len(points)):
                x_points = points[tup][0]
                y_points = points[tup][1]
                points[tup][0] = round(pivot_x + (x_points - pivot_x) * math.cos(derajat_radians) - (y_points - pivot_y) * math.sin(derajat_radians))
                points[tup][1] = round(pivot_y + (x_points - pivot_x) * math.sin(derajat_radians) + (y_points - pivot_y) * math.cos(derajat_radians))

            pygame.draw.lines(self.screen, 'white', True, points)
            pygame.display.flip()
            pygame.time.delay(1000)
            
            self.screen.fill((0,0,0))
            points = copy.deepcopy(old_points)
            pygame.display.update()
            self.clock.tick(60) # 60fps


print("Program Rotasi")
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

pivot_x = int(input("Titik pivot x: "))
pivot_y = int(input("Titik pivot y: "))
derajat = int(input("Banyak derajat perputaran: "))

Game().run(copy.deepcopy(points), pivot_x, pivot_y, derajat)