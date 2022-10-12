# 9. Користувачем вводиться початковий і кінцевий рік. Створити цикл, який виведе всі високосні роки в цьому проміжку (границі включно). P.S. Рік є високосним, якщо він кратний 4, але не кратний 100, а також якщо він кратний 400.

first_yr = int(input("Type the 1st number: "))
second_yr = int(input("Type the 1st number: "))

leap_yr = []
for year in range(first_yr, second_yr):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        leap_yr.append(year)
        
print(leap_yr)