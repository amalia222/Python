from ipaddress import *
for i in range(24, 32):
    nv1 = ip_network(f'98.162.78.139/{i}', False)
    nv2 = ip_network(f'98.162.78.154/{i}', False)
    if nv1.network_address != nv2.network_address:
        print(i)