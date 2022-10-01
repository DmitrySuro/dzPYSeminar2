# Реализуйте алгоритм перемешивания списка.

import random
my_list = [1, 2, 3, 4, 5, 6]
for i in range(len(my_list)):
    random_index =  random.randint(0,len(my_list) -1)
    if my_list[i] != my_list[random_index]:
        my_list[i],my_list[random_index] = my_list[random_index],my_list[i]
        print(my_list[i], my_list[random_index])
print(my_list)
