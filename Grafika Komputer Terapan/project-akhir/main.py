import pygame
import sys
import math
import random

pygame.init()

WIDTH, HEIGHT = 600, 600
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Project Akhir Grafika Komputer Terapan - Kelompok 9")
clock = pygame.time.Clock()
surface = pygame.Surface((WIDTH, HEIGHT))

try:
    background_image = pygame.image.load('background.png')
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
except:
    background_image = None

font = pygame.font.Font(None, 36)
header_font = pygame.font.Font(None, 48)

# Menu
menu_options = ['Start', 'Cara Bermain', 'About', 'Exit']
selected_menu = 0

animation_time = 0
animation_duration = 1

music_file = 'music.mp3'

pygame.mixer.music.load(music_file)
pygame.mixer.music.play(-1)  # -1 mainkan terus

volume = 0.5
pygame.mixer.music.set_volume(volume)
volume_icon = pygame.image.load('volume_icon.png')
volume_step = 0.5

rotate_angle = 0


target_rect_y = HEIGHT // 2 + selected_menu
current_rect_y = target_rect_y

running = True
menu = None
cursor_position = []
x = []
y = []
last_x = []
last_y = []
last_line = False
draw_line = True
on_reflection = True
refleksi = random.choice("12345")
jawaban = None
text = ''
draw_text = pygame.font.Font(None, 36)
quiz_surface = pygame.Surface((WIDTH, 50))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
        if menu == None:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_menu = (selected_menu - 1) % len(menu_options)
                elif event.key == pygame.K_DOWN:
                    selected_menu = (selected_menu + 1) % len(menu_options)
                elif event.key == pygame.K_RETURN:
                    if menu_options[selected_menu] == "Start":
                        game_active = True
                        menu = menu_options[selected_menu]
                        continue
                    elif menu_options[selected_menu] == "Cara Bermain":
                        menu = menu_options[selected_menu]
                    elif menu_options[selected_menu] == "About":
                        menu = menu_options[selected_menu]
                    elif menu_options[selected_menu] == "Exit":
                        running = False
                elif event.key == pygame.K_LEFT:
                    if volume_step > 0:
                        rotate_angle = (rotate_angle + 9) % 360
                        volume_step = round(volume_step - 0.05, 2)
                        volume = round(max(0, volume - 0.05), 2)
                        pygame.mixer.music.set_volume(volume)
                elif event.key == pygame.K_RIGHT:
                    if volume_step < 1:
                        rotate_angle = (rotate_angle - 9) % 360
                        volume_step = round(volume_step + 0.05, 2)
                        volume = round(min(1, volume + 0.05), 2)
                        pygame.mixer.music.set_volume(volume)
        elif menu == 'About' or menu == 'Cara Bermain':
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    surface.fill(BLACK)
                    cursor_position = []
                    x = []
                    y = []
                    last_x = []
                    last_y = []
                    last_line = False
                    draw_line = True
                    on_reflection = True
                    game_active = False
                    refleksi = random.choice("12345")
                    jawaban = None
                    menu = None
                elif event.key == pygame.K_LEFT:
                    if volume_step > 0:
                        rotate_angle = (rotate_angle + 9) % 360
                        volume_step = round(volume_step - 0.05, 2)
                        volume = round(max(0, volume - 0.05), 2)
                        pygame.mixer.music.set_volume(volume)
                elif event.key == pygame.K_RIGHT:
                    if volume_step < 1:
                        rotate_angle = (rotate_angle - 9) % 360
                        volume_step = round(volume_step + 0.05, 2)
                        volume = round(min(1, volume + 0.05), 2)
                        pygame.mixer.music.set_volume(volume)
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
                cursor_position.append(event.pos)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    draw_line = False
                elif event.key == pygame.K_BACKSPACE:
                    surface.fill(BLACK)
                    cursor_position = []
                    x = []
                    y = []
                    last_x = []
                    last_y = []
                    last_line = False
                    draw_line = True
                    on_reflection = True
                    game_active = False
                    refleksi = random.choice("12345")
                    jawaban = None
                    menu = None
                elif event.key == pygame.K_1:
                    jawaban = '1'
                elif event.key == pygame.K_2:
                    jawaban = '2'
                elif event.key == pygame.K_3:
                    jawaban = '3'
                elif event.key == pygame.K_4:
                    jawaban = '4'
                elif event.key == pygame.K_5:
                    jawaban = '5'
                elif event.key == pygame.K_LEFT:
                    if volume_step > 0:
                        rotate_angle = (rotate_angle + 9) % 360
                        volume_step = round(volume_step - 0.05, 2)
                        volume = round(max(0, volume - 0.05), 2)
                        pygame.mixer.music.set_volume(volume)
                elif event.key == pygame.K_RIGHT:
                    if volume_step < 1:
                        rotate_angle = (rotate_angle - 9) % 360
                        volume_step = round(volume_step + 0.05, 2)
                        volume = round(min(1, volume + 0.05), 2)
                        pygame.mixer.music.set_volume(volume)
    if menu != None:
        if menu == 'Start':
            screen.fill(BLACK)
            if draw_line:
                text = 'Gambar garis bebas'
                draw_text = pygame.font.Font(None, 36).render(text, True, WHITE)
                draw_text_rect= draw_text.get_rect(center=(WIDTH // 2, 50))
                surface.blit(draw_text, draw_text_rect)
            else:
                if len(text.split('\n')) > 1:
                    draw_text = [pygame.font.Font(None, 36).render(line, True, RED) for line in text.split('\n')]
                    for i, render_line in enumerate(draw_text):
                        draw_text_rect = render_line.get_rect(center=(WIDTH // 2, HEIGHT - 200 + i * 40))
                        surface.blit(render_line, draw_text_rect)
                else:
                    quiz_surface.fill(BLACK)
                    draw_text = pygame.font.Font(None, 36).render(text, True, WHITE)
                    draw_text_rect= draw_text.get_rect(center=(WIDTH//2, 30))
                    quiz_surface.blit(draw_text, draw_text_rect)
                    surface.blit(quiz_surface, (0, HEIGHT-70))

            screen.blit(surface, (0,0))

            pygame.display.set_caption("Kuis Refleksi")

            # Menggambar garis dengan DDA
            if draw_line and len(cursor_position) == 2:
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
                        draw_line = False

                    i = 0

                    x.append(round(x1))
                    y.append(round(y1))
                    while i < r:
                        x1 = x1 + xr
                        y1 = y1 + yr
                        x.append(round(x1))
                        y.append(round(y1))
                        i +=1
                    cursor_position.pop(0)

            if draw_line == False:
                for i in range(len(x)):
                    surface.set_at((x[i], y[i]), 'black')

                if refleksi == '1':
                    for point in range(len(y)):
                        y[point] = HEIGHT - y[point]
                elif refleksi == '2':
                    for point in range(len(x)):
                        x[point] = WIDTH - x[point]
                elif refleksi == '3':
                    x, y = y, x
                elif refleksi == '4':
                    if last_line == True:
                        x = last_x.copy()
                        y = last_y.copy()
                        last_line = False
                    else:
                        last_x = x.copy()
                        last_y = y.copy()
                        for point in range(len(x)):
                            x[point], y[point] = HEIGHT - y[point], WIDTH - x[point]
                        last_line = True
                elif refleksi == '5':
                    if last_line == True:
                        x = last_x.copy()
                        y = last_y.copy()
                        last_line = False
                    else:
                        last_x = x.copy()
                        last_y = y.copy()
                        for point in range(len(x)):
                            x[point], y[point] = WIDTH - x[point], HEIGHT - y[point] 
                        last_line = True

                pygame.time.delay(500)
                
            for i in range(len(x)):
                surface.set_at((x[i], y[i]), 'white')
            if jawaban != None:
                if jawaban == refleksi:
                    text = 'Jawaban benar'
                else:
                    text = 'Jawaban salah'
            else:
                text = 'Pencerminan Terhadap :\n1. sumbu x      2. sumbu y      3. garis y=x\n4. garis y=-x     5. titik asal O (0,0)\n- Ketik angka untuk menjawab -'
        elif menu == 'Cara Bermain':
            pygame.display.set_caption("About")
            surface.fill(BLACK)
            if background_image:
                surface.blit(background_image, (0, 0))
            else:
                screen.fill(BLACK)
            text = 'Tekan enter untuk memilih menu\nTekan panah atas/bawah untuk navigasi menu\nTekan panah kiri/kanan untuk kontrol volume\nKlik kiri mouse untuk membuat garis\nKetik angka 1-5 untuk menjawab pertanyaan\nTekan backspace untuk kembali ke menu'
            draw_text = [pygame.font.Font(None, 36).render(line, True, WHITE) for line in text.split('\n')]
            
            for i, render_line in enumerate(draw_text):
                draw_text_rect = render_line.get_rect(center=(WIDTH // 2, (HEIGHT // 2 - 100) + i * 50))
                surface.blit(render_line, draw_text_rect)
            screen.blit(surface, (0,0))
        elif menu == 'About':
            pygame.display.set_caption("About")
            surface.fill(BLACK)
            if background_image:
                surface.blit(background_image, (0, 0))
            else:
                screen.fill(BLACK)
            text = 'Grafika Komputer Terapan\nProject Akhir - Start Menu pada game\nKelompok 9\nMuhammad Daffa Deli Junior Irawan - 152022003\nBagus Anugrah - 152022029\nTekan backspace untuk kembali ke menu'
            draw_text = [pygame.font.Font(None, 36).render(line, True, WHITE) for line in text.split('\n')]
            for i, render_line in enumerate(draw_text):
                draw_text_rect = render_line.get_rect(center=(WIDTH // 2, (HEIGHT // 2 - 100) + i * 50))
                surface.blit(render_line, draw_text_rect)
            screen.blit(surface, (0,0))
    else:
        if background_image:
            screen.blit(background_image, (0, 0))
        else:
            screen.fill(BLACK)
        
        header_text = header_font.render("KUIS REFLEKSI", True, WHITE)
        header_text_rect = header_text.get_rect(center=(WIDTH // 2, 200))
        pygame.font.Font.set_underline(header_font, True)
        screen.blit(header_text, header_text_rect)


        # Draw menu options
        for i, option in enumerate(menu_options):
            text = font.render(option, True, WHITE if i != selected_menu else RED)

            # Animasi teks berdenyut
            if i == selected_menu:
                animation_scale = 1 + 0.1 * math.sin(animation_time *2* math.pi / animation_duration)
                # animation_scale = 1.3 # no text beat/pulse animation
                text = pygame.transform.scale(text, (int(text.get_width() * animation_scale),
                                                    int(text.get_height() * animation_scale)))

            text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + i * 50))

            # Kotak merah
            if i == selected_menu:
                rect_width = int(text.get_width()+10)
                rect_height = text.get_height() + 5
                rect_x = WIDTH // 2 - rect_width // 2
                rect_y = int(current_rect_y) - rect_height // 2

                pygame.draw.rect(screen, RED, (rect_x, rect_y, rect_width, rect_height), 2)

            screen.blit(text, text_rect)

        # Interpolasi posisi untuk transisi
        target_rect_y = HEIGHT // 2 + selected_menu * 50
        current_rect_y += (target_rect_y - current_rect_y) * 0.1
        # current_rect_y += (target_rect_y - current_rect_y) # no red rect animation

        
        # rotated_volume_icon = pygame.transform.rotate(volume_icon, rotate_angle)
        rotated_volume_icon = pygame.transform.rotozoom(volume_icon, rotate_angle, 1)
        # rotated_volume_icon = volume_icon

        volume_icon_rect = rotated_volume_icon.get_rect(center=(WIDTH - 70, HEIGHT - 70))
        screen.blit(rotated_volume_icon, volume_icon_rect)

        volume_text = font.render(f"Volume: {int(volume * 100)}%", True, WHITE)
        volume_text_rect = volume_text.get_rect(center=(WIDTH // 2, HEIGHT - 100))
        screen.blit(volume_text, volume_text_rect)

    pygame.display.flip()

    animation_time += 1 / FPS

    clock.tick(FPS)

pygame.mixer.music.stop()
pygame.quit()
sys.exit()
