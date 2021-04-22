import pygame, sys
from items import Food
from colors import colors
from drawn_assets import make_outline, draw_arrow


def hamiltonian_circuit(size, screen, apples, player):
    '''
    A basic AI which creates a path which hits all places on the board and runs the snake game
    until the snake reaches the maximum length.
    '''
    width, height = size
    length = 1
    path = [[50, 50]]
    track = []
    for rows in range(0, ((height - 50) // (2 * player.edge)) - 1):
        path += (build_path(width - 50, height - 50, rows, player))
    final_y = height - 50 - player.edge
    while final_y > 50:
        path.append([50, final_y])
        final_y -= player.edge
    index = 0
    clock = pygame.time.Clock()
    apple = Food(size, apples)
    for apples in range(0, apple.apples):
        apple.apple_pos.append(apple.get_coordinates(player.track, []))
    while True:
        x, y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed(num_buttons=3)[0] and 0 <= x <= 50 and 0 <= y <= 50:
                    return
        pygame.time.delay(25)
        clock.tick(50)
        screen.fill(colors.get('black'))
        track.insert(0, [path[index % len(path)][0], path[index % len(path)][1]])
        if len(track) > length:
            track.pop()
        index += 1
        if [path[index % len(path)][0], path[index % len(path)][1]] in apple.apple_pos:
            if length+4>=1600:
                length=1
                track=[]
            else:
                length+=4
            apple.apple_pos.pop(apple.apple_pos.index([path[index % len(path)][0], path[index % len(path)][1]]))
            apple.apple_pos.append(apple.get_coordinates(track, []))

        for apples in apple.apple_pos:
            pygame.draw.rect(screen, colors.get('dark_red'), [apples[0], apples[1], apple.edge, apple.edge])
            pygame.draw.rect(screen, colors.get('red'), [apples[0] + 1, apples[1] + 1, apple.edge - 2, apple.edge - 2])

        for cubes in track:
            pygame.draw.rect(screen, colors.get('dark_green'), [cubes[0], cubes[1], player.edge, player.edge])
            pygame.draw.rect(screen, colors.get('green'),
                             [cubes[0] + 1, cubes[1] + 1, player.edge - 2, player.edge - 2])
        make_outline(size, screen)
        draw_arrow(screen)

        pygame.display.update()


def build_path(width, height, rows, player):
    start_x = 66
    start_y = 50 + 2 * rows * player.edge
    row = []
    while start_x + player.edge < width - 2 * rows * player.edge:
        row.append([start_x, start_y])
        start_x += player.edge

    while start_y + player.edge < height:
        row.append([start_x, start_y])
        start_y += player.edge
    row.append([start_x, start_y])
    start_x -= player.edge

    while start_y - player.edge > 50 + 2 * rows * player.edge:
        row.append([start_x, start_y])
        start_y -= player.edge

    while start_x > 50:
        row.append([start_x, start_y])
        start_x -= player.edge
    return row
