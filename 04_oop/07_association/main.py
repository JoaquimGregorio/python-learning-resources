"""
OOP - Association
"""
from classes import Writer, Pen, Typewriter

writer = Writer("Mário")
pen = Pen("Bic")
typewriter = Typewriter()

# Association:
writer.tool = typewriter
writer.tool.write()
