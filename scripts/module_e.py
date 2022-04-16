# scripts/module_e.py

import os
import sys
print(os.pardir)
print(os.path.dirname(__file__))
print(os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    os.pardir)
))
PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    os.pardir)
)
sys.path.append(PROJECT_ROOT)
print(sys.path)

import utils
print(utils.capitalize("this is all in lower case."))