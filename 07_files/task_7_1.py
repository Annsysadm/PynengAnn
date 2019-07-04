# -*- coding: utf-8 -*-
'''
Задание 7.1

Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
# исходная строка из 4_6 задачи
#ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

# import os
# print(os.getcwd())

with open('ospf.txt') as f:
    for line in f:
        route = line.replace(',', ' ').replace('[','').replace(']', '')
        # Таким образом можно присвоить несколько переменных за один раз:
        _, prefix, ad_metric, _, nhop, update, intf = route.split()
        # шаблон вывода:
        output = '\n{:25} {}'*6

        print(output.format("Protocol:", "OSPF",
                             "Prefix:", prefix,
                             "AD/Metric:", ad_metric,
                             "Next-Hop:", nhop,
                             "Last update:", update,
                             "Outbound Interface:", intf))