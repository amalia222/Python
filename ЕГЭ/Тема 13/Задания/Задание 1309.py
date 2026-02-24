from ipaddress import *
max_count = 0
for mask in range(7, 33):
    net = ip_network(f'130.0.5.80/{mask}', False)
    count = 0
    count1 = f'{net.network_address:b}'.count('1')
    for i in net:
        if f'{i:b}'.count('1') == count1:
            count += 1
    if count > max_count:
        max_count = count
print(max_count)
answer = ...

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(13, 1309, answer, 'da4fb5c6e93e74d3df8527599fa62642'))