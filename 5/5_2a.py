# -*- coding: utf-8 -*-
'''
Задание 5.2a
Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети,
надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску, как в задании 5.2.
Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16
Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.1/30 - хост из сети 10.0.5.0/30
Если пользователь ввел адрес 10.0.1.1/24,
вывод должен быть таким:
Network:
10        0         1         0
00001010  00000000  00000001  00000000
Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000
Проверить работу скрипта на разных комбинациях сеть/маска.
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
net = input('Введите IP-адрес сети в формате 10.1.1.1/24:  ')
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
