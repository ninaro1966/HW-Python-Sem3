# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# Пример из второй лекции
# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
#
#     list[int] = []
#     for e in range(1, 10):
#         list.append(fib(e))
#     print(list)

# k = int(input('Please input integer: '))   # - но по шкале "больше 0"
# k1 = 0
# k2 = 1
# if k <= 0:
#     k = input('Input integer > 0: ')
# elif k == 1:
#     print(k1)
# elif k == 2:
#     print(k2)
# else:
#     print(0, 1, end=' ')
# for i in range(2, k):
#     k1, k2 = k2, k1 + k2
#     print(k2, end=' ')

number = int(input('Введите предел последовательности Фибоначчи: '))

def Fibona44i(number):
    list = [1, 0, 1]                    # обрабатываем 0 и 1
    for i in range(2, number+1):
        list.append(list[i-1]+list[i]) # для отрицательных чисел сисок с -1 добавляем к обработанным 0 и 1


    for i in range(0, -number+1, -1):   #недофибоначчи для отрицательных чисел делает разность и вставляет в нулевую позицию списка
            list.insert(0, list[1]-list[0])

    return list


print(Fibona44i(number))