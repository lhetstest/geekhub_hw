# 7. Write a script to concatenate all elements in a list into a string and print it. List must include both strings and integers and must be hardcoded.

my_list = [23, '232', 'kwje', 34, 'a']

my_str = ''

for item in my_list:
    if type(item) == int:
        item=str(item)
        my_str+=item
    else:
        my_str+=item
print(my_str)