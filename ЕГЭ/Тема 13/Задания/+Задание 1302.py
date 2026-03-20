from ipaddress import *
count = 0
net = ip_network('122.159.136.144/255.255.255.248', False)
for i in net:
    if f'{i:b}'.count('1') % 4 != 0:
        count += 1
print(count)

answer = 5

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(13, 1302, answer, 'e4da3b7fbbce2345d7772b0674a318d5'))