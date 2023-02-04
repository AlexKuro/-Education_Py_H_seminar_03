""" 
3. Задайте список из вещественных чисел. 
Напишите программу, которая найдёт разницу между 
максимальным и минимальным значением дробной части элементов.
Пример:
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19 
"""
import math

list_1 = [1.1, 1.2, 3.1, 5, 10.01]


def differenceReal1(list_1):  # Вариант 1
    """ 
    Разница между максимальным и минимальным значением дробной части элементов 
    """
    list_2 = []

    for i in range(len(list_1)):
        list_2.append(math.modf(list_1[i]))

    mini = min(list_2)
    maxi = max(list_2)

    a = str(maxi[0] - mini[0])
    return float(a[:4])


def differenceReal2(list_1):  # Вариант 2
    """ 
    Разница между максимальным и минимальным значением дробной части элементов 
    """
    list_2 = []

    for i in range(len(list_1)):
        list_2.append(list_1[i] - int(list_1[i]))

    mini = min(list_2)
    maxi = max(list_2)

    a = str(maxi - mini)
    return float(a[:4])


print(f"\n Список {list_1} --> {differenceReal1(list_1)}\n")

print(f"\n Список {list_1} --> {differenceReal2(list_1)}\n")
