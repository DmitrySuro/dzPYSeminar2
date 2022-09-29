# Задайте список из n чисел последовательности
# $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# Пример:

# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19} ???

n = int(input('Insert your number:'))
my_dict = []
for i in range(1, n + 1):
    my_dict.append([i, (1 / i + 1)**i])
print(dict(my_dict))
