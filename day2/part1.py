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

def create_num_range(range):
    # split item on - and make integer range
    range_start = int(range.split("-")[0])
    range_end = int(range.split("-")[1])
    num_range = np.linspace(range_start, range_end, int(range_end) - int(range_start) + 1, dtype=int)
    return num_range

result = 0 # store result

ranges = read_file("input-data.txt")

# loop through ranges
for range in ranges:
    print(f"Range: {range}")

    num_range = create_num_range(range)

    for num in num_range:

        # skip numbers with less than 2 digits
        if len(str(num)) < 2:
            continue

        # split number in half, check if the halves sub to zero
        string_num = str(num)
        first_half = string_num[:len(string_num)//2]
        second_half = string_num[len(string_num) // 2:]

        # skip leading zeros
        first_half_leading_zero = check_leading_zero(first_half)
        second_half_leading_zero = check_leading_zero(second_half)
        if first_half_leading_zero or second_half_leading_zero:
            continue

        difference = int(first_half) - int(second_half)

        if difference == 0:
            print(f"Found valid number: {num}")
            result += num

print(f"\n Result: {result}")
