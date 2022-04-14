import ipaddress

# ipaddress é um módulo que permite trabalhar com endereços IP

ip = '192.168.0.0/24'

rede = ipaddress.ip_network(ip, strict=False)

for ip in rede:
    print(ip)