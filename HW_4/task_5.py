# 5. Ну і традиційно - калькулятор :slightly_smiling_face: Повинна бути 1 функцiя, яка приймає 3 аргументи - один з яких операцiя, яку зробити! Аргументи брати від юзера (можна по одному - окремо 2, окремо +, окремо 2; можна всі разом - типу 2 + 2). Операції що мають бути присутні: +, -, *, /, %, //, **. Не забудьте протестувати з різними значеннями на предмет помилок!

from tokenize import Name


def calc(a,b):
    
    operation = input("type the symbol for operation(+, -, *, /, %, //, **): ")
    
    if operation == "+":
        print(a+b)
    elif operation == "-":
        print(a-b)
    elif operation == "*":
        print(a*b)
    elif operation == "/":
        try:
            c=a/b
            print(c)
        except ZeroDivisionError:
            print("B should not be zero")
    elif operation == "%":
        print(a%b)
    elif operation == "//":
        print(a//b)
    elif operation == "**":
        print(a**b)
try:
    a = int(input("Enter the 1st number: "))
    b = int(input("type the 2nd number: "))
except ValueError: 
    print("Type only numbers")
try:
    calc(a,b)
except NameError:
    a = int(input("Enter the 1st number: "))
    b = int(input("type the 2nd number: "))
    calc(a,b)
