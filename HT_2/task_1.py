#Write a script which accepts a sequence of comma-separated numbers from user and generates a list and a tuple with those numbers.
new_list = []
values=input("Type some values: ")
some_list = values.split(",")

for value in some_list:
    value = int(value)
    new_list.append(value)
    
print(new_list)
new_tuple = tuple(new_list)
print(new_tuple)