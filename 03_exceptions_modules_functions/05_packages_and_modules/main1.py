"""
Import modules from inside other modules without main file.
It can be useful for testing.
"""
try:
    import sys
    import os

    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
except ImportError:
    raise
