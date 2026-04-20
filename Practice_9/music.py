import os
import sys
import pygame

pygame.init()
pygame.mixer.init()

# 📏 экран
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Music Player")

FPS = 60
clock = pygame.time.Clock()

# 📂 музыка папка
MUSIC_FOLDER = "music"
SUPPORTED = (".mp3", ".wav")

# 🎵 playlist жасау
playlist = []
for file in os.listdir(MUSIC_FOLDER):
    if file.endswith(SUPPORTED):
        playlist.append(file)

current = 0
playing = False

def load_track(index):
    path = os.path.join(MUSIC_FOLDER, playlist[index])
    pygame.mixer.music.load(path)

def play():
    global playing
    pygame.mixer.music.play()
    playing = True

def stop():
    global playing
    pygame.mixer.music.stop()
    playing = False

def next_track():
    global current
    current = (current + 1) % len(playlist)
    load_track(current)
    play()

def prev_track():
    global current
    current = (current - 1) % len(playlist)
    load_track(current)
    play()

# 🚀 бастапқы трек
if playlist:
    load_track(current)

font = pygame.font.SysFont("Arial", 28)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                if playing:
                    pygame.mixer.music.pause()
                    playing = False
                else:
                    pygame.mixer.music.unpause()
                    playing = True

            if event.key == pygame.K_s:
                stop()

            if event.key == pygame.K_n:
                next_track()

            if event.key == pygame.K_b:
                prev_track()

    screen.fill((30, 30, 40))

    # 🎵 мәтін
    if playlist:
        text = font.render(f"Track: {playlist[current]}", True, (255, 255, 255))
    else:
        text = font.render("No music found", True, (255, 0, 0))

    screen.blit(text, (50, 150))

    # 🎮 controls
    controls = font.render("P-play/pause  S-stop  N-next  B-back", True, (150, 150, 150))
    screen.blit(controls, (50, 250))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()