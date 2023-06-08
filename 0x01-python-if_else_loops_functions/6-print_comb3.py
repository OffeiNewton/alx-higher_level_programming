#!/usr/bin/python3

# Loop through the range of digits from 0 to 9
for i in range(0, 10):
    # Loop through the range of digits from i+1 to 10
    for j in range(i + 1, 10):
        # Print the combination of two digits
        print("{:d}{:d}".format(i, j), end="")
        # Print the separator if it's not the last combination
        if i != 8 or j != 9:
            print(", ", end="")

print()  # Print a new line
