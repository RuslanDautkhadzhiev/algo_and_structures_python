#-------------------------------------------------------------------------------
# Name:        task9
# Purpose: Найти максимальный элемент среди минимальных элементов столбцов матрицы.
#
# Author:      DautkhadzhievRKH
#
# Created:     16.03.2019
# Copyright:   (c) DautkhadzhievRKH 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from random import random

M = 5 # кол-во столбцов
N = 5 # кол-во строк
a = []
for i in range(N):
    b = []
    for j in range(M):
        n = int(random() * 200) # 0-200
        b.append(n)
        print('%5d' % n, end='')
    a.append(b)
    print()

i_max = -1
for j in range(M):
    i_min = 200
    for i in range(N):
        if a[i][j] < i_min:
            i_min = a[i][j]
    if i_min > i_max:
        i_max = i_min
print('Максимальный элемент среди минимальных %d' % i_max)




