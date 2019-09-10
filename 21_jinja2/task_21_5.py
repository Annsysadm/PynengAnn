# -*- coding: utf-8 -*-
'''
Задание 21.5

Создать шаблоны templates/gre_ipsec_vpn_1.txt и templates/gre_ipsec_vpn_2.txt,
которые генерируют конфигурацию IPsec over GRE между двумя маршрутизаторами.

Шаблон templates/gre_ipsec_vpn_1.txt создает конфигурацию для одной стороны туннеля,
а templates/gre_ipsec_vpn_2.txt - для второй.

Примеры итоговой конфигурации, которая должна создаваться на основе шаблонов в файлах:
cisco_vpn_1.txt и cisco_vpn_2.txt.


Создать функцию create_vpn_config, которая использует эти шаблоны для генерации конфигурации VPN на основе данных в
словаре data.

Параметры функции:
* template1 - имя файла с шаблоном, который создает конфигурацию для одной строны туннеля
* template2 - имя файла с шаблоном, который создает конфигурацию для второй строны туннеля
* data_dict - словарь со значениями, которые надо подставить в шаблоны

Функция должна возвращать кортеж с двумя конфигурациямя (строки), которые получены на основе шаблонов.

Примеры конфигураций VPN, которые должна возвращать функция create_vpn_config в файлах
cisco_vpn_1.txt и cisco_vpn_2.txt.
'''
from task_21_1 import generate_config

data = {
    'tun_num': 10,
    'wan_ip_1': '192.168.100.1',
    'wan_ip_2': '192.168.100.2',
    'tun_ip_1': '10.0.1.1 255.255.255.252',
    'tun_ip_2': '10.0.1.2 255.255.255.252'
}


def create_vpn_config(template1, template2, data_dict):
    """
    The function that uses templates to generate a VPN configuration based on data in dictionary data.
    :param template1: name of the template file that creates the configuration for one side of the tunnel.
    :param template2: name of the template file that creates the configuration for second side of the tunnel.
    :param data_dict: dictionary with values to be substituted into templates
    :return: is tuple with two configurations (strings), which are obtained on the basis of templates.
    """
    return generate_config(template1, data_dict), generate_config(template2, data_dict)


if __name__ == '__main__':
    create_vpn_config('templates/gre_ipsec_vpn_1.txt', 'templates/gre_ipsec_vpn_2.txt', data)