#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
input_vlan = int(input('Input VLAN: '))

line_list = []
with open('CAM_table.txt') as srs:
    for line in srs:
        if not line.startswith('-') and not line.startswith('\n') and line.split()[0].isdigit():
            vlan, mac, _, intf = line.split()
            line_list.append([int(vlan), [mac, intf]])
            result = sorted(line_list)
            # result = sorted([vlan, mac, intf])
            # print(result)
            # print(f'{vlan:8}{mac:17}{intf:8}')
    # print(result)
# print(result)
print('line_list', line_list)
print('result', result)

for vlann, element in result:
    if vlann == input_vlan:
        print(f'{vlann:<5} {element[0]:17}{element[1]:8}')
