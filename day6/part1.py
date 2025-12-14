# load text file, split on new line
def load_data(file_path: str) -> list[str]:
    with open(file_path, 'r') as f:
        input = f.read()
    return input

data = load_data('day6/input_data/input-data.txt')

# split data on new line
lines = data.split('\n')
# split lines on spaces
numbers = [line.split(' ') for line in lines]
# remove empty strings from words
numbers = [[numbers for numbers in line if numbers] for line in numbers]

# numbers is lists of lines. Each element in the lines should be looped through. Element 1, line 1. Element 1 line 2, etc.
result = 0
for i in range(len(numbers[0])):
    p1 = numbers[0][i]
    p2 = numbers[1][i]
    p3 = numbers[2][i]
    p4 = numbers[3][i]
    symbol = numbers[4][i]
    if symbol == "+":
        result += (int(p1) + int(p2) + int(p3) + int(p4))
    elif symbol == "*":
        result += (int(p1) * int(p2) * int(p3) * int(p4))
print(f'Result: {result}')
