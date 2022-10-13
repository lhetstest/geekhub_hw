# Write a script to remove values duplicates from dictionary. Feel free to hardcode your dictionary.

my_dic = {
    "one": 23,
    "two": 3,
    "three": 257,
    "four": 39,
    "car": "Ford",
    "name": "Lucy",
    "age": 240,
    "mana": 180,
    "married": False,
    "mother": "Lucy"
}

# print(set(my_dic.values()))
temp = []
res = dict()
for key, val in my_dic.items():
    if val not in temp:
        temp.append(val)
        res[key] = val

print(res)
# result.update(my_dic)