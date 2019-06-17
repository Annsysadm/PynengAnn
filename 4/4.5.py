# -*- coding: utf-8 -*-
'''
Задание 4.5
Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2.
Результатом должен быть список: ['1', '3', '8']
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
command2 = 'switchport trunk allowed vlan 1,3,8,9'
a = command1.split()
b = command2.split()

vlans1 = set(a[-1].split(','))
vlans2 = set(b[-1].split(','))
vlans3 = list(vlans1.intersection(vlans2))
vlans3.sort()
print(vlans3)
