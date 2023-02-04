""" 
4. Напишите программу, которая будет 
преобразовывать десятичное число в двоичное.
Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10 
"""
import random

n = random.randint(0, 100)
x = n
print(f"\nПреобразование десятичного числа {n} в двоичное --> ", end='')
list_bin = []
while n > 0:
    list_bin.append(n % 2)
    list_bin.insert(0, list_bin.pop())
    n = n//2

print(*list_bin, sep='')
print(f"Проверка --------------------------------------> {bin(x)}\n\n", end='')
