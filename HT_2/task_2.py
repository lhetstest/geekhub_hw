'''
Write a script which accepts two sequences of comma-separated colors from user. Then print out a set containing all the colors from color_list_1 which are not present in color_list_2.
'''
color_list_1 = input('type the comma-separated colors: ')
color_list_2 = input('type the comma-separated colors: ')
colors1 = color_list_1.split(',')
colors2 = color_list_2.split(',')

colors1_list=[]
for value in colors1:
    value = int(value)
    colors1_list.append(value)
    
colors2_list=[]
for value in colors2:
    value = int(value)
    colors2_list.append(value)


set1 = set(colors1_list)
set2 = set(colors2_list)

elements = set1.intersection(set2)

for item in elements:
    set1.remove(item)
print(set1)