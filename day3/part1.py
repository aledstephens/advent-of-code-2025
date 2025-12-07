"""
Treating the batteries as strings, using python's built-in max() and index() functions
"""
def read_file_lines(file_name):
    with open(f"day3/input_data/{file_name}") as f:
        lines = f.readlines()
    return [line.strip() for line in lines]

banks = read_file_lines("input-data.txt")

total_joltage = 0

for bank in banks:
    print(f"Processing bank: {bank}")

    # ignore the final digit since it's not a 10s
    valid_bank = bank[:-1]

    # find the position of the highest digit in the valid bank
    highest_digit_10 = max(valid_bank)
    highest_pos_10 = valid_bank.index(highest_digit_10)
    print(f"Highest digit: {highest_digit_10} at position {highest_pos_10}")

    # slice the full bank from that position
    remaining_bank = bank[highest_pos_10+1:]
    print(f"Remaining bank: {remaining_bank}")

    # find highest digit in remaining bank
    highest_digit = max(remaining_bank)
    print(f"Highest digit in remaining bank: {highest_digit}")

    bank_joltage = (int(highest_digit_10) * 10) + int(highest_digit)
    print(f"Joltage: {bank_joltage}")

    total_joltage += bank_joltage

print(f"Total joltage: {total_joltage}")
