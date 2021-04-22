from colors import colors
from game import edit, make_outline, draw_banned_blocks, sys
from items import pygame


def settings(size, screen, base_font, player, gamemode, banned_blocks):
    '''
    The page where the player will be able to customize their game with certain game modes which can be turned or off
    at will in between rounds of play.
    '''
    while True:
        x, y = pygame.mouse.get_pos()
        title = base_font.render("Configure Your Game ", True, colors.get('white'))
        game_mode_list = base_font.render("Settings:", True, colors.get('white'))
        start = pygame.font.SysFont('arial', 30, False, True if 580 <= x <= 835 and 470 <= y <= 500 else False) \
            .render("Play Normal Game", True, colors.get('white'))
        hamilton = pygame.font.SysFont('arial', 30, False, True if 475 <= x <= 835 and 520 <= y <= 550 else False) \
            .render("Play Hamiltonian Pathway", True, colors.get('white'))
        edit_marker = pygame.font.SysFont('arial', 30, False, True if 65 <= x <= 135 and 200 <= y <= 230 else False) \
            .render("Edit", True, colors.get('white'))
        poison = pygame.font.SysFont('arial', 30, False, True if 65 <= x <= 255 and 250 <= y <= 280 else False) \
            .render("Poison Apple", True, colors.get('white'))
        multi = pygame.font.SysFont('arial', 30, False, True if 65 <= x <= 210 and 300 <= y <= 330 else False) \
            .render("Multi Ball", True, colors.get('white'))
        dualist = pygame.font.SysFont('arial', 30, False, True if 65 <= x <= 175 and 350 <= y <= 380 else False) \
            .render("Dualist", True, colors.get('white'))

        screen.fill(colors.get('black'))
        make_outline(size, screen)
        screen.blit(title, (250, 70))
        screen.blit(game_mode_list, (75, 150))
        screen.blit(edit_marker, (75, 200))
        screen.blit(poison, (75, 250))
        screen.blit(multi, (75, 300))
        screen.blit(dualist, (75, 350))
        screen.blit(hamilton, (480, 520))
        screen.blit(start, (580, 470))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed(num_buttons=3)[0] and 65 <= x <= 135 and 200 <= y <= 230:
                    banned_blocks = edit(size, player.edge, screen, banned_blocks)
                elif pygame.mouse.get_pressed(num_buttons=3)[0] and 65 <= x <= 255 and 250 <= y <= 280:
                    gamemode[0] = (gamemode[0] + 1) % 6
                elif pygame.mouse.get_pressed(num_buttons=3)[0] and 65 <= x <= 210 and 300 <= y <= 330:
                    gamemode[1] = (gamemode[1] + 1) % 5
                elif pygame.mouse.get_pressed(num_buttons=3)[0] and 65 <= x <= 175 and 350 <= y <= 380:
                    gamemode[2] = 1 if gamemode[2] == 0 else 0
                elif pygame.mouse.get_pressed(num_buttons=3)[0] and 580 <= x <= 835 and 470 <= y <= 500:
                    return banned_blocks, gamemode, True
                elif pygame.mouse.get_pressed(num_buttons=3)[0] and 475 <= x <= 835 and 520 <= y <= 550:
                    return banned_blocks, gamemode, False

        x_poison = 265
        for poison_apples in range(0, gamemode[0]):
            pygame.draw.rect(screen, colors.get('dark_blue'), [x_poison, 260, 20, 20])
            pygame.draw.rect(screen, colors.get('blue'), [x_poison + 1, 261, 18, 18])
            x_poison += 25

        x_apple = 220
        for apples in range(0, (2 * gamemode[1]) + 1):
            pygame.draw.rect(screen, colors.get('dark_red'), [x_apple, 310, 20, 20])
            pygame.draw.rect(screen, colors.get('red'), [x_apple + 1, 311, 18, 18])
            x_apple += 25

        if gamemode[2]:
            x_cube = 185
            for cubes in range(0, 5):
                pygame.draw.rect(screen, colors.get('dark_orange'), [x_cube, 360, 20, 20])
                pygame.draw.rect(screen, colors.get('orange'), [x_cube + 1, 361, 18, 18])
                x_cube += 20

        pygame.display.update()


def loss_screen(length, screen, size, base_font, player, banned_blocks):
    '''
    The display which is shown when a loss occurs. Displays the length of the snake and gives the player the
    option to either play again or edit the board.
    '''
    while True:
        x, y = pygame.mouse.get_pos()
        loss = base_font.render('Game Over', True, colors.get('white'))
        score = base_font.render(f'Final Score: {length} ', True, colors.get('white'))
        replay = pygame.font.SysFont('arial', 32, False, True if 240 <= x <= 390 and 320 <= y <= 350 else False) \
            .render('Play Again', True, colors.get('white'))
        editor = pygame.font.SysFont('arial', 32, False, True if 490 <= x <= 640 and 320 <= y <= 350 else False) \
            .render('Settings', True, colors.get('white'))
        make_outline(size, screen)
        draw_banned_blocks(banned_blocks, screen, player.edge)
        pygame.draw.rect(screen, colors.get('white'),
                         [player.track[0][0] + 1, player.track[0][1] + 1, player.edge - 2, player.edge - 2])
        screen.fill(colors.get('white'), (226, 210, 449, 193))
        screen.fill(colors.get('black'), (227, 211, 447, 191))
        screen.blit(loss, (360, 225))
        screen.blit(score, (330, 265))
        screen.blit(replay, (250, 320))
        screen.blit(editor, (500, 320))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed(num_buttons=3)[0] and 240 <= x <= 390 and 320 <= y <= 350:
                    return True
                elif pygame.mouse.get_pressed(num_buttons=3)[0] and 490 <= x <= 640 and 320 <= y <= 350:
                    return False
