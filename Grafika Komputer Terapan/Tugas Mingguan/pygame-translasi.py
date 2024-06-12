import pygame
import sys

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('Algoritma Translasi')
        self.screen = pygame.display.set_mode((700,700))

        self.screen.fill((0,0,0))
        pygame.draw.lines(self.screen, 'white', True, points)
        pygame.display.flip()

        self.clock = pygame.time.Clock()
    def run(self, points, translation_x, translation_y):
        x = 0
        y = 0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            
            if x <= translation_x:
                pygame.time.delay(500)
                self.screen.fill((0,0,0))
                for tup in range(len(points)):
                    points[tup][0] += x
                x+=1

            if y <= translation_y:
                pygame.time.delay(500)
                self.screen.fill((0,0,0))
                for tup in range(len(points)):
                    points[tup][1] += y
                y+=1

            pygame.draw.lines(self.screen, 'white', True, points)
            pygame.display.update()
            self.clock.tick(60) # 60fps


print("Program Translasi")
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

translation_x = int(input("Masukkan pergeseran koordinat x: "))
translation_y = int(input("Masukkan pergeseran koordinat y: "))

Game().run(points, translation_x, translation_y)