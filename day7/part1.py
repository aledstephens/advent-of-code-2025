import numpy as np

def load_map(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    grid = []
    for line in lines:
        row = [1 if char == '^' else 2 if char == 'S' else 0 for char in line.strip()]
        grid.append(row)
    return np.array(grid)

def cycle_grid_and_replace(grid):
    result = 0
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            print(f"({i},{j}): {val}")

            # Fill zeros with above twos
            if val == 0 and grid[i-1, j] == 2:
                grid[i, j] = 2

            # Fill left/right zeros with above twos if current is one
            if val == 1 and grid[i-1, j] == 2:
                result += 1
                # Fill left
                grid[i, j-1] = 2
                # Fill right
                grid[i, j+1] = 2
    return grid, result

data = load_map('day7/input_data/input-data.txt')
new_grid, result = cycle_grid_and_replace(data)
print(f"total number of splits: {result}")
