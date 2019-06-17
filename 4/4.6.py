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
oospf_route = ospf_route.replace('[', '').replace(']', '').replace(',', '')
# убираем лишние квадратные скобки и лишние запятые
f = ospf_route.split() # получился список

ip_template = '''
Protocol:              {}
Prefix:                {}
AD/Metric:             {}
Next-Hop:              {}
Last update:           {}
Outbound Interface     {}
'''
print(ip_template.format('OSPF', f[1], f[2], f[4], f[5], f[6]))