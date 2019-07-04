#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

from sys import argv
file_name = argv[1]
# аргумент на вход config_sw1.txt
ignore = ['duplex', 'alias', 'Current configuration']

with open(file_name) as srs, open('config_sw3_cleared.txt', 'w') as dest:
     for line in srs:
         if not (set(ignore) & set(line.split())):
             dest.write(line)
