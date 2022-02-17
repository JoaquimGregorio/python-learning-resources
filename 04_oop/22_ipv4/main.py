from classes.calcipv4 import CalcIpv4

calc_ipv4 = CalcIpv4(ip="192.168.100.103", mask="255.255.255.192")

print(calc_ipv4.ip)
print(calc_ipv4.mask)
print(calc_ipv4.net)
print(calc_ipv4.broadcast)
print(calc_ipv4.prefix)
print(calc_ipv4.number_of_ips)
