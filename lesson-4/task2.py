#-------------------------------------------------------------------------------
# Name:        task2
# Purpose:Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»
# Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов. Результаты анализа сохранить в виде комментариев в файле с кодом.
#
# Author:      DautkhadzhievRKH
#
# Created:     23.03.2019
# Copyright:   (c) DautkhadzhievRKH
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from math import sqrt
import timeit

# решето Аткина

def sieveOfAtkin(limit, k): # limit - обшее кол-во проствых чисел, k - позиция искомого числа
    a = [2, 3]
    is_prime = [False]*(limit +1 )
    for x in range(1,int(sqrt(limit)) + 1):
        for y in range(1,int(sqrt(limit)) + 1):
            n = 4 * x ** 2 + y ** 2
            if n <= limit and (n % 12 == 1 or n % 12 == 5) : is_prime[n] = not is_prime[n]
            n = 3* x ** 2+ y ** 2
            if n <= limit and n % 12==7 : is_prime[n] = not is_prime[n]
            n = 3 *x **2 - y **2
            if x > y and n <= limit and n % 12 == 11 : is_prime[n] = not is_prime[n]
    for x in range(5, int(sqrt(limit))):
        if is_prime[x]:
            for y in range(x ** 2, limit + 1, x ** 2):
                is_prime[y] = False
    for i in range(5, limit):
        if is_prime[i] : a.append(i)
    return a[k-1]


# решето Эратосфена

# вариация с множеством

def sieveOfEratosthenes(limit, k):
    lim = limit+1
    not_prime = set()
    primes = []

    for i in range(2, lim):
        if i in not_prime:
            continue

        for f in range(i * 2, lim, i):
            not_prime.add(f)

        primes.append(i)

    return primes[k-1]


c = int(input('Укажите порядковый номер искомого простого числа: '))

time = timeit.timeit('sieveOfAtkin({}, {})'.format(10000, c),
                         setup='from __main__ import sieveOfAtkin', number=100)
print('\tTotal time: {}\n\tTime per iteration: {}'.format(time, float(time)/100))

time = timeit.timeit('sieveOfEratosthenes({}, {})'.format(10000, c),
                         setup='from __main__ import sieveOfEratosthenes', number=100)
print('\tTotal time: {}\n\tTime per iteration: {}'.format(time, float(time)/100))

'''
10-е число 100 раз:

    Решето Аткина
    Total time: 2.3485625420443927
	Time per iteration: 0.023485625420443926

    Решето Эратосфена
    Total time: 0.3809374846911182
	Time per iteration: 0.003809374846911182


100-е число 100 раз:

    Решето Аткина
    Total time: 2.3462978681711983
	Time per iteration: 0.023462978681711984

    Решето Эратосфена
    Total time: 0.3811427237626184
	Time per iteration: 0.0038114272376261835

    1000-е число 100 раз:

    Решето Аткина
    Total time: 2.3468722814227903
	Time per iteration: 0.0234687228142279

    Решето Эратосфена
   	Total time: 0.3772598310635895
	Time per iteration: 0.0037725983106358953

    Сложность решето Аткина: O(N/loglogN)
    Сложность решето Эратосфена: O(NloglogN)

    Решето Эратосфена выигрывает однозначно в данном случае.
    '''
