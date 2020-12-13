import pygame
import random


class Snake:
    def __init__(self, size):
        self.width, self.height = size
        self.edge = self.width // 50
        self.x_position = 0
        self.y_position = 0
        self.velocity = self.edge

    def movement(self, direction):
        if direction == 'right' and self.x_position < self.width - self.edge:
            self.x_position += self.velocity

        elif direction == 'left' and self.x_position > 0:
            self.x_position -= self.velocity

        elif direction == 'up' and self.y_position > 0:
            self.y_position -= self.velocity

        elif direction == 'down' and self.y_position + self.velocity < self.height - self.edge:
            self.y_position += self.velocity

        return self.x_position, self.y_position

    def direction_check(self,direction):
        if keys[pygame.K_RIGHT] and direction != 'left':
            return 'right'
        elif keys[pygame.K_LEFT] and direction != 'right':
            return 'left'
        elif keys[pygame.K_UP] and direction != 'down':
            return 'up'
        elif keys[pygame.K_DOWN] and direction != 'up':
            return 'down'
        else:
            return direction


pygame.init()
size = (900, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Hamiltonian Snake")
keys = pygame.key.get_pressed()
player = Snake(size)
direction = None
run = True
while run:
    pygame.time.delay(75)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    direction=player.direction_check(direction)
    player.x_position, player.y_position = player.movement(direction)
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 255, 0), (player.x_position, player.y_position, player.edge, player.edge))
    pygame.display.update()

