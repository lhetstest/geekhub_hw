# 1. Написати функцiю season, яка приймає один аргумент (номер мiсяця вiд 1 до 12) та яка буде повертати пору року, до якої цей мiсяць належить (зима, весна, лiто або осiнь). У випадку некоректного введеного значення - виводити відповідне повідомлення.

def season(month):
    try:
        month = int(input("Please enter the number of the month: "))
    
        if month==12 || month<3:
            print()
        elif month>=3 &&
    except error:
        print("Type the positive number less or equal to 12")