# Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

user_number = input('Please insert your number: ')
sum_digits = 0
for i in str(user_number):
    if i != '.':
        sum_digits += int(i)
print(sum_digits)
