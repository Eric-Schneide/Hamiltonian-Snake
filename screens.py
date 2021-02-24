from items import pygame
from colors import colors
from game import make_outline, edit, sys


def start_menu():
    pass


def loss_screen(length, screen, size, base_font, player, banned_blocks):
    '''
    The display which is shown when a loss occurs. Displays the length of the snake and gives the player the
    option to either play again or edit the board.
    '''
    while True:
        x, y = pygame.mouse.get_pos()
        loss = base_font.render('Game Over', True, colors.get('white'))
        score = base_font.render(f'Final Length: {length} ', True, colors.get('white'))
        replay = pygame.font.SysFont('arial', 30, False,
                                     True if 240 <= x <= 390 and 320 <= y <= 350 else False) \
            .render('play again', True, colors.get('white'))
        editor = pygame.font.SysFont('arial', 30, False,
                                     True if 490 <= x <= 640 and 320 <= y <= 350 else False) \
            .render('edit board', True, colors.get('white'))
        make_outline(size, player.edge, screen, banned_blocks)
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
                    return banned_blocks
                elif pygame.mouse.get_pressed(num_buttons=3)[0] and 490 <= x <= 640 and 320 <= y <= 350:
                    return edit(size, player.edge, screen, banned_blocks)
