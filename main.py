from game import maingame,pygame
from screens import start_menu,loss_screen





def mainframe(banned_blocks=[]):
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
        start_menu()
        length, player = maingame(size, screen, base_font, banned_blocks)
        banned_blocks = loss_screen(length, screen, size, base_font, player, banned_blocks)


print(mainframe())
