import numpy as np

def read_file(file_name):
    with open(f"day2/input_data/{file_name}") as f:
        line = f.readline().strip()
        items = line.split(",")
    return items

def check_leading_zero(half):
    # check if either has a leading zero
    if half[0] == "0":
        return True
    else:
        return False

def create_id_range(id_range):
    # split item on - and make integer range
    range_start = int(id_range.split("-")[0])
    range_end = int(id_range.split("-")[1])
    id_range = np.linspace(range_start, range_end, int(range_end) - int(range_start) + 1, dtype=int)
    return id_range

def is_single_digit(id):
    if id < 10:
        return True
    else:
        return False

def does_pattern_length_divide(pat_length, id_length):
    if id_length % pat_length != 0:
        print(f"ID length {id_length} not multiple of pattern length {pat_length}")
        return False
    else:
        return True

def does_pattern_match(pat_length, id):
    # split id into pat_length parts
    id_str = str(id)
    parts = [id_str[i:i+pat_length] for i in range(0, len(id_str), pat_length)]
    print(parts)
    # compare all parts
    first_part = parts[0]
    all_match = all(part == first_part for part in parts)
    if all_match:
        print(f"ID {id} matches pattern length {pat_length}")
        return True
    else:
        print(f"ID {id} does not match pattern length {pat_length}")
        return False

result = 0 # store result

id_ranges = read_file("input-data.txt")

# loop through ranges
for id_range in id_ranges:
    print(f"Range: {id_range}")

    id_range = create_id_range(id_range)

    for id in id_range:
        print(f"Checking ID: {id}")

        if is_single_digit(id):
            print(f"ID {id} is single digit, skipping to next ID")
            continue

        id_length = len(str(id))

        for pat_length in range(1, len(str(id))):
            print(f"Trying pattern length: {pat_length} for ID {id}")

            if not does_pattern_length_divide(pat_length, id_length):
                print(f"Pattern length {pat_length} does not divide ID length {id_length}, skipping to next pattern length")
                continue

            if does_pattern_match(pat_length, id):
                result += id
                print(f"Found a match. ID {id} added to result, current result: {result}")
                print(f"Moving to next ID")
                break
print("result:", result)