#!/usr/bin/python3

import sys
import types

if sys.version_info < (3, 8):
    print("Please make sure you are running Python 3.8.x")
    sys.exit(1)

try:
    module = types.ModuleType("hidden_4")
    with open("hidden_4.pyc", "rb") as file:
        code = file.read()
    exec(code, module.__dict__)

    names = sorted(name for name in dir(module) if not name.startswith("__"))

    for name in names:
        print(name)

except FileNotFoundError:
    print("File 'hidden_4.pyc' not found.")

