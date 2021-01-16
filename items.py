import random
import pygame

class Snake:
    '''
    The player class
    '''
    def __init__(self, size):
        self.width, self.height = size
        self.edge = (self.width-100) // 50
        self.x_position = 50
        self.y_position = 50
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
        return True if self.x_position < 50 or self.x_position > (self.width - 50 - self.edge) or \
                       self.y_position < 50 or self.y_position > (self.height - 50 - self.edge) or \
                       self.track[0] in self.track[1:] else False

class Food:
    '''
    The apple which will increase the score and the length of the snake
    '''
    def __init__(self, size):
        self.width, self.height = size
        self.edge = (self.width-100) // 50
        self.x_position, self.y_position = self.edge * random.randint(1, ((self.width-100) // self.edge) - 1)+50, \
                                           self.edge * random.randint(1, ((self.height-100) // self.edge) - 1)+50

    def get_coordinates(self, track, occupied=True):
        '''
        finds coordinates for the apple which are not already occupied by the snake after being eaten
        '''
        while occupied:
            food_x = self.edge * random.randint(0, ((self.width-100) // self.edge) - 1)+50
            food_y = self.edge * random.randint(0, ((self.height-100) // self.edge) - 1)+50
            occupied = False if [food_x, food_y] not in track else True
        return food_x, food_y