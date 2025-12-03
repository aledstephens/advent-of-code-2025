import numpy as np

# load data as numpy array
input = np.loadtxt("day1/input_data/input1.txt", dtype=str)

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

def count_hundreds(rot):
    '''
    Drops hundreds place from signed integers
    '''
    hundreds = abs(rot) //100

    return hundreds

def drop_hundreds(rot):
    '''
    Drops hundreds place
    '''
    if rot < 0:
        rot = abs(rot)
        rot = -(rot % 100)
    else:
        rot = rot % 100
    return rot

# Convert data to signed numeric
input_signed = convert_input_to_numeric(input)

# initialise variables
position = 50
password = 0

# main loop
for rot in input_signed:

    # to record whether starting position was 0
    starting_position = position

    print(f"rotation = {rot}")

    # each full rotation goes past zero
    hundreds = count_hundreds(rot)
    password += hundreds
    print(f"Password updated with {hundreds} hundreds in rotation")

    # remove the hundreds because they've been accounted for
    rot = drop_hundreds(rot)

    # calculate position after rotation
    position = position + rot
    print(f"position after rotation {position}")

    # account for passing zero
    if starting_position != 0 and (position <= 0 or position >= 100):
        password += 1
        print(f"Password updated because passed zero going negative or positive: {password}")

    # convert negative to positive
    if position < 0:
        position = 100 + position
        print(f"position after accounting for negative {position}")

    # drop hundreds (cases where position > 100)
    position = drop_hundreds(position)

    print(f"POSITION: {position}, PASSWORD: {password} \n")

print(f"FINAL PASSWORD: {password}")
