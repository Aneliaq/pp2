import pygame
import sys
from datetime import datetime
from tools import flood_fill, TextManager

pygame.init()

# screen
width, height = 950, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("TSIS2 Paint")

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (160, 32, 240)
PINK = (255, 105, 180)
LIGHT_BLUE = (135, 206, 250)
GRAY = (200, 200, 200)

# canvas
canvas = pygame.Surface((width, height))
canvas.fill(WHITE)

# tools
color = BLACK
tool = "brush"
drawing = False
radius = 5

last_pos = None
start_pos = None
preview_end = None

# TEXT MANAGER (from tools.py)
text_manager = TextManager()
text_input = ""
text_pos = None
typing = False

font = pygame.font.SysFont("Arial", 18)
text_font = pygame.font.SysFont("Arial", 24)

# buttons
buttons = {
    "brush": pygame.Rect(10, 10, 80, 35),
    "eraser": pygame.Rect(95, 10, 80, 35),
    "circle": pygame.Rect(180, 10, 80, 35),
    "rect": pygame.Rect(265, 10, 80, 35),
    "square": pygame.Rect(350, 10, 80, 35),
    "r_tri": pygame.Rect(435, 10, 80, 35),
    "e_tri": pygame.Rect(520, 10, 80, 35),
    "rhomb": pygame.Rect(605, 10, 80, 35),

    "PU": pygame.Rect(690, 10, 40, 35),
    "PI": pygame.Rect(735, 10, 40, 35),
    "LB": pygame.Rect(780, 10, 40, 35),
    "K": pygame.Rect(825, 10, 40, 35),

    "clear": pygame.Rect(870, 10, 70, 35),

    "line": pygame.Rect(10, 50, 80, 35),
    "fill": pygame.Rect(95, 50, 80, 35),
    "text": pygame.Rect(180, 50, 80, 35),
}

clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # mouse down
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            drawing = True

            if tool == "line":
                start_pos = (mx, my)
                preview_end = (mx, my)

            if tool == "text":
                text_pos = (mx, my)
                typing = True
                text_input = ""

            if tool == "fill":
                flood_fill(canvas, mx, my, color)

            for name, rect in buttons.items():
                if rect.collidepoint(mx, my):

                    if name in ["brush", "eraser", "circle", "rect", "square",
                                "r_tri", "e_tri", "rhomb", "line", "fill", "text"]:
                        tool = name

                    if name == "clear":
                        canvas.fill(WHITE)

                    if name == "PU":
                        color = PURPLE
                    if name == "PI":
                        color = PINK
                    if name == "LB":
                        color = LIGHT_BLUE
                    if name == "K":
                        color = BLACK

        # keyboard
        if event.type == pygame.KEYDOWN:

            # SAVE
            if event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                filename = datetime.now().strftime("paint_%Y-%m-%d_%H-%M-%S.png")
                pygame.image.save(canvas, filename)
                print("Saved:", filename)

            # brush size
            if event.key == pygame.K_1:
                radius = 2
            elif event.key == pygame.K_2:
                radius = 5
            elif event.key == pygame.K_3:
                radius = 10

            # text input
            if typing and tool == "text":
                if event.key == pygame.K_RETURN:
                    text_manager.add_text(text_input, text_pos, color)
                    typing = False

                elif event.key == pygame.K_ESCAPE:
                    typing = False

                else:
                    text_input += event.unicode

        # mouse up
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            last_pos = None

            if tool == "line" and start_pos:
                mx, my = pygame.mouse.get_pos()
                pygame.draw.line(canvas, color, start_pos, (mx, my), radius)
                start_pos = None
                preview_end = None

        # mouse move
        if event.type == pygame.MOUSEMOTION:
            mx, my = pygame.mouse.get_pos()
            if tool == "line" and drawing and start_pos:
                preview_end = (mx, my)

    mx, my = pygame.mouse.get_pos()

    # drawing
    if drawing and my > 50:

        if tool == "brush":
            if last_pos:
                pygame.draw.line(canvas, color, last_pos, (mx, my), radius)
            last_pos = (mx, my)

        elif tool == "eraser":
            pygame.draw.circle(canvas, WHITE, (mx, my), radius * 2)

        elif tool == "circle":
            pygame.draw.circle(canvas, color, (mx, my), radius * 6)

        elif tool == "rect":
            pygame.draw.rect(canvas, color, (mx, my, radius * 8, radius * 8))

        elif tool == "square":
            pygame.draw.rect(canvas, color, (mx, my, radius * 8, radius * 8))

    # preview line
    if tool == "line" and start_pos and preview_end:
        pygame.draw.line(screen, color, start_pos, preview_end, radius)

    # draw canvas
    screen.blit(canvas, (0, 0))

    # live text preview
    if tool == "text" and typing and text_pos:
        img = text_font.render(text_input, True, color)
        screen.blit(img, text_pos)

    # saved texts (from tools.py)
    text_manager.draw(screen, text_font)

    # buttons
    for name, rect in buttons.items():
        pygame.draw.rect(screen, GRAY, rect)
        text = font.render(name, True, BLACK)
        screen.blit(text, text.get_rect(center=rect.center))

    pygame.display.update()
    clock.tick(120)