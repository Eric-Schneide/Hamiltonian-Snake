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
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and direction != 'left':
            return 'right'
        elif (keys[pygame.K_LEFT] or keys[pygame.K_a]) and direction != 'right':
            return 'left'
        elif (keys[pygame.K_UP] or keys[pygame.K_w]) and direction != 'down':
            return 'up'
        elif (keys[pygame.K_DOWN] or keys[pygame.K_s]) and direction != 'up':
            return 'down'
        else:
            return direction

class Food:
    def __init__(self, size):
        self.width, self.height = size
        self.edge = self.width // 50
        self.x_position,self.y_position=self.get_coordinates(player.x_position,player.y_position)

    def get_coordinates(self, player_x, player_y, occupied=True):
        while occupied:
            food_x=self.edge*random.randint(0,self.width//50)
            food_y=self.edge*random.randint(0,self.height//50)
            occupied=False if food_x!=player_x and food_y!=player_y else True
        return food_x,food_y

pygame.init()
size = (900, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Hamiltonian Snake")
points=1
player = Snake(size)
apple=Food(size)
direction = None
run = True
while run:
    pygame.time.delay(75)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    direction=player.direction_check(direction)
    player.x_position, player.y_position = player.movement(direction)
    screen.fill((0, 0, 0))
    if player.x_position==apple.x_position and player.y_position==apple.y_position:
        points+=2
        apple.x_position,apple.y_position=apple.get_coordinates(player.x_position,player.y_position)
    pygame.draw.rect(screen, (255, 0, 0), (apple.x_position, apple.y_position, apple.edge, apple.edge))
    pygame.draw.rect(screen, (0, 255, 0), (player.x_position, player.y_position, player.edge, player.edge))




    pygame.display.update()

print(points)