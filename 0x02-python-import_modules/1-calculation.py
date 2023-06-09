#!/usr/bin/python3

a = 10
b = 5

from calculator_1 import add, subtract, multiply, divide

add_result = add(a, b)
subtract_result = subtract(a, b)
multiply_result = multiply(a, b)
divide_result = divide(a, b)

print("The sum of {} and {} is {}".format(a, b, add_result))
print("Subtracting {} from {} gives {}".format(b, a, subtract_result))
print("Multiplying {} and {} gives {}".format(a, b, multiply_result))
print("Dividing {} by {} gives {}".format(a, b, divide_result))

