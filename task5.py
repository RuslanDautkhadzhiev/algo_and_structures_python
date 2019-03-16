#-------------------------------------------------------------------------------
# Name:        task5
# Purpose: В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию (индекс) в массиве.
#
# Author:      DautkhadzhievRKH
#
# Created:     16.03.2019
# Copyright:   (c) DautkhadzhievRKH 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from random import random

N = 20
arr = [] # массив как список
for i in range(N):
        arr.append(int(random() * 100) - 50)
print(arr)

i = 0
j= -1 # индекс
while i < N:
    if arr[i] < 0 and j == -1:
        j = i
    elif arr[i] < 0 and arr[i] > arr[j]:
        j = i
    i += 1
print('Максимальный отрицательный эл-т %d встречается в массиве на %d-й позиции' % (arr[j], j+1))





