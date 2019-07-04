# -*- coding: utf-8 -*-
'''
Задание 4.6
Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface     FastEthernet0/0
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
ospf_route = ospf_route.replace('[', ' ') # убираем лишние квадратные скобки
ospf_route = ospf_route.replace(']', ' ') # убираем лишние квадратные скобки
b = ospf_route.split(',') # получился список
print('b =', b)
e = b[1:3]
g = b[-1].strip()
g = g.split()
h = b[-2].strip()
h = h.split()
print('e =', e)
print('g =', g)
print('h =', h)
c = b[0].split() # нулевой элемент списка b перевели в список
c.pop(3)         #удалили 3 элемент из списка с
print('c =', c)
f = c + h + g  # результирующий список
print('f =', f)
print(type(f))

ip_template = '''
Protocol:              {}
Prefix:                {}
AD/Metric:             {}
Next-Hop:              {}
Last update:           {}
Outbound Interface     {}
'''
print(ip_template.format('O', '10.0.24.0/24', '110/41', '10.0.13.3', '3d18h', 'FastEthernet0/0'))