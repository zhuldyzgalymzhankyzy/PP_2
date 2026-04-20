import pygame
import sys
import datetime

pygame.init()

WIDTH, HEIGHT = 800, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

clock = pygame.time.Clock()

# 📂 суреттер
clock_img = pygame.image.load("clock.png").convert_alpha()
mickey = pygame.image.load("mickey.png").convert_alpha()
right_hand = pygame.image.load("right.png").convert_alpha()
left_hand = pygame.image.load("left.png").convert_alpha()

# 📏 размер
clock_img = pygame.transform.scale(clock_img, (800, 600))
mickey = pygame.transform.scale(mickey, (300, 300))
right_hand = pygame.transform.scale(right_hand, (80, 120))
left_hand = pygame.transform.scale(left_hand, (40, 120))

CENTER = (WIDTH // 2, HEIGHT // 2)

# 🧠 айналдыру функциясы (pivot)
def rotate_pivot(image, angle, pos, pivot):
    rect = image.get_rect(topleft=(pos[0] - pivot[0], pos[1] - pivot[1]))
    offset = pygame.math.Vector2(pos) - rect.center
    rotated_offset = offset.rotate(-angle)

    rotated_image = pygame.transform.rotate(image, angle)
    new_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    new_rect = rotated_image.get_rect(center=new_center)
    return rotated_image, new_rect

# 📍 қол позициялары (иық)
RIGHT_POS = (CENTER[0] + 0, CENTER[1] + 0)
LEFT_POS = (CENTER[0] - 0, CENTER[1] + 0)

# 📍 pivot (иық нүктесі)
RIGHT_PIVOT = (40, 108)
LEFT_PIVOT = (20, 108)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    # 🖼 сағат
    screen.blit(clock_img, clock_img.get_rect(center=CENTER))

    # 🐭 микки
    screen.blit(mickey, mickey.get_rect(center=CENTER))
    pygame.draw.circle(screen, (255, 0, 0), RIGHT_POS, 5)
    pygame.draw.circle(screen, (255, 0, 0), LEFT_POS, 5)
    # ⏰ уақыт
    now = datetime.datetime.now()
    sec = now.second
    minute = now.minute

    sec_angle = -sec * 6
    min_angle = -(minute + sec / 60) * 6

    # 🔴 оң қол (секунд)
    r_img, r_rect = rotate_pivot(right_hand, sec_angle, RIGHT_POS, RIGHT_PIVOT)
    screen.blit(r_img, r_rect)

    # ⚫ сол қол (минут)
    l_img, l_rect = rotate_pivot(left_hand, min_angle, LEFT_POS, LEFT_PIVOT)
    screen.blit(l_img, l_rect)

    # ⭕ центр
    pygame.draw.circle(screen, (0, 0, 0), CENTER, 5)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()