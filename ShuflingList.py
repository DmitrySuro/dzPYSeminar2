# Реализуйте алгоритм перемешивания списка.

import random
list = [1, 2, 3, 4, 5, 6]
for i in list:
    temp = list[i]
    list[i] = list[random.randint(0,5)]
    list[random.randint(0,5)] = temp
print(list)
