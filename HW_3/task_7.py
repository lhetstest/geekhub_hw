#  Write a script which accepts a <number>(int) from user and generates dictionary in range <number> where key is <number> and value is <number>*<number>
#     e.g. 3 --> {0: 0, 1: 1, 2: 4, 3: 9}

user_input = int(input("Enter the max value: "))

my_dict = {}
for i in range(user_input+1):
    my_dict.update({f'{i}':f'{i*i}'})
print(my_dict)