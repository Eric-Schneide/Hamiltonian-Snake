from items import Food, Dualist, P_Food, pygame
from colors import colors
from drawn_assets import make_grid, make_outline, draw_banned_blocks, draw_arrow
import sys


def maingame(size, screen, base_font, player, banned_blocks, gamemode, length=1, direction=None, track=[]):
    '''
    The main snake game
    '''
    clock = pygame.time.Clock()
    apple = Food(size, (2 * gamemode[1]) + 1)
    dualist = Dualist(size, 1 if gamemode[2] else 0)
    poison_apple = P_Food(size, gamemode[0])
    for apples in range(0, apple.apples):
        apple.apple_pos.append(apple.get_coordinates(player.track, banned_blocks))
    for poison_apples in range(0, poison_apple.apples):
        poison_apple.apple_pos.append(poison_apple.get_coordinates(player.track, banned_blocks, apple.apple_pos))

    while True:
        pygame.time.delay(75)
        clock.tick(15)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        keys = pygame.key.get_pressed()
        direction = player.direction_check(direction, keys)
        player.movement(direction)
        player.tracker(length)
        screen.fill(colors.get('black'))

        if [player.x_position, player.y_position] in apple.apple_pos:
            length += 2
            dualist.length += 2
            if length + dualist.length + len(banned_blocks) >= 1600:
                return length
            apple.apple_pos.pop(apple.apple_pos.index([player.x_position, player.y_position]))
            apple.apple_pos.append(apple.get_coordinates(player.track, banned_blocks))
            if poison_apple.change_check(gamemode[0]):
                poison_apple.apple_pos.pop(0)
                poison_apple.apple_pos.append(
                    poison_apple.get_coordinates(player.track, banned_blocks, apple.apple_pos))

        draw_banned_blocks(banned_blocks, screen, player.edge)

        for cubes in player.track:
            pygame.draw.rect(screen, colors.get('dark_green'), [cubes[0], cubes[1], player.edge, player.edge])
            pygame.draw.rect(screen, colors.get('green'),
                             [cubes[0] + 1, cubes[1] + 1, player.edge - 2, player.edge - 2])
        if gamemode[2]:
            dualist.movement(direction)
            dualist.tracker(dualist.length)
            for cubes in dualist.track:
                pygame.draw.rect(screen, colors.get('dark_orange'), [cubes[0], cubes[1], player.edge, player.edge])
                pygame.draw.rect(screen, colors.get('orange'),
                                 [cubes[0] + 1, cubes[1] + 1, player.edge - 2, player.edge - 2])
        for apples in apple.apple_pos:
            pygame.draw.rect(screen, colors.get('dark_red'), [apples[0], apples[1], apple.edge, apple.edge])
            pygame.draw.rect(screen, colors.get('red'), [apples[0] + 1, apples[1] + 1, apple.edge - 2, apple.edge - 2])

        for poison_apples in poison_apple.apple_pos:
            pygame.draw.rect(screen, colors.get('dark_blue'),
                             [poison_apples[0], poison_apples[1], poison_apple.edge, poison_apple.edge])
            pygame.draw.rect(screen, colors.get('blue'),
                             [poison_apples[0] + 1, poison_apples[1] + 1, poison_apple.edge - 2, poison_apple.edge - 2])
        make_outline(size, screen)

        if player.collision_check(banned_blocks, dualist.track, poison_apple.apple_pos):
            return length

        score = base_font.render(f'Length: {length}', True, colors.get('white'))
        screen.blit(score, (50, 10))

        pygame.display.update()


def edit(size, edge, screen, banned_blocks):
    '''
    Allows the player to edit the boards, marking spaces which can be banned and result in a loss
    if touched by the snake
    '''

    while True:
        screen.fill(colors.get('black'))
        draw_arrow(screen)
        make_grid(size, edge, screen, banned_blocks)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed(num_buttons=3)[0]:
                x, y = pygame.mouse.get_pos()
                if x <= 50 and y <= 50:
                    return banned_blocks
                elif 50 <= x <= size[0] - 50 and 50 <= y <= size[1] - 50:
                    cell_x, cell_y = edge * ((x - 50) // edge) + 50, edge * ((y - 50) // edge) + 50
                    if [cell_x, cell_y] == [50, 50]:
                        pass
                    elif [cell_x, cell_y] not in banned_blocks:
                        pygame.draw.line(screen, colors.get('white'), (cell_x, cell_y), (cell_x + edge, cell_y + edge))
                        banned_blocks.append([cell_x, cell_y])
                    else:
                        pygame.draw.line(screen, colors.get('black'), (cell_x, cell_y), (cell_x + edge, cell_y + edge))
                        banned_blocks.remove([cell_x, cell_y])
        pygame.display.update()




