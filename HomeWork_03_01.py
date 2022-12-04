from gbfunctions import random_list

# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

list_length = int(input('Введите длину списка: \n'))
numbers = []

numbers = random_list(list_length)

odd_numbers = numbers[1::2]
sum = sum(odd_numbers)
convert_list = ', '.join(map(str,odd_numbers))

print(numbers, ' -> на нечётных позициях элементы:', convert_list, ' Ответ:', sum)