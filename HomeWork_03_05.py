# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи
# Решение оформлять в виде функций
# По возможности добавляйте docstring

k = 10
n_fibonacci = list(range(0, k+1))

def fibonacci(n_fibonacci):
    f_fibonacci = [0]*len(n_fibonacci)
    for i in range(0, len(f_fibonacci)):
        if n_fibonacci[i] == 0: f_fibonacci[i] = 0
        elif n_fibonacci[i] == 1: f_fibonacci[i] = 1
        else: f_fibonacci[i] = f_fibonacci[i-1] + f_fibonacci[i-2]
    return f_fibonacci

def negafibonacci(fibonacci):
    f_negafibonacci = [0]*len(fibonacci)
    oper = 1
    for i in range(1, len(f_negafibonacci)):
        f_negafibonacci[i] = oper * fibonacci[i]
        oper *= -1
    f_negafibonacci = f_negafibonacci[::-1] + fibonacci[1:]
    return f_negafibonacci

def num_negafibonacci(fibonacci):
    fibonacci = fibonacci[::-1] + fibonacci[1:]
    for i in range(0, len(fibonacci)):
        if fibonacci[i] != 0:
            fibonacci[i] = -fibonacci[i]
        else:
            break
    return fibonacci


f_fibonacci = fibonacci(n_fibonacci)
n_negafibonacci = num_negafibonacci(n_fibonacci)
f_negafibonacci = negafibonacci(f_fibonacci)

print('For n ∈ ', n_fibonacci, '->', '\nFibonacci numbers ∈ ', f_fibonacci)
print('')
print('For n ∈ ', n_negafibonacci, '->', '\nFibonacci & Negafibonacci numbers ∈ ', f_negafibonacci)
