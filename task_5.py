
""" 
5. Задайте число. Составьте список чисел Фибоначчи, 
в том числе для отрицательных индексов.
Пример:
- для k = 8 список будет выглядеть так: 
[-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
"""

f = f1 = 0
f2 = 1
fibonachi = [0, 1]
n = 10
print("\nCписок чисел Фибоначчи, в том числе для отрицательных индексов:")
print(f"Для n = {n} список выглядит так: ", end='')
for i in range(0, n):
    f = f1 + f2
    f1 = f2
    f2 = f
    fibonachi.append(f2)

negafibonachi = [1]
f = f1 = 0
f2 = 1
for i in range(0, n):
    f = f1 + (-f2)
    f1 = f2
    f2 = f
    negafibonachi.append(f2)

fibonachiN = negafibonachi[::-1]

for i in fibonachi:
    fibonachiN.append(i)
print(fibonachiN, end='\n\n')
