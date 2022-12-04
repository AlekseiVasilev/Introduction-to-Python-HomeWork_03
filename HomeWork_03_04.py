import time
# Напишите программу, которая будет преобразовывать десятичное число в двоичное. Подумайте, как это можно решить с помощью рекурсии.
# Не использовать функцию bin
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

num = int(input('Введите число:\n'))

def to_binary(num):
    binar = str('')
    while num - num // 2 > 0:
        if num % 2 != 0:
            binar = '1' + binar
            # time.sleep(0.1)
            # print(bin, '!=')
        else:
            binar = '0' + binar
            # time.sleep(0.1)
            # print(bin, 'else')
        num = num // 2
    return binar

binar = to_binary(num)

print('Number: ',num, '\n In binary system - >', binar)