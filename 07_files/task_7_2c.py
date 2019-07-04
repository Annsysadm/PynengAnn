# -*- coding: utf-8 -*-
'''
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
#!/usr/bin/env python
from sys import argv
file_srs, file_dest = argv[1:]
ignore = ['duplex', 'alias', 'Current configuration']

with open(file_srs) as srs, open(file_dest, 'w') as dest:
    for line in srs:
        if not (set(ignore) & set(line.split())):
            dest.write(line)
