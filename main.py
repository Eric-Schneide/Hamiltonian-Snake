from items import Snake, Food, pygame
import sys

def make_grid(size, edge, screen):
    '''
    draws the grid of the board onto the screen
    '''
    width, height = size
    for i in range(0, ((width-100) // edge) + 1):
        pygame.draw.line(screen, (255, 255, 255), ((i * edge)+50, 50), ((i * edge)+50, height-50))
    for i in range(0, ((height-100) // edge) + 1):
        pygame.draw.line(screen, (255, 255, 255), (50, (i * edge)+50), (width-50, i * edge+50))

def start_menu():
    pass

def maingame(size, screen):
    clock = pygame.time.Clock()
    length = 1
    max_length = 1600
    player = Snake(size)
    apple = Food(size)
    direction = None
    track = []
    while True:
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
            sys.exit() if length > max_length else None
            apple.x_position, apple.y_position = apple.get_coordinates(player.track)
        pygame.draw.rect(screen, (255, 0, 0), (apple.x_position, apple.y_position, apple.edge, apple.edge))
        for cube in track:
            pygame.draw.rect(screen, (0, 255, 0), (cube[0], cube[1], player.edge, player.edge))
        if player.collision_check():
            return length,player
        make_grid(size, player.edge, screen)

        pygame.display.update()


def loss_screen(length,screen,size,player):

    make_grid(size, player.edge, screen)
    screen.fill((0, 0, 0), (227, 211, 447, 191))
    pygame.display.update()

def mainframe():
    '''
    The main game-screen which displays the snake game.
    '''
    while True:
        pygame.init()
        size = (900, 612)
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Hamiltonian Snake")
        start_menu()
        length,player=maingame(size,screen)
        loss_screen(length,screen,size,player)
print(mainframe())
