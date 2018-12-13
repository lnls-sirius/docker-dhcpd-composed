#!/usr/bin/python3
from string import Template

t = Template("""
subnet 10.128.${net}.0 netmask 255.255.255.0 {
    range 10.128.${net}.200 10.128.${net}.254;
    option domain-name-servers 10.0.0.71, 10.0.0.72;
    option subnet-mask 255.255.255.0;
    option routers 10.128.${net}.1;
    option broadcast-address 10.128.${net}.255;
    default-lease-time 7200;
    max-lease-time 86400;
}

""")

for net in range(101, 122):
    print(t.safe_substitute(net=net))
