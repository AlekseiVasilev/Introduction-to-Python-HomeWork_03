import math
# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
# [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91

numbers = '4.07, 5.1, 8.2444, 6.98'.split(', ')
numbers = list(map(str, numbers))

print(numbers)

def integer_remove(numbers):
    for i in range(len(numbers)):
        numbers[i] = str(numbers[i]).split('.')
        numbers[i][0] = 0
        numbers[i] = '.'.join(map(str, numbers[i]))
    return numbers

numbers = list(map(float, integer_remove(numbers)))

min_num = min(numbers)
max_num = max(numbers)

# max_num = 0

# for i in range(len(numbers)):
#     if numbers[i] > max_num:
#         max_num = numbers[i]

# min_num = max_num

# for i in range(len(numbers)):
#     if numbers[i] < min_num:
#         min_num = numbers[i]

res = round((max_num - min_num), 2)
print(numbers, '; => min = ', min_num, '; max = ', max_num, '; difference = ', res)



# mod_numbers = [0]*len(numbers)

# def remainder(num):
#     num = str(num).split('.')
#     return num
# mod_numbers = [remainder(i) for i in range(len(mod_numbers))]
# print(mod_numbers)
