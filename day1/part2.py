import numpy as np

# load data as numpy array
input = np.loadtxt("day1/input_data/input-test.txt", dtype=str)

# Prepare dataset

def convert_input_to_numeric(input):
    '''
    Converts input from L/R to signed integers
    '''

    input_signed = []

    for rot in input:
        if rot[0] == "R":
            input_signed.append(int(rot[1:]))
        elif rot[0] == "L":
            input_signed.append(-int(rot[1:]))
        else:
            raise ValueError("Unexpected rotation direction")
    return input_signed

def drop_hundreds(input_signed):
    '''
    Drops hundreds place from signed integers
    '''
    input_dropped_hundreds = []

    for rot in input_signed:
        if rot < 0:
            rot = abs(rot)
            input_dropped_hundreds.append(- (rot % 100) )
        else:
            input_dropped_hundreds.append(rot % 100)
    return input_dropped_hundreds

input_signed = convert_input_to_numeric(input)
input_dropped_hundreds = drop_hundreds(input_signed)

position = 50
password = 0

for rot in input_dropped_hundreds:

    # start state
    if position < 0:
        start_state = "NEG"
    else:
        start_state = "POS"
    print(f"start state = {start_state}")

    # print(f"starting position = {position}")
    print(f"rotation = {rot}")
    position = position + rot
    # print(f"position after rotation {position}")

    # end state
    if position < 0:
        end_state = "NEG"
    else:
        end_state = "POS"
    print(f"end state = {end_state}")

    if position < 0:
        position = 100 + position
        # print(f"position after accounting for negative {position}")
    position = int(str(position)[-2:])
    print(f"FINAL POSITION {position}")

    if position == 0:
        password += 1
        # print("Password updated")

    # compare states
    if start_state != end_state:
        password += 1
        print("Password updated because state changed")


print(f"PASSWORD: {password}")
