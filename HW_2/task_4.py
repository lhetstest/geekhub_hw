# 4. Write a script which accepts a <number> from user and then <number> times asks user for string input. At the end script must print out result of concatenating all <number> strings.

amount = int(input('how many values you got: '))

new_string=''
for i in range(amount):
    user_input = input('Enter your value: ')
    
    new_string += user_input
print(new_string)