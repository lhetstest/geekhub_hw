'''
Write a script which accepts two sequences of comma-separated colors from user. Then print out a set containing all the colors from color_list_1 which are not present in color_list_2.
'''
color_list_1 = input('type the comma-separated colors: ')
color_list_2 = input('type the comma-separated colors: ')
colors1 = set(color_list_1.split(','))
colors2 = set(color_list_2.split(','))

print(colors1.difference(colors2))