import io
import os

def is_grid_empty(grid, x, y):
    grid_max_y = len(grid)-1
    grid_max_x = len(grid[0])-1

    if(x < 0 or x >= grid_max_x):
        return True
    if(y < 0 or y >= grid_max_y):
        return True
    # print(f"mx{grid_max_x}, my{grid_max_y}")
    # print(f"x{x} y{y}")
    return grid[y][x] == '.'

def is_grid_roll(grid, x, y):
    grid_max_y = len(grid)
    grid_max_x = len(grid[0])-1

    if(x < 0 or x >= grid_max_x):
        return False
    if(y < 0 or y >= grid_max_y):
        return False

    # if(y == 8):
    #     print(f"mx{grid_max_x}, my{grid_max_y}")
    #     print(f"x{x} y{y}")
    return grid[y][x] == '@' or grid[y][x] == 'x'

def is_accessable(grid, x, y):
    roll_cell = 0
    
    if(is_grid_roll(grid, x-1, y-1)):
        roll_cell += 1

    if(is_grid_roll(grid, x, y-1)):
        roll_cell += 1
        
    if(is_grid_roll(grid, x+1, y-1)):
        roll_cell += 1

    if(is_grid_roll(grid, x-1, y)):
        roll_cell += 1
        
    if(is_grid_roll(grid, x+1, y)):
        roll_cell += 1

    if(is_grid_roll(grid, x-1, y+1)):
        roll_cell += 1

    if(is_grid_roll(grid, x, y+1)):
        roll_cell += 1
        
    if(is_grid_roll(grid, x+1, y+1)):
        roll_cell += 1

    return roll_cell < 4


if __name__ == "__main__":
    grid = []
    with open("day4.txt", 'r') as fh:
        size = os.fstat(fh.fileno()).st_size
        while fh.tell() < size:
            for line in fh:
                grid.append(list(line))
        
        print('\n'.join([''.join([str(cell) for cell in row]) for row in grid]))
    
        can_remove = True
        total_removed = 0
        while can_remove:
            accessable = 0
            for indy, row in enumerate(grid):
                for indx, cell in enumerate(row):
                    if(is_accessable(grid, indx, indy)):
                        if(cell == '@'):
                            grid[indy][indx] = 'x'
                            accessable += 1
                            total_removed += 1

            print('\n\n')
            print('\n'.join([''.join([str(cell) for cell in row]) for row in grid]))
            print(accessable)
            if(accessable > 0):
                for indy, row in enumerate(grid):
                    for indx, cell in enumerate(row):
                        if(cell == 'x'):
                            grid[indy][indx] = '.'
            if(accessable == 0):
                can_remove = False

            print('\n'.join([''.join([str(cell) for cell in row]) for row in grid]))
        print(total_removed)