#-------------------------------------------------------------------------------
# Name: task5
#
# Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
# Author:      DautkhadzhievRKH
#
# Created:     11.03.2019
# Copyright:   (c) DautkhadzhievRKH 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------


for i in range(32, 128):
    print("%5d-%s" % (i, chr(i)), end='')
    if i % 10 == 0:
        print()
print()



