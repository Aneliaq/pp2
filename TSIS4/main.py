import pygame
import sys
from game import SnakeGame
from db import *

pygame.init()

W, H = 500, 400
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Verdana", 18)

create_tables()

# ---------- STATES ----------
state = "menu"
username = ""
player_id = None

game = SnakeGame()
saved = False


# ---------- BUTTON CLASS ----------
class Button:
    def __init__(self, x, y, w, h, text):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text

    def draw(self):
        pygame.draw.rect(screen, (70,70,70), self.rect)
        txt = font.render(self.text, True, (255,255,255))
        screen.blit(txt, (self.rect.x + 20, self.rect.y + 10))

    def click(self, pos):
        return self.rect.collidepoint(pos)


# ---------- BUTTONS ----------
play_btn = Button(180, 140, 140, 40, "PLAY")
lead_btn = Button(180, 190, 150, 40, "LEADERBOARD")
quit_btn = Button(180, 240, 140, 40, "QUIT")


# ---------- LEADERBOARD ----------
def draw_leaderboard():
    screen.fill((0,0,0))
    data = get_top_scores()

    title = font.render("TOP 10 PLAYERS", True, (255,255,255))
    screen.blit(title, (160, 20))

    y = 60
    for i, r in enumerate(data):
        t = font.render(f"{i+1}. {r[0]} | {r[1]} | lvl {r[2]}", True, (255,255,255))
        screen.blit(t, (80, y))
        y += 25

    back = font.render("CLICK BACKSPACE TO RETURN", True, (255,255,255))
    screen.blit(back, (100, 350))


# ---------- MENU ----------
def draw_menu():
    screen.fill((0,0,0))

    title = font.render("ENTER NAME:", True, (255,255,255))
    screen.blit(title, (180, 80))

    name = font.render(username, True, (255,255,255))
    screen.blit(name, (180, 110))

    play_btn.draw()
    lead_btn.draw()
    quit_btn.draw()


# ---------- GAME DRAW ----------
def draw_game():
    best = get_best_score(player_id)
    game.draw(screen, font, best)


# ---------- MAIN LOOP ----------
while True:

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # ---------- MENU ----------
        if state == "menu":

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                elif e.key == pygame.K_RETURN:
                    player_id = get_player(username)
                    game.reset()
                    state = "game"
                else:
                    username += e.unicode

            if e.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                if play_btn.click(pos):
                    player_id = get_player(username)
                    game.reset()
                    state = "game"

                if lead_btn.click(pos):
                    state = "leaderboard"

                if quit_btn.click(pos):
                    pygame.quit()
                    sys.exit()

        # ---------- GAME ----------
        elif state == "game":
            game.handle_input(e)

        # ---------- LEADERBOARD ----------
        elif state == "leaderboard":
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_BACKSPACE:
                    state = "menu"

    # ---------- STATES ----------
    if state == "menu":
        draw_menu()

    elif state == "game":
        game.update()

        if game.game_over and not saved:
            save_score(player_id, game.score, game.level)
            saved = True

        if game.game_over:
            state = "menu"
            saved = False

        draw_game()

    elif state == "leaderboard":
        draw_leaderboard()

    pygame.display.update()
    clock.tick(game.speed if state=="game" else 60)