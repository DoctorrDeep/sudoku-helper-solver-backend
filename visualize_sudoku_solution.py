import pygame
import no_backtracking_solution
import backtracking_solution
import starter_sudoku_sets

sudoku = starter_sudoku_sets.medium_sudoku

# get the solution of the sudoku
last_solution, sudoku_dict = no_backtracking_solution.try_fill_in(sudoku)

pygame.init()

dimension = 720
step = 80
margin = 2
bgcolor = 255, 255, 255
linecolor = 0, 0, 0

screen = pygame.display.set_mode((dimension, dimension))
pygame.display.set_caption("Sudoku Squares")


def game_loop():
    """Pygame: draw the numbers and grids"""

    gameExit = False
    while not gameExit:
        # pygame draws constantly
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(bgcolor)

        # Draw text of numbers and options in grid formation
        for x_ind, x in enumerate(range(0, dimension, step)):
            for y_ind, y in enumerate(range(0, dimension, step)):

                # Convert data into formatted string objects for drawing
                value_for_cell = last_solution[y_ind][x_ind] or sudoku_dict.get(
                    (y_ind, x_ind)
                )
                if isinstance(value_for_cell, list):
                    font_size = 12
                    value_for_cell = " ".join([str(i) for i in value_for_cell])
                else:
                    font_size = 32
                    value_for_cell = str(value_for_cell)

                font = pygame.font.Font("freesansbold.ttf", font_size)
                text = font.render(value_for_cell, True, linecolor, bgcolor)
                textRect = text.get_rect()
                textRect.center = (x + step // 2, y + step // 2)
                screen.blit(text, textRect)

        # Draw the grid lines
        for val_index, val in enumerate(range(0, dimension, step)):
            pygame.draw.line(screen, linecolor, (0, val), (dimension, val))
            pygame.draw.line(screen, linecolor, (val, 0), (val, dimension))
            if val_index in [3, 6]:
                new_val = val + margin
                pygame.draw.line(screen, linecolor, (0, new_val), (dimension, new_val))
                pygame.draw.line(screen, linecolor, (new_val, 0), (new_val, dimension))

        pygame.display.update()


game_loop()
pygame.quit()
quit()
