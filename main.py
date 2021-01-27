from items import Snake, Food, pygame
import sys

def make_grid(size, edge, screen,banned_blocks):
    '''
    draws the grid of the board onto the screen
    '''
    width, height = size
    for i in range(0, ((width-100) // edge) + 1):
        pygame.draw.line(screen, (255, 255, 255), ((i * edge)+50, 50), ((i * edge)+50, height-50))
    for i in range(0, ((height-100) // edge) + 1):
        pygame.draw.line(screen, (255, 255, 255), (50, (i * edge)+50), (width-50, i * edge+50))
    draw_banned_blocks(size,banned_blocks,screen,edge)

def draw_banned_blocks(size,banned_blocks,screen,edge):
    for blocks in banned_blocks:
        pygame.draw.line(screen, (255, 255, 255), (blocks[0], blocks[1]), (blocks[0] + edge, blocks[1] + edge))

def start_menu():
    pass

def maingame(size, screen,banned_blocks):
    clock = pygame.time.Clock()
    length = 1
    max_length = 1600
    track = []
    player = Snake(size)
    apple = Food(size,track,banned_blocks)
    direction = None

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
            apple.x_position, apple.y_position = apple.get_coordinates(player.track,banned_blocks)
        pygame.draw.rect(screen, (255, 0, 0), (apple.x_position, apple.y_position, apple.edge, apple.edge))
        for cube in track:
            pygame.draw.rect(screen, (0, 255, 0), (cube[0], cube[1], player.edge, player.edge))
        if player.collision_check(banned_blocks):
            return length,player
        make_grid(size, player.edge, screen,banned_blocks)


        pygame.display.update()

def loss_screen(length,screen,size,player):

    make_grid(size, player.edge, screen)
    screen.fill((0, 0, 0), (227, 211, 447, 191))
    pygame.display.update()

def edit(size, edge, screen, banned_blocks=[]):
    while True:
        #screen.fill((0,0,0))
        make_grid(size,edge,screen,banned_blocks)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed(num_buttons=3)[0]:
                    x,y=pygame.mouse.get_pos()
                    if x<=50 and y<=50:
                        return banned_blocks
                    elif x >= 50 and x <= size[0] - 50 and y>=50 and y<= size[1]-50:
                        cell_x,cell_y=edge*((x-50)//edge)+50,edge*((y-50)//edge)+50
                        if [cell_x,cell_y] not in banned_blocks:
                            pygame.draw.line(screen, (255,255,255), (cell_x,cell_y),(cell_x+edge,cell_y+edge))
                            banned_blocks.append([cell_x,cell_y])
                        else:
                            pygame.draw.line(screen, (0, 0, 0), (cell_x, cell_y), (cell_x + edge, cell_y + edge))
                            banned_blocks.remove([cell_x, cell_y])
        pygame.display.update()

def mainframe(banned_blocks=[]):
    '''
    The main game-screen which displays the snake game.
    '''
    while True:
        pygame.init()
        size = (900, 612)
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Hamiltonian Snake")
        start_menu()
        length,player=maingame(size,screen,banned_blocks)
        banned_blocks=edit(size,player.edge,screen)
print(mainframe())
