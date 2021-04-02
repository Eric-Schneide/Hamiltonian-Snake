from items import pygame
from colors import colors
from game import make_outline,draw_banned_blocks, draw_arrow, edit, sys


def start_menu():
    '''
    The main menu which is used as an opening page for the game.
    '''
    pass


def settings(size, screen, base_font):
    '''
    The page where the player will be able to customize their game with certain game modes which can be turned or off
    at will in between rounds of play.
    '''
    while True:
        x, y = pygame.mouse.get_pos()
        title = base_font.render("Configure Your Game Mode", True, colors.get('white'))
        list = base_font.render("Settings:", True, colors.get('white'))
        start = pygame.font.SysFont('arial', 30, False, True if 580 <= x <= 835 and 470 <= y <= 500 else False) \
            .render("Play Normal Game", True, colors.get('white'))
        hamilton = pygame.font.SysFont('arial', 30, False, True if 475 <= x <= 835 and 520 <= y <= 550 else False) \
            .render("Play Hamiltonian Pathway", True, colors.get('white'))
        edit = pygame.font.SysFont('arial', 30, False, True if 65 <= x <= 135 and 200 <= y <= 230 else False) \
            .render("Edit", True, colors.get('white'))
        poison = pygame.font.SysFont('arial', 30, False, True if 65 <= x <= 255 and 250 <= y <= 280 else False) \
            .render("Poison Apple", True, colors.get('white'))
        multi = pygame.font.SysFont('arial', 30, False, True if 65 <= x <= 210 and 300 <= y <= 330 else False) \
            .render("Multi Ball", True, colors.get('white'))
        dualist = pygame.font.SysFont('arial', 30, False, True if 65 <= x <= 175 and 350 <= y <= 380 else False) \
            .render("Dualist", True, colors.get('white'))

        screen.fill(colors.get('black'))
        draw_arrow(screen)
        make_outline(size, screen)
        screen.blit(title, (250, 70))
        screen.blit(list, (75, 150))
        screen.blit(edit, (75, 200))
        screen.blit(poison, (75, 250))
        screen.blit(multi, (75, 300))
        screen.blit(dualist, (75, 350))
        screen.blit(hamilton, (480, 520))
        screen.blit(start, (580, 470))

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed(num_buttons=3)[0] and 580 <= x <= 835 and 470 <= y <= 500:
                    return


def loss_screen(length, screen, size, base_font, player, banned_blocks):
    '''
    The display which is shown when a loss occurs. Displays the length of the snake and gives the player the
    option to either play again or edit the board.
    '''
    while True:
        x, y = pygame.mouse.get_pos()
        loss = base_font.render('Game Over', True, colors.get('white'))
        score = base_font.render(f'Final Score: {length + len(banned_blocks)} ', True, colors.get('white'))
        replay = pygame.font.SysFont('arial', 32, False, True if 240 <= x <= 390 and 320 <= y <= 350 else False) \
            .render('Play Again', True, colors.get('white'))
        editor = pygame.font.SysFont('arial', 32, False, True if 490 <= x <= 640 and 320 <= y <= 350 else False) \
            .render('Settings', True, colors.get('white'))
        make_outline(size, screen)
        draw_banned_blocks(banned_blocks, screen, player.edge)
        pygame.draw.rect(screen, colors.get('white'),
                         [player.track[0][0], player.track[0][1], player.edge, player.edge])
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
