import pygame
import sys
import math
from clock import MickeyClock

pygame.init()

WIDTH, HEIGHT = 700, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

clock = pygame.time.Clock()
mickey_clock = MickeyClock()

bg = pygame.image.load("images/mickeyclock.jpeg")
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
bg_rect = bg.get_rect()

center = (WIDTH // 2, HEIGHT // 2)

def draw_hand(angle, length, color, width):
    rad = math.radians(angle - 90)
    x = center[0] + math.cos(rad) * length
    y = center[1] + math.sin(rad) * length
    pygame.draw.line(screen, color, center, (x, y), width)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(bg, bg_rect)

    minutes_angle, seconds_angle = mickey_clock.get_time_angles()

    draw_hand(seconds_angle, 200, (255, 0, 0), 5)


    draw_hand(minutes_angle, 160, (0, 0, 0), 8)

    pygame.display.update()
    clock.tick(1)