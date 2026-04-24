import pygame
import sys
import random

pygame.init()

# screen setup
width, height = 500, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# FPS control
clock = pygame.time.Clock()

# colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# snake settings
block_size = 10
x = 100
y = 100
dx = block_size
dy = 0

snake_body = []
snake_length = 1

# food position
food_x = random.randrange(0, width, block_size)
food_y = random.randrange(0, height, block_size)

food_weight = random.choice([1, 2, 3]) 
food_timer = 0                          
food_lifetime = 100  

# score and level
score = 0
level = 1
speed = 10

font = pygame.font.SysFont("Verdana", 20)

game_over = False


while True:

    # game over screen
    while game_over:
        screen.fill(BLACK)
        text = font.render("Game Over! Press Q or C", True, WHITE)
        screen.blit(text, (100, 150))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

                if event.key == pygame.K_c:
                    # reset game values
                    game_over = False
                    x = 100
                    y = 100
                    snake_body = []
                    snake_length = 1
                    score = 0
                    level = 1
                    speed = 10

    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # snake movement control
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -block_size
                dy = 0
            if event.key == pygame.K_RIGHT:
                dx = block_size
                dy = 0
            if event.key == pygame.K_UP:
                dy = -block_size
                dx = 0
            if event.key == pygame.K_DOWN:
                dy = block_size
                dx = 0

    # update snake position
    x += dx
    y += dy

    # check wall collision
    if x < 0 or x >= width or y < 0 or y >= height:
        game_over = True

    screen.fill(BLACK)
    food_timer += 1

    if food_timer > food_lifetime:
        food_x = random.randrange(0, width, block_size)
        food_y = random.randrange(0, height, block_size)
        food_weight = random.choice([1, 2, 3])
        food_timer = 0


    if food_weight == 1:
        food_color = RED
    elif food_weight == 2:
        food_color = (255, 165, 0) 
    else:
        food_color = (255, 255, 0)  

    # draw food
    pygame.draw.circle(screen, food_color, (food_x + block_size//2, food_y + block_size//2), block_size//2)

    # update snake body
    snake_head = [x, y]
    snake_body.append(snake_head)

    if len(snake_body) > snake_length:
        del snake_body[0]

    # check self collision
    for block in snake_body[:-1]:
        if block == snake_head:
            game_over = True

    # draw snake
    for block in snake_body:
        pygame.draw.ellipse(screen, GREEN, (block[0], block[1], block_size, block_size))

    # check food collision
    if x == food_x and y == food_y:
        score += food_weight   
        snake_length += 1

        # ensure food does not spawn on snake
        while [food_x, food_y] in snake_body:
            food_x = random.randrange(0, width, block_size)
            food_y = random.randrange(0, height, block_size)

        food_weight = random.choice([1, 2, 3])  
        food_timer = 0 
        snake_length += 1
        score += 1

    # level system
    if score > 0 and score % 3 == 0:
        level = score // 3 + 1
        speed = 10 + (level - 1) * 2

    # display score and level
    text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.update()
    clock.tick(speed)