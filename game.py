from items import Food, pygame
from colors import colors
from drawn_assets import make_grid, make_outline,draw_banned_blocks,draw_arrow
import sys


def maingame(size, screen, base_font, player, banned_blocks, gamemode, length=1, direction=None, track=[]):
    '''
    The main snake game
    '''
    clock = pygame.time.Clock()
    max_length = 1600 - len(banned_blocks)
    apple = Food(size, track, banned_blocks)


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
        screen.fill(colors.get('black'))
        if player.x_position == apple.x_position and player.y_position == apple.y_position:
            length += 4
            apple.x_position, apple.y_position = apple.get_coordinates(player.track, banned_blocks)
        pygame.draw.rect(screen, colors.get('dark_red'), [apple.x_position, apple.y_position, apple.edge, apple.edge])
        pygame.draw.rect(screen, colors.get('red'),
                         [apple.x_position + 1, apple.y_position + 1, apple.edge - 2, apple.edge - 2])
        for cube in track:
            pygame.draw.rect(screen, colors.get('dark_green'), [cube[0], cube[1], player.edge, player.edge])
            pygame.draw.rect(screen, colors.get('green'), [cube[0] + 1, cube[1] + 1, player.edge - 2, player.edge - 2])
        if player.collision_check(banned_blocks):
            return length
        make_outline(size, screen)
        draw_banned_blocks(banned_blocks, screen, player.edge)
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
