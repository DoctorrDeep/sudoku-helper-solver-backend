from itertools import product

# Define 3X3 squares in grid
cube_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

CUBE_XYS = []
for x_and_y in product(cube_list, cube_list):
    a_cube = []
    for row_col in product(x_and_y[0], x_and_y[1]):
        a_cube.append(row_col)
    CUBE_XYS.append(a_cube)

# Define 3X3 squares in grid: with list comprehension (less readable)
# cube_xys = [
#     [row_col for row_col in product(x_and_y[0], x_and_y[1])]
#     for x_and_y in product(cube_list, cube_list)
# ]

# Define array of ALL cell positions in sudoku grid
ALL_XYS = list(product(range(9), range(9)))
