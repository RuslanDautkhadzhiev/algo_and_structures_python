#-------------------------------------------------------------------------------
# Name: task1
#
# Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков..
#
# Author:      DautkhadzhievRKH
#
# Created:     23.03.2019
# Copyright:   (c) DautkhadzhievRKH 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import timeit

# рекурсивная функция для записи числа в обратном порядке
def reverseOfNumber(num):
    if (num < 10): return num
    return str(num % 10) + str(reverseOfNumber(num // 10))

# обычная фунция для тех же действий
def rev_num(n):
    m = 0
    while n > 0:
     m = m * 10 + n % 10
     n = n // 10
    return m


a = int(input('Введите любое натуральное число: '))

time = timeit.timeit('reverseOfNumber({})'.format(a),
                         setup='from __main__ import reverseOfNumber', number=100)
print('\tTotal time: {}\n\tTime per iteration: {}'.format(time, float(time)/100))

time = timeit.timeit('rev_num({})'.format(a),
                         setup='from __main__ import rev_num', number=100)
print('\tTotal time: {}\n\tTime per iteration: {}'.format(time, float(time)/100))

'''
Результаты поворота 100 раз числа 15486879231

Рекурсия:
	Toal time: 0.0005638471215460362
	Time per iteration: 5.638471215460361e-06
    Сложность: O(N)

    Обычная функция:
	Total time: 0.00019819498480238293
	Time per iteration: 1.981949848023829e-06
    Сложность:  O(N^2)

Обычная функция быстрее.
'''
