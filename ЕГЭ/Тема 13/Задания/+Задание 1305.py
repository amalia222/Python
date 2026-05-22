from ipaddress import ip_network
net = ip_network('191.128.66.83/255.192.0.0', 0)
print(net[-2])
answer = 191191255254

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(13, 1305, answer, 'e02030d89e606e5f68c55c7aed0a8e23'))