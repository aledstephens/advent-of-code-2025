import numpy as np

# load data as numpy array
input = np.loadtxt("day1/input_data/input-test.txt", dtype=str)

# Prepare dataset
input_signed = []

# convert to integers
for rot in input:
    if rot[0] == "R":
        input_signed.append(int(rot[1:]))
    elif rot[0] == "L":
        input_signed.append(-int(rot[1:]))
    else:
        raise ValueError("Unexpected rotation direction")

input_drop_hundreds = []

for rot in input_signed:
    if rot < 0:
        rot = abs(rot)
        input_drop_hundreds.append(- (rot % 100) )
    else:
        input_drop_hundreds.append(rot % 100)

position = 50
password = 0

for rot in input_drop_hundreds:
    # print(f"starting position = {position}")
    print(f"rotation = {rot}")
    position = position + rot
    # print(f"position after rotation {position}")
    if position < 0:
        position = 100 + position
        # print(f"position after accounting for negative {position}")
    position = int(str(position)[-2:])
    print(f"FINAL POSITION {position}")
    if position == 0:
        password += 1
        # print("Password updated")

print(f"PASSWORD: {password}")
