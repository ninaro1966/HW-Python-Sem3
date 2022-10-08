# 3.Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным
#значением дробной части элементов. Если число целое, то его дробная часть не считается за 0 и оно в сравнении не участвует
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19
from audioop import minmax
from random import randint as rInt
# Работающий вариант из Google, не получилось округлить в коде самой - не ясно, сколько знаков.
# my_list = [1.1, 1.2, 3.1, 5, 10.01]
# min = 1
# max = 0
# for i in my_list:
#  if (i - int(i)) <= min:
#         min = i - int(i)
#  if (i - int(i)) >= max:
#         max = i - int(i)
# print(max-min)
# Как получить дробную часть
# number = 6.5678
# print(round(number%1), 2))               деление с остатком от 1(отбрасываем цифры до запятой)
# print(round(number - int(number), 2))      или  удалить у него целую часть
# # ответ - from decimal import Decimal
# Мантисса — это, по сути, число, записанное без точки. Экспонента — это степень, в которую нужно возвести некое число N
# (как правило, N = 2), чтобы при перемножении на мантиссу получить искомое число (с точностью до разрядности мантиссы).
# Выглядит это примерно так: x = m * N e , где m и e — целые числа, записанные в бинарном виде в выделенных под них битах.
from random import uniform as uI
from random import randint as rInt
from decimal import Decimal

number = int(input('Введите размер списка: '))

myList = []

for i in range(number):
    coef = rInt(1, 4)
    number = Decimal(f'{round(uI(-10,10), coef)}')
    myList.append(number)

numList = []
mantissa = []

for num in myList:
    numList.append(float(num))
    if abs(num) - int(abs(num)) != 0.0:
            mantissa.append(abs(num) - abs(int(num)))

print(numList)
print(f'Максимальная {max(mantissa)} и минимальная {min(mantissa)} мантиссы')
print(f'Разница мантисс {max(mantissa) - min(mantissa)}')