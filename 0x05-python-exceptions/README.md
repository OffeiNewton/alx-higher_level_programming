Python Information Functions
This repository contains C code that provides functions to print basic information about Python objects such as lists, bytes, and floats. The code is designed to be used in conjunction with Python programs.

Installation
To use the Python information functions, follow these steps:

Ensure you have the necessary Python development packages installed on your system. On Ubuntu, you can install them with the following command:

shell
Copy code
sudo apt-get install python3-dev
Clone this repository to your local machine.

shell
Copy code
git clone <repository-url>
Build the shared library by running the provided compilation command.

shell
Copy code
gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 103-python.c
Usage
To use the Python information functions in your Python program, follow these steps:

Import the ctypes module.

python
Copy code
import ctypes
Load the shared library containing the functions.

python
Copy code
lib = ctypes.CDLL('./libPython.so')
Define the argument types for each function.

python
Copy code
lib.print_python_list.argtypes = [ctypes.py_object]
lib.print_python_bytes.argtypes = [ctypes.py_object]
lib.print_python_float.argtypes = [ctypes.py_object]
Call the desired function with the appropriate Python object.

python
Copy code
# Example usage
l = [b'Hello', b'World']
lib.print_python_list(l)
Function Descriptions
The following functions are available in the code:

print_python_list
Prints basic information about a Python list object.

Prototype: void print_python_list(PyObject *p)
Parameters:
p: A PyObject pointer representing the Python list object.
print_python_bytes
Prints basic information about a Python bytes object.

Prototype: void print_python_bytes(PyObject *p)
Parameters:
p: A PyObject pointer representing the Python bytes object.
print_python_float
Prints basic information about a Python float object.

Prototype: void print_python_float(PyObject *p)
Parameters:
p: A PyObject pointer representing the Python float object.
