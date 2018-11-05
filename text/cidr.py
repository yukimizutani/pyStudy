#!/usr/bin/env python
# python cidr.py 192.168.1.1/24

import struct, socket

input = '/home/yuki/a10/threatlist-tdid_f7539a1b-all-latest.csv'


if __name__ == '__main__':

    (ip, cidr) = '185.153.197.50/32'.split('/')
    cidr = int(cidr)
    host_bits = 32 - cidr
    i = struct.unpack('>I', socket.inet_aton(ip))[0]  # note the endianness
    start = (i >> host_bits) << host_bits  # clear the host bits
    end = start | ((1 << host_bits) - 1)

    # excludes the first and last address in the subnet
    for i in range(start, end):
        print(socket.inet_ntoa(struct.pack('>I', i)))
