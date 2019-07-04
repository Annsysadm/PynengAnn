# -*- coding: utf-8 -*-
'''
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
#!/usr/bin/env python

from sys import argv
file_name = argv[1]

ignore = ['duplex', 'alias', 'Current configuration']
with open(file_name) as f:
    for line in f:
        for command in ignore:
            if not line.startswith('!') and not (set(ignore) & set(line.split())):
                print(line, end='')