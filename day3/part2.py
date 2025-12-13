"""
Treating the batteries as strings, using python's built-in max() and index() functions
"""
def read_file_lines(file_name):
    with open(f"day3/input_data/{file_name}") as f:
        lines = f.readlines()
    return [line.strip() for line in lines]

banks = read_file_lines("input-data.txt")

total_batteries = 12
total_joltage = 0

for bank in banks:
    print(f"Processing bank: {bank}")

    bank_joltage = []
    remaining_bank = bank

    for remaining_batteries in range(11, -1, -1):
        print(remaining_batteries)

        # ignore remaining number of batteries
        if remaining_batteries > 0:
            valid_bank = remaining_bank[:-remaining_batteries]
        else:
            valid_bank = remaining_bank
        print(f"valid bank {valid_bank}")

        # find the position of the highest digit in the valid bank
        highest_digit = max(valid_bank)
        highest_pos = valid_bank.index(highest_digit)
        print(f"Highest digit: {highest_digit} at position {highest_pos}")

        remaining_bank = remaining_bank[highest_pos+1:]
        print(f"Remaining bank: {remaining_bank}")

        bank_joltage.append(int(highest_digit))
        print(f"Joltage: {bank_joltage}")

    # convert list to int
    bank_joltage = int(''.join(map(str, bank_joltage)))

    total_joltage += bank_joltage

print(f"Total joltage: {total_joltage}")
