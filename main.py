import pygame
import random
import sys


class Snake:
    '''
    The player class
    '''
    def __init__(self, size):
        self.width, self.height = size
        self.edge = self.width // 50
        self.x_position = 0
        self.y_position = 0
        self.velocity = self.edge
        self.track = []

    def movement(self, direction):
        '''
        Takes the direction that the snake is facing and moves the snake in that direction
        '''
        if direction == 'right':
            self.x_position += self.velocity

        elif direction == 'left':
            self.x_position -= self.velocity

        elif direction == 'up':
            self.y_position -= self.velocity

        elif direction == 'down':
            self.y_position += self.velocity

        return self.x_position, self.y_position

    def direction_check(self, direction, keys):
        '''
        Checks for changes in direction and adjusts accordingly
        '''
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

    def tracker(self, length):
        '''
        builds a list of positions for the snake pieces according to the length of the snake. This tracker will be
        used to draw the snake onto the screen
        '''
        self.track.insert(0, [self.x_position, self.y_position])
        self.track.pop() if len(self.track) > length else None
        return self.track

    def collision_check(self):
        '''
        Checks if the head of the snake hits a block of the tail, a banned block from editing, or the barrier
        '''
        return True if self.x_position < 0 or self.x_position > (self.width - self.edge) or self.y_position < 0 \
                       or self.y_position > (self.height - self.edge) or self.track[0] in self.track[1:] else False


class Food:
    '''
    The apple which will increase the score and the length of the snake
    '''
    def __init__(self, size):
        self.width, self.height = size
        self.edge = self.width // 50
        self.x_position, self.y_position = self.edge * 15, self.edge * 15

    def get_coordinates(self, track, occupied=True):
        '''
        finds coordinates for the apple which are not already occupied by the snake after being eaten
        '''
        while occupied:
            food_x = self.edge * random.randint(0, (self.width // self.edge) - 1)
            food_y = self.edge * random.randint(0, (self.height // self.edge) - 1)
            occupied = False if [food_x, food_y] not in track else True
        return food_x, food_y


def mainframe():
    '''
    The main game-screen which displays the snake game.
    '''
    pygame.init()
    size = (901, 613) #A bit obscure of a size to be able to show the full grid and an even number of blocks for the height
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Hamiltonian Snake")
    clock = pygame.time.Clock()
    length = 1
    player = Snake(size)
    apple = Food(size)
    direction = None
    track = []
    run = True
    while run:
        pygame.time.delay(75)
        clock.tick(15)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        keys = pygame.key.get_pressed()
        direction = player.direction_check(direction, keys)
        player.movement(direction)
        track = player.tracker(length)
        screen.fill((0, 0, 0))
        if player.x_position == apple.x_position and player.y_position == apple.y_position:
            length += 2
            apple.x_position, apple.y_position = apple.get_coordinates(player.track)
        pygame.draw.rect(screen, (255, 0, 0), (apple.x_position, apple.y_position, apple.edge, apple.edge))
        for cube in track:
            pygame.draw.rect(screen, (0, 255, 0), (cube[0], cube[1], player.edge, player.edge))
        run = False if player.collision_check() else True
        make_grid(size, player.edge, screen)

        pygame.display.update()

    return length


def make_grid(size, edge, screen):
    '''
    draws the grid of the board onto the screen
    '''
    width, height = size
    for i in range(0, (width // edge) + 1):
        pygame.draw.line(screen, (255, 255, 255), (i * edge, 0), (i * edge, height))
    for i in range(0, (height // edge) + 1):
        pygame.draw.line(screen, (255, 255, 255), (0, i * edge), (width, i * edge))


print(mainframe())
