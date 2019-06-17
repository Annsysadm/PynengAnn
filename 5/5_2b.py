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

ip = ip.split('/')
m = int(ip[1]) # mask
number_of_nulls = 32 - m
ip = ip[0].split('.')

ip[0], ip[1], ip[2], ip[3] = int(ip[0]), int(ip[1]), int(ip[2]), 0

print(f'''Network:
{ip[0]:<8}  {ip[1]:<8}  {ip[2]:<8}  {ip[3]:<8}
{ip[0]:08b}  {ip[1]:08b}  {ip[2]:08b}  {ip[3]:08b}''')

mask = m * '1' + number_of_nulls * '0'
list_mask = [int(mask[:8], 2), int(mask[8:16], 2), int(mask[16:24], 2), int(mask[24:32], 2)]

print(f'''Mask:
/{m}
{list_mask[0]:<8}  {list_mask[1]:<8}  {list_mask[2]:<8}  {list_mask[3]:<8}
{list_mask[0]:<08b}  {list_mask[1]:<08b}  {list_mask[2]:<08b}  {list_mask[3]:<08b}
''')
