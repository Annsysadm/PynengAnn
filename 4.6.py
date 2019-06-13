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

b = ospf_route.split(',') # получился список
print('b =', b)
e = b[1:3]
print('e =', e)
c = b[0].split() # нулевой элемент списка b перевели в список
print('c =', c)
g = c[4]
print('g =', g)
print(str(c[:3]))
print(str(b[1:3]))
f = str(c[:3]) + g + str(b[1:3])
print('f =', f)

#d = f + c
#print('d =', d )


ip_template = '''
Protocol:              {1:<8}
Prefix:                {2:<8}
AD/Metric:             {3:<8}
Next-Hop:              {5:<8}
Last update:           {5:<8}
Outbound Interface     {6:<8}
'''

ip_template = '''
Protocol:              {1:<8}
Prefix:                {2:<8}
AD/Metric:             {3:<8}
Next-Hop:              {5:<8}
Last update:           {5:<8}
Outbound Interface     {6:<8}
'''