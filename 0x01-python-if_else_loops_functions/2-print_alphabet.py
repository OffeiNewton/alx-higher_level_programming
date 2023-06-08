#!/usr/bin/python3

# ASCII values for lowercase letters start from 97
# Loop through the ASCII range and print the corresponding character using string format
for i in range(97, 123):
    print("{:c}".format(i), end="")
