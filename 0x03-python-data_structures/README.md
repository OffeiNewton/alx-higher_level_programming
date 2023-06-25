Python List Info
This project provides a C function, print_python_list_info, that can be used to retrieve basic information about Python lists. The function is implemented in C and can be called from Python using the provided shared library.

Table of Contents
Installation
Usage
Example
Contributing
License
Installation
To use the print_python_list_info function, follow these steps:

Clone the repository: git clone <repository-url>
Compile the C code into a shared library using the provided compilation command: gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,PyList -o libPyList.so -fPIC -I/usr/include/python3.4 100-print_python_list_info.c
Usage
The shared library libPyList.so can be used in Python scripts to call the print_python_list_info function. Here's how you can use it:

python
Copy code
import ctypes

lib = ctypes.CDLL('./libPyList.so')
lib.print_python_list_info.argtypes = [ctypes.py_object]

# Create a Python list
l = ['hello', 'World']

# Call the function to print the list info
lib.print_python_list_info(l)
The function takes a single argument, a Python list object (PyObject*), and prints the following information:

The size of the list ([*] Size of the Python List = <size>)
The allocated memory for the list ([*] Allocated = <allocated>)
The type of each element in the list (Element <index>: <type>)
Example
python
Copy code
import ctypes

lib = ctypes.CDLL('./libPyList.so')
lib.print_python_list_info.argtypes = [ctypes.py_object]

l = ['hello', 'World']
lib.print_python_list_info(l)

del l[1]
lib.print_python_list_info(l)

l = l + [4, 5, 6.0, (9, 8), [9, 8, 1024], "My string"]
lib.print_python_list_info(l)

l = []
lib.print_python_list_info(l)

l.append(0)
lib.print_python_list_info(l)

l.append(1)
l.append(2)
l.append(3)
l.append(4)
lib.print_python_list_info(l)

l.pop()
lib.print_python_list_info(l)
Output:

mathematica
Copy code
[*] Size of the Python List = 2
[*] Allocated = 2
Element 0: str
Element 1: str
[*] Size of the Python List = 1
[*] Allocated = 2
Element 0: str
[*] Size of the Python List = 7
[*] Allocated = 7
Element 0: str
Element 1: int
Element 2: int
Element 3: float
Element 4: tuple
Element 5: list
Element 6: str
[*] Size of the Python List = 0
[*] Allocated = 0
[*] Size of the Python List = 1
[*] Allocated = 4
Element 0: int
[*] Size of the Python List = 5
[*] Allocated = 8
Element 0: int
Element 1: int
Element 2: int
Element 3: int
Element 4: int
[*] Size of the Python List = 4
[*] Allocated = 8
Element 0
