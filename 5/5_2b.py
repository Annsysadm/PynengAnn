# -*- coding: utf-8 -*-
'''
Задание 5.2b
Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
#!/usr/bin/env python
from sys import argv
ip = argv[1]

ip, ip_mask = net.split('/')
mask = ip_mask # mask
print('mask = ', mask)
ip = ip.split('.')
#print(ip)
ip = int(ip[0]), int(ip[1]), int(ip[2]), int(ip[3])
# перевод элементов из сторокового типа в int


# перевод из десятичной в двоичную и тип строка
ip_bin = f'{ip[0]:08b}{ip[1]:08b}{ip[2]:08b}{ip[3]:08b}'

ip_bin = ip_bin[:int(mask)] + '0' * (32 - int(mask))
#print(f'Введенный адрес сети в двоичном виде: {ip_bin:>38}')

print(ip_bin[:int(mask)])
print(32 - int(mask))

# Преобразование адреса сети в кортеж из четырех срезов и каждый срез в десятичный формат
ip_bin = int(ip_bin[:8], 2), int(ip_bin[8:16], 2), int(ip_bin[16:24], 2), int(ip_bin[24:32], 2)

print('ip_bin: ', ip_bin) # вывод на печать что получилось

# print('ip: ', ip)         # вывод на печать что получилось
# создаем строку для вывода маски в двоичном виде, строковый тип

ip_mask ='1'*int(ip_mask)+'0'*(32-(int(ip_mask))) # маска в виде строки из нулей и единиц

# Преобразование маски в кортеж из четырех срезов и каждый срез в десятичный формат
ip_mask = int(ip_mask[:8], 2), int(ip_mask[8:16], 2), int(ip_mask[16:24], 2), int(ip_mask[24:32], 2)
# print('mask int[]: ', ip_mask)
# print(type(ip_mask))

ip_template = '''
{0}
{1:<8}  {2:<8}  {3:<8}  {4:<8}
{1:08b}  {2:08b}  {3:08b}  {4:08b}'''

# print(ip_template.format('IP-address:', ip[0], ip[1], ip[2], ip[3]))
print(ip_template.format('Network:', ip_bin[0], ip_bin[1], ip_bin[2], ip_bin[3]))
print(ip_template.format('Mask: \n' + mask, ip_mask[0], ip_mask[1], ip_mask[2], ip_mask[3]))
