from game import maingame, pygame
from hamiltonian_curcuit import hamiltonian_circuit
from screens import settings, loss_screen
from items import Snake


def mainframe(banned_blocks=[], gamemode=[0, 0, 0], settings_skip=False):
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
        if not settings_skip:
            banned_blocks, gamemode, gameplay = settings(size, screen, base_font, player, gamemode, banned_blocks)
        if gameplay:
            length = maingame(size, screen, base_font, player, banned_blocks, gamemode)
            settings_skip = loss_screen(length, screen, size, base_font, player, banned_blocks)
        else:
            hamiltonian_circuit(size, screen, player)



mainframe()
