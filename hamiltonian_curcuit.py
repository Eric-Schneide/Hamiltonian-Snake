def hamiltonian_circuit(size, screen, player):
    '''
    A basic AI which creates a path which hits all places on the board and runs the snake game
    until the snake reaches the maximum length.
    '''
    width, height = size - (50, 50)
    length = 1
    path = [50, 50]
    for rows in range(0, (height - 50) // (2 * player.edge)):
        path += build_path(width, height, rows, screen, player)


def build_path(width, height, rows, screen, player):
    start_x = 66
    stary_y = 50 + 2 * rows
    row = []
