#-------------------------------------------------------------------------------
# Name:        task3
# Purpose: По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти точки.
#
# Author:      DautkhadzhievRKH
#
# Created:     09.03.2019
# Copyright:   (c) DautkhadzhievRKH 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
print('Задайте координаты точки A(x1;y1):')
x1 = float(input('\tx1 = '))
y1 = float(input('\ty1 = '))
print('Задайте координаты точки B(x2;y2):')
x2 = float(input('\tx2 = '))
y2 = float(input('\ty2 = '))
if x1 ==0 and x2 == 0: # в этом случае невозможно вычислить коэффициент k
    print('Указанные координаты не принадлежат прямой!')
else:
    k = (y1 - y2) / (x1 - x2) # вычисляем коэффициент пропорциональности
    b = y2 - k*x2
    print('Уравнение прямой, проходящей через эти точки:')
    print('y = %.2f*x + %.2f' % (k, b))
