import ipaddress   #transforma uma string em um endereço de IP

ip = '192.168.0.1'
endereço = ipaddress.ip_address(ip)

print(endereço)
print(endereço + 100)
print(endereço + 256)
print(endereço + 2000)
print()
ip = '192.168.0.0/24'
redes = ipaddress.ip_network(ip, strict=False)

for ip in redes:
    print(ip)

