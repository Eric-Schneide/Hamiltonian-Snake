from game import maingame, pygame
from screens import start_menu, settings, loss_screen
from items import Snake


def mainframe(banned_blocks=[],gamemode=[0,0,0], menu_skip=False, settings_skip=False):
    '''
    The main game-screen which displays the snake game.
    '''
    while True:
        pygame.init()
        pygame.font.init()
        size = (900, 612)
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Hamiltonian Snake")
        base_font = pygame.font.SysFont('', 48)
        player = Snake(size)
        start_menu() if not menu_skip else None
        if not settings_skip:
            menu_skip, banned_blocks, gamemode = settings(size, screen, base_font, player,gamemode, banned_blocks)
        length = maingame(size, screen, base_font, player, banned_blocks, gamemode)
        settings_skip = loss_screen(length, screen, size, base_font, player, banned_blocks)


mainframe()
