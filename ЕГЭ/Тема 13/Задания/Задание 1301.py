from ipaddress import *
min_count = 10 ** 6
for mask in range(32):
    net = ip_network(f'157.220.185.237/{mask}', False)
    if ip_address('157.220.184.230') in net:
        for ip in net:
            count = 0
            if f'{ip:b}'.count('1') == 15:
                count += 1
        if count < min_count:
            min_count = count
print(min_count)

answer = ...

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(13, 1301, answer, '45c48cce2e2d7fbdea1afc51c7c6ad26'))