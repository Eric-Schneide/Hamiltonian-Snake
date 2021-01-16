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

def mainframe():
    '''
    The main game-screen which displays the snake game.
    '''
    pygame.init()
    size = (900, 612)
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

print(mainframe())
