from colors import colors
from items import pygame


def make_outline(size, screen):
    '''
    draws an outline of the board onto the screen for playing
    '''
    width, height = size
    pygame.draw.line(screen, colors.get('white'), (50, 50), (50, height - 50))
    pygame.draw.line(screen, colors.get('white'), (width - 50, 50), (width - 50, height - 50))
    pygame.draw.line(screen, colors.get('white'), (50, 50), (width - 50, 50))
    pygame.draw.line(screen, colors.get('white'), (50, height - 50), (width - 50, height - 50))


def make_grid(size, edge, screen, banned_blocks):
    '''
    draws the grid of the board onto the screen for precision in editing
    '''
    width, height = size
    draw_banned_blocks(banned_blocks, screen, edge)
    for i in range(0, ((width - 100) // edge) + 1):
        pygame.draw.line(screen, colors.get('white'), ((i * edge) + 50, 50), ((i * edge) + 50, height - 50))
    for i in range(0, ((height - 100) // edge) + 1):
        pygame.draw.line(screen, colors.get('white'), (50, (i * edge) + 50), (width - 50, i * edge + 50))


def draw_banned_blocks(banned_blocks, screen, edge):
    '''
    draws lines onto the grid through the banned blocks to mark them
    '''
    for blocks in banned_blocks:
        pygame.draw.rect(screen, colors.get('dark_purple'), (blocks[0], blocks[1], edge, edge))
        pygame.draw.rect(screen, colors.get('purple'), (blocks[0] + 1, blocks[1] + 1, edge - 2, edge - 2))


def draw_arrow(screen):
    '''
    draws back arrow
    '''
    pygame.draw.line(screen, colors.get('white'), (10, 25), (45, 25))
    pygame.draw.line(screen, colors.get('white'), (10, 25), (10 + 20 * (3 ** (1 / 2) / 2), (25 - 20 / 2)))
    pygame.draw.line(screen, colors.get('white'), (10, 25), (10 + 20 * (3 ** (1 / 2) / 2), (25 + 20 / 2)))
