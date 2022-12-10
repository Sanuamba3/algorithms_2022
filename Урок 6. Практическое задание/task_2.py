"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""
from memory_profiler import profile
from memory_profiler import memory_usage

user_number = 100
# 1 Способ - собственный декоратор:

def decor(func):
    def wrapper_1(*args, **kwargs):
        m1 = memory_usage()
        res = func(args[0])
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff
    return wrapper_1

@decor
def recur_sum_1(number):
    if number == 1:
        return number
    else:
        return recur_sum_1(number-1)[0] + number

# 2 Способ - обернуть функцию с рекурсией
@profile
def wrapper_2(input_number):
    def recur_sum_2(number):
        if number == 1:
            return number
        else:
            return recur_sum_2(number - 1) + number
    return recur_sum_2(input_number)

recur_check, mem1 = recur_sum_1(user_number)
if recur_check == user_number * (user_number + 1) / 2:
    print('Равенство верно!')
print(mem1)

if wrapper_2(user_number) == user_number * (user_number + 1) / 2:
    print('Равенство верно!')