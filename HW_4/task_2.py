# 2. Створіть 3 рiзних функцiї (на ваш вибiр). Кожна з цих функцiй повинна повертати якийсь результат (напр. інпут від юзера, результат математичної операції тощо). Також створiть четверту ф-цiю, яка всередині викликає 3 попередні,
# обробляє їх результат та також повертає результат своєї роботи. Таким чином ми будемо викликати одну (четверту) функцiю, а вона в своєму тiлi - ще 3.

def add(a,b):
    return a+b

def spell(word):
    return f"Did I hear correct? {word}"

def greeting(name):
    return f"Grüß got, {name}"

def communicate(age):
    if age>18:
        price = add(age, 25)
        name = input("Please enter your name: ")
        print(spell(name))
        print(greeting(name))
        print(f'You are allowed to donate {price} euro')
    else:
        print("it is forbidden to use at your age")
communicate(int(input("How old are you? ")))