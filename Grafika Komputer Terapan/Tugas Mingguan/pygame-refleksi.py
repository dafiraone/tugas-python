import pygame
import sys
import copy

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('Algoritma Refleksi')
        self.screen = pygame.display.set_mode((500,500))
        self.screen.fill((0,0,0))

        self.clock = pygame.time.Clock()

    def run(self, points, refleksi):
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if pencerminan == 1:
                for tup in range(len(points)):
                    y_points = points[tup][1]
                    points[tup][1] = -y_points
            elif pencerminan == 2:
                for tup in range(len(points)):
                    x_points = points[tup][0]
                    points[tup][0] = -x_points
            elif pencerminan == 3:
                for tup in range(len(points)):
                    x_points = points[tup][0]
                    y_points = points[tup][1]
                    points[tup][0], points[tup][1] = y_points, x_points
            elif pencerminan == 4:
                for tup in range(len(points)):
                    x_points = points[tup][0]
                    y_points = points[tup][1]
                    points[tup][0], points[tup][1] = -y_points, -x_points


            mid_coor = copy.deepcopy(points)
            for tup in range(len(points)):
                x_points = points[tup][0]
                y_points = points[tup][1]
                mid_coor[tup] = [x_points + 500 // 2, 500 // 2 - y_points]

            pygame.draw.lines(self.screen, 'white', True, mid_coor)
            pygame.display.flip()
            pygame.time.delay(500)
            self.screen.fill((0,0,0))
            pygame.display.update()
            print(points)
            self.clock.tick(60) # 60fps


print("Program Refleksi")
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

pencerminan = int(input("""Teknik refleksi:
    1. Pencerminan terhadap sumbu x
    2. Pencerminan terhadap sumbu y
    3. Pencerminan terhadap garis y=x
    4. Pencerminan terhadap garis y=-x
    5. Pencerminan terhadap garis x=h
    6. Pencerminan terhadap garis y=k
    7. Pencerminan terhadap titik asal O (0,0)

Masukkan teknik refleksi (dengan nomor): """))

Game().run(points, refleksi=pencerminan)