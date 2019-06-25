# -*- coding: utf-8 -*-
'''
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

input_ip_address = input('Введите ip-address: ')
list_input_address = (input_ip_address.split('.'))
oct1, oct2, oct3, oct4 = int(list_input_address[0]), int(list_input_address[1]), int(list_input_address[2]), int(list_input_address[3])

ip_correct = False
while not ip_correct:
    if not list_input_address[0].isdigit() and list_input_address[1].isdigit() and list_input_address[2].isdigit() and list_input_address[3].isdigit():
        print('Неправильный ip-адрес (не состоит из цифр)\n')
        input_ip_address = input('Введите ip-address снова: ')
    elif len(input_ip_address.split('.')) != 4:
        print('Неправильный ip-адрес - не состоит из 4 элементов разделенных точкой\n')
        input_ip_address = input('Введите ip-address снова: ')
    elif not (oct1 in range(256) and  oct2 in range(256) and  oct3 in range(256) and oct4 in range(256)):
        print('Attention! Неправильный ip-адрес.\n')
        input_ip_address = input('Введите ip-address снова: ')
    else:
        ip_correct = True
'''
    if ip_address[0] in range(1, 224):
        result = 'unicast'
    elif ip_address[0] in range(224, 239):
        result = 'multicast'
    elif ip_address == [255, 255, 255, 255]:
        result = 'local broadcast'
    elif ip_address == [0, 0, 0, 0]:
        result = 'unassigned'
    else:
        result = 'unused'
'''