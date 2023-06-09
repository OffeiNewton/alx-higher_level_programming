#!/usr/bin/python3
import sys

args = sys.argv[1:]
num_args = len(args)

print("{} argument{}:".format(num_args, "" if num_args == 1 else "s"), end=' ')
print("." if num_args == 0 else "")

for i, arg in enumerate(args, start=1):
    print("{}: {}".format(i, arg))

