# Write a script to get the maximum and minimum VALUE in a dictionary.

my_dict = {
    "one": 23,
    "two": 3,
    "three": 257,
    "four": 39
}

minimal = min(my_dict.values())
maximal = max(my_dict.values())
print('This value is minimal: ', minimal)
print('This value is maximal: ', maximal)