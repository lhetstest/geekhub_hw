# Write a script to get the maximum and minimum VALUE in a dictionary.

my_dict = {
    "one": 23,
    "two": 3,
    "three": 257,
    "str1": "hello",
    "four": 39,
    "boole": True
}

the_list = []
for value in my_dict.values(): 
    if type(value) == int:
        the_list.append(value)

minimal = min(the_list)
maximal = max(the_list)
print('This value is minimal: ', minimal)
print('This value is maximal: ', maximal)