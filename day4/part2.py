import numpy as np

# load array which is individual strings and separated by new lines
def load_data(file_path: str) -> np.array:
    input = np.loadtxt(file_path, dtype=str)
    char_list = [list(line) for line in input] # split the lists into individual characters
    array = np.array(char_list)
    return array

def search_for_target(input: np.array, target: str) -> list[tuple[int,int]]:
    result = []
    for i in range(input.shape[0]):
        for j in range(input.shape[1]):
            if input[i,j] == target:
                result.append((i,j))
    return result

def check_bounds(coord: tuple[int, int], array_limit: tuple[int, int]) -> bool:
    return coord[0] < 0 or coord[0] > array_limit[0] or coord[1] < 0 or coord[1] > array_limit[1]

def find_all_neighbours(coord: tuple[int, int], array_limit: tuple[int, int]) -> list[tuple[int, int]]:
    nbr_all = [
        (coord[0] - 1, coord[1] -1),
        (coord[0] - 1, coord[1]    ),
        (coord[0] - 1, coord[1] + 1),
        (coord[0],     coord[1] - 1),
        (coord[0],     coord[1] + 1),
        (coord[0] + 1, coord[1] - 1),
        (coord[0] + 1, coord[1]    ),
        (coord[0] + 1, coord[1] + 1),
    ] # returns coord neighbours

    limit = (array_limit[0], array_limit[1])

    nbr_valid = []

    for coord in nbr_all:
        if check_bounds(coord, limit) == False:
            nbr_valid.append(coord)

    return nbr_valid

def remove_valid_locations(input: np.array, locations, target: str) -> int:
    valid_count = 0

    array_limit = input.shape
    array_limit = (array_limit[0] - 1, array_limit[1] - 1)

    for location in locations:
        # print(f'Checking location {location}')
        nbr_coords = find_all_neighbours(location, array_limit)

        for coord in nbr_coords:

            if coord in locations:
                # print(f'Found valid neighbour at {coord}')
                valid_count += 1

            if valid_count >= 4:
                # print(f"Target has 4 or more neighbours, skipping")
                break

        if valid_count < 4:
            locations.pop(locations.index(location)) # remove location from list

        valid_count = 0 # reset for next location

    return locations

data = load_data('day4/input_data/input-data.txt')

init_locations = search_for_target(data, '@') # the initial number of target locations
num_init_locations = len(init_locations)

# loop until the number of locations stops changing
prev_count = -1 # initialize to a different value than current count
current_locations = init_locations

while prev_count != len(current_locations):
    prev_count = len(current_locations)
    current_locations = remove_valid_locations(data, current_locations, '@')
    print(f'Number of valid locations: {len(current_locations)}')
num_final_locations = len(current_locations)
result = num_init_locations - num_final_locations
print(f'Result: {result} removed locations')

