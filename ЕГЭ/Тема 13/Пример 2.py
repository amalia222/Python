from ipaddress import *
print(ip_network('167.66.136.176/255.254.0.0', False).network_address)