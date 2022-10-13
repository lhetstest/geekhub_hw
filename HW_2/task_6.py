# 6. Write a script to check whether a value from user input is contained in a group of values.
#     e.g. [1, 2, 'u', 'a', 4, True] --> 2 --> True
#          [1, 2, 'u', 'a', 4, True] --> 5 --> False

my_list = [1, 2, 'u', 'a', 4, True]

value = input("Type your guess here: ")

try:
    my_list.index(value)
    print(True)
except ValueError:
    print(False)
