# 3. Write a script which accepts a <number> from user and print out a sum of the first <number> positive integers.
number = int(input("type the number: "))

sum = 0
for i in range(number):
    sum+=i
print(sum)