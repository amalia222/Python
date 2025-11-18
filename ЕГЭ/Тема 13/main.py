'''
Узлы с IP-адресами 98.162.71.150 и 98.162.71.140 находятся в одной сети.
Чему равно наибольшее количество возможных единиц в маске этой сети?
'''
from ipaddress import ip_network

for mask in range(32):
    network1 = ip_network(f'98.162.71.150/{mask}', False)
    network2 = ip_network(f'98.162.71.140/{mask}', False)
    if network1.network_address == network2.network_address:
        print(f'{network1.netmask:b}'.count('1'))
