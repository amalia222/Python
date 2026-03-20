from ipaddress import *
s = []
for mask in range(32, 10, -1):
    net = ip_network(f'147.222.199.75/{mask}', False)
    if ip_address('147.222.222.147') in net:
        count = 0
        for i in net:
            if f'{i:b}'.count('1') == 14:
                count += 1
        s.append(count)
print(min(s))


answer = 78

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(13, 1303, answer, '35f4a8d465e6e1edc05f3d8ab658c551'))