import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1000, 800
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Project Akhir Grafika Komputer Terapan - Kelompok 9")
clock = pygame.time.Clock()

# Background image (replace 'background.jpg' with the path to your image)
try:
    background_image = pygame.image.load('background.png')
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
except pygame.error:
    background_image = None

# Fonts
font = pygame.font.Font(None, 36)
header_font = pygame.font.Font(None, 48)

# Menu options
menu_options = ['Start', 'About', 'Exit']
selected_menu = 0

# Animation variables
animation_time = 0
animation_duration = 0.5  # in seconds

# Music file (replace 'music.mp3' with the path to your music file)
music_file = 'music.mp3'

# Load music and play it
pygame.mixer.music.load(music_file)
pygame.mixer.music.play(-1)  # -1 means play indefinitely

# Volume control variables
volume = 0.5  # initial volume
pygame.mixer.music.set_volume(volume)
volume_icon = pygame.image.load('volume_icon.png')  # replace with your volume icon
volume_step = 0.5

# Rotation variables for volume icon
rotate_angle = 0  # initial rotation angle

# Transition variables
target_rect_y = HEIGHT // 2 + selected_menu
current_rect_y = target_rect_y

# Main loop
running = True
game_active = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                selected_menu = (selected_menu - 1) % len(menu_options)
            elif event.key == pygame.K_DOWN:
                selected_menu = (selected_menu + 1) % len(menu_options)
            elif event.key == pygame.K_RETURN:
                if menu_options[selected_menu] == "Start":
                    game_active = True
                elif menu_options[selected_menu] == "About":
                    print("Grafika Komputer Terapan")
                    print("Project Akhir - Start Menu pada Game")
                    print('Kelompok 9')
                    print('Muhammad Daffa Deli Junior Irawan - 152022003')
                    print('Bagus Anugrah - 152022029\n')
                elif menu_options[selected_menu] == "Exit":
                    running = False

                # Reset animation time when menu option is selected
                # animation_time = 0

            # Volume control with left and right arrow keys
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

    if game_active:
        screen.fill(WHITE)  # Clear the screen
        pygame.display.set_caption("Game Window")
    else:
        # Draw background
        if background_image:
            screen.blit(background_image, (0, 0))
        else:
            screen.fill(WHITE)

        # Draw header "START MENU" with underline
        header_text = header_font.render("START MENU", True, WHITE)
        header_text_rect = header_text.get_rect(center=(WIDTH // 2, 200))
        pygame.font.Font.set_underline(header_font, True)
        screen.blit(header_text, header_text_rect)


        # Draw menu options
        for i, option in enumerate(menu_options):
            text = font.render(option, True, WHITE if i != selected_menu else RED)

            # Calculate animation scale based on a sine function for the selected menu
            if i == selected_menu:
                animation_scale = 1 + 0.1 * math.sin(animation_time * 2 * math.pi / animation_duration)
                text = pygame.transform.scale(text, (int(text.get_width() * animation_scale),
                                                    int(text.get_height() * animation_scale)))

            text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + i * 50))

            # Draw the rectangle background for the selected menu
            if i == selected_menu:
                rect_width = int(1.2 * text.get_width())
                rect_height = text.get_height()
                rect_x = WIDTH // 2 - rect_width // 2
                rect_y = int(current_rect_y) - rect_height // 2

                pygame.draw.rect(screen, RED, (rect_x, rect_y, rect_width, rect_height), 2)

            screen.blit(text, text_rect)

        # Interpolate the position of the rectangle for a smooth transition
        target_rect_y = HEIGHT // 2 + selected_menu * 50
        current_rect_y += (target_rect_y - current_rect_y) * 0.1

        
        # rotated_volume_icon = pygame.transform.rotate(volume_icon, rotate_angle)
        rotated_volume_icon = pygame.transform.rotozoom(volume_icon, rotate_angle, 1)

        # Set maximum width and height for the volume icon
        # max_size = 100
        # if rotated_volume_icon.get_width() > max_size or rotated_volume_icon.get_height() > max_size:
        #     rotated_volume_icon = pygame.transform.scale(rotated_volume_icon, (max_size, max_size))

        # Position the volume icon at the bottom right
        volume_icon_rect = rotated_volume_icon.get_rect(center=(WIDTH - 70, HEIGHT - 70))
        screen.blit(rotated_volume_icon, volume_icon_rect)

        # Draw volume level text
        volume_text = font.render(f"Volume: {int(volume * 100)}%", True, WHITE)
        volume_text_rect = volume_text.get_rect(center=(WIDTH // 2, HEIGHT - 100))
        screen.blit(volume_text, volume_text_rect)

    # Update the display
    pygame.display.flip()

    # Update animation time
    animation_time += 1 / FPS

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.mixer.music.stop()
pygame.quit()
sys.exit()
