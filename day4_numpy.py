import io
import os
import numpy as np
from scipy.ndimage import convolve
import time

if __name__ == "__main__":
    grid = []
    start_time = time.perf_counter()
    with open("day4.txt", 'r') as fh:
        size = os.fstat(fh.fileno()).st_size
        while fh.tell() < size:
            for line in fh:
                grid.append(list(line.strip()))
        

    grid_array = np.array([[1 if cell in ['@'] else 0 for cell in row] for row in grid])
    vector_neighbors = np.array([[1, 1, 1],
                                [1, 0, 1],
                                [1, 1, 1]])
    can_remove = True
    total_removed = 0
    while can_remove:
        neighbor_counts = convolve(grid_array, vector_neighbors, mode='constant', cval=0)
        cells_to_remove = 0

        for indy, row in enumerate(grid_array):
            for indx, cell in enumerate(row):
                if(neighbor_counts[indy, indx] < 4 and grid_array[indy, indx] == 1):
                    grid_array[indy, indx] = 0
                    total_removed += 1
                    cells_to_remove += 1

        if(cells_to_remove == 0):
            can_remove = False

        print(cells_to_remove)

    print(total_removed)

    end_time = time.perf_counter()
    print(f"Execution time: {end_time - start_time:.4f} seconds")