import math
# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 2, 8, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

# numbers = [2, 3, 4, 8, 5, 6]

numbers = '2, 3, 2, 8, 5, 6'.split(', ')
numbers = list(map(int, numbers))

print(numbers)

mod_numbers = []


for i in range (int(math.ceil(len(numbers) / 2))):
    mod_numbers.append(numbers[i] * numbers[len(numbers) - 1 - i])

    
print(mod_numbers)
