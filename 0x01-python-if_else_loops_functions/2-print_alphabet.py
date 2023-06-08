#!/usr/bin/python3

# ASCII value for lowercase 'a' is 97
# Loop through the range of 26 (number of lowercase letters) and print the corresponding character using string format
for i in range(26):
    print(chr(i + ord('a')), end='')
