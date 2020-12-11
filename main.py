import pygame
import random


class Snake:
    def __init__(self, size, width=None, height=None):
        self.width, self.height = size
        self.edge = self.width // 50
        self.x_position = 0
        self.y_position = 0
        self.velocity = self.edge


pygame.init()
size = (900, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Hamiltonian Snake")
player = Snake(size)
direction = None
run = True
while run:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and direction != 'left':
        direction = 'right'
    elif keys[pygame.K_LEFT] and direction != 'right':
        direction = 'left'
    elif keys[pygame.K_UP] and direction != 'down':
        direction = 'up'
    elif keys[pygame.K_DOWN] and direction != 'up':
        direction = 'down'
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 255, 0), (player.x_position, player.y_position, player.edge, player.edge))
    pygame.display.update()
    if direction == 'right' and player.x_position < player.width - player.edge:
        player.x_position += player.velocity
    elif direction == 'left' and player.x_position > 0:
        player.x_position -= player.velocity
    elif direction == 'up' and player.y_position > 0:
        player.y_position -= player.velocity
    elif direction == 'down' and player.y_position + player.velocity < player.height - player.edge:
        player.y_position += player.velocity
