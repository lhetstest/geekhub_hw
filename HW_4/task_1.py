# 1. Написати функцiю season, яка приймає один аргумент (номер мiсяця вiд 1 до 12) та яка буде повертати пору року, до якої цей мiсяць належить (зима, весна, лiто або осiнь). У випадку некоректного введеного значення - виводити відповідне повідомлення.

def season(month):
    if month==12 or month<3:
        print("Winter")
    elif month>=3 and month<5:
        print("Spring")
    elif month>=5 and month<9:
        print("Summer")
    elif month>=9 and month<12:
        print("Autumn")

season(int(input("Please enter the number of the month: ")))