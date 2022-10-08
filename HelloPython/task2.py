# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый
# и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16]
# [2, 3, 5, 6] => [12, 15]
from audioop import minmax
from random import randint as rInt
number = int(input('Введите список:  '))

myList = []

for i in range(number):
    myList.append(rInt(-10, 10))

print(myList)

listLength = len(myList)
multiList = []
for i in range(listLength//2+1):
    element = myList[i]*myList[listLength-i-1]
    multiList.append(element)

print(multiList)