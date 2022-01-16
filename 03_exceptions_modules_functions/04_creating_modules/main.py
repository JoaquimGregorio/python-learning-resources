import calc

# it will execute all the code inside the module
# if we don't use the if condition (if __name__ == "__main__") ...

# the __name__ of the first file that is being executed will
# always be "__main__"
# print(__name__)

print(calc.PI)

list1 = [2, 4]
print(calc.multiply_list(list1))
