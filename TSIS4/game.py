import pygame
import random

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
DARK_RED = (139, 0, 0)


class SnakeGame:
    def __init__(self, w=500, h=400, block=10):
        self.w = w
        self.h = h
        self.block = block
        self.reset()

    def reset(self):
        self.x, self.y = 100, 100
        self.dx, self.dy = self.block, 0

        self.snake = []
        self.length = 1

        self.score = 0
        self.level = 1
        self.speed = 10
        self.game_over = False

        # FOOD
        self.spawn_food()

        # POISON
        self.spawn_poison()

        # POWER UPS
        self.power = None
        self.power_spawn_time = pygame.time.get_ticks()

        self.active_power = None
        self.power_start_time = 0

        self.obstacles = []

    # ---------------- SPAWN ----------------

    def spawn_food(self):
        self.food = [
            random.randrange(0, self.w, self.block),
            random.randrange(0, self.h, self.block)
        ]
        self.food_weight = random.choice([1, 2, 3])

    def spawn_poison(self):
        self.poison = [
            random.randrange(0, self.w, self.block),
            random.randrange(0, self.h, self.block)
        ]

    def spawn_power(self):
        self.power = {
            "type": random.choice(["speed", "slow", "shield"]),
            "pos": [
                random.randrange(0, self.w, self.block),
                random.randrange(0, self.h, self.block)
            ],
            "spawn_time": pygame.time.get_ticks()
        }

    def spawn_obstacles(self):
        self.obstacles = []
        for _ in range(self.level * 3):
            self.obstacles.append([
                random.randrange(0, self.w, self.block),
                random.randrange(0, self.h, self.block)
            ])

    # ---------------- INPUT ----------------

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.dx, self.dy = -self.block, 0
            if event.key == pygame.K_RIGHT:
                self.dx, self.dy = self.block, 0
            if event.key == pygame.K_UP:
                self.dx, self.dy = 0, -self.block
            if event.key == pygame.K_DOWN:
                self.dx, self.dy = 0, self.block

    # ---------------- UPDATE ----------------

    def update(self):
        if self.game_over:
            return

        # move snake
        self.x += self.dx
        self.y += self.dy

        # wall collision
        if self.x < 0 or self.x >= self.w or self.y < 0 or self.y >= self.h:
            self.game_over = True

        head = [self.x, self.y]
        self.snake.append(head)

        if len(self.snake) > self.length:
            self.snake.pop(0)

        # self collision
        if head in self.snake[:-1]:
            self.game_over = True

        # food
        if head == self.food:
            self.score += self.food_weight
            self.length += 1
            self.spawn_food()

        # poison
        if head == self.poison:
            self.length -= 2
            self.spawn_poison()
            if self.length <= 1:
                self.game_over = True

        # ---------------- POWER UPS LOGIC ----------------

        # spawn power-up ONLY if none exists
        if self.power is None:
            self.spawn_power()

        # remove after 8 seconds if not collected
        if self.power and pygame.time.get_ticks() - self.power["spawn_time"] > 8000:
            self.power = None

        # collect power-up
        if self.power and head == self.power["pos"]:
            self.active_power = self.power["type"]
            self.power_start_time = pygame.time.get_ticks()
            self.power = None

        # effects
        if self.active_power == "speed":
            self.speed = 18
        elif self.active_power == "slow":
            self.speed = 5

        # reset power after 5 sec
        if self.active_power and pygame.time.get_ticks() - self.power_start_time > 5000:
            self.active_power = None
            self.speed = 10

        # ---------------- LEVEL + OBSTACLES ----------------

        self.level = self.score // 5 + 1

        if self.level >= 3 and not self.obstacles:
            self.spawn_obstacles()

        if head in self.obstacles:
            self.game_over = True

    # ---------------- DRAW ----------------

    def draw(self, screen, font, best):
        screen.fill(BLACK)

        # snake
        for s in self.snake:
            pygame.draw.rect(screen, GREEN, (s[0], s[1], self.block, self.block))

        # food
        color = RED if self.food_weight == 1 else ORANGE if self.food_weight == 2 else YELLOW
        pygame.draw.rect(screen, color, (*self.food, self.block, self.block))

        # poison
        pygame.draw.rect(screen, DARK_RED, (*self.poison, self.block, self.block))

        # power-up
        if self.power:
            if self.power["type"] == "speed":
                c = (0, 255, 255)
            elif self.power["type"] == "slow":
                c = (255, 0, 255)
            else:
                c = WHITE

            pygame.draw.rect(screen, c, (*self.power["pos"], self.block, self.block))

        # obstacles
        for o in self.obstacles:
            pygame.draw.rect(screen, (120, 120, 120), (*o, self.block, self.block))

        # UI
        text = font.render(
            f"Score: {self.score} Level: {self.level} Best: {best}",
            True,
            WHITE
        )
        screen.blit(text, (10, 10))