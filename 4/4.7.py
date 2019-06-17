# -*- coding: utf-8 -*-
'''
Задание 4.7
Преобразовать MAC-адрес mac в двоичную строку такого вида:
'101010101010101010111011101110111100110011001100'
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
#1 Variant 
'''
mac = 'AAAA:BBBB:CCCC'
b = mac.replace(':', '')     # убрали двоеточие. Тип остался строка
b1 = int(b, 16)              # перевели из 16ричной системы в 10тичную
print('в десятичной: ', b1)  # вывод b1, чтобы посмотреть какое получилось число
b2 = str(bin(b1))            # перевод b1 из 10тичной в 2ичную и перевод в строковый тип
print('в двоичной:', b2)
b2 = b2[2:]                  # убираем первые два символа обозначения 2ичной системы
print('ответ:', b2)
'''
#2 Variant

mac = mac.replace(':', '')     # убрали двоеточие. Тип остался строка
mac = int(mac, 16)             # перевели из 16ричной системы в 10тичную

print("{0:b}".format(mac))
