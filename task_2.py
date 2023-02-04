""" 
Напишите программу, которая найдёт 
произведение пар чисел списка. 
Парой считаем первый и последний элемент, второй и 
предпоследний и т.д. Пример:
[2, 3, 4, 5, 6] => [12, 15, 16];
[2, 3, 5, 6] => [12, 15] 
"""

import random

n = 5
list_1 = [random.randint(0, n) for i in range(n)]

my_sum = 0
print(f"\n{list_1} --> ", end=' ')
j = 1
for i in range(len(list_1)//2):
    my_sum = list_1[i] * list_1[-j]
    print(f"{my_sum}", end=' ')
    j += 1
print("\n")
