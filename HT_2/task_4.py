# 4. Write a script which accepts a <number> from user and then <number> times asks user for string input. At the end script must print out result of concatenating all <number> strings.

amount = int(input('how many values you got: '))

new_string=''
for i in range(amount):
    new_string=new_string.join(input("Enter your value: "))
print(new_string)