from ipaddress import ip_network
net = ip_network('205.182.128.0/255.255.192.0', 0)
count = 0
for i in net:
    if f'{i:b}'[16:24].count('1') == f'{i:b}'[16:24].count('0'):
        count += 1
print(count)
answer = 5120

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(13, 1306, answer, '6aadca7bd86c4743e6724f9607256126'))