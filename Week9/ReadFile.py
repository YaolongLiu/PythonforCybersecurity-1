#!/usr/bin/env python3

ip_file=open("ips.txt", "r")

# ip_address = ip_file.read()
for line in ip_file:
    if line.startswith("192."):
        print(line)

# print(ip_address)

ip_file.close()


#with could automatically close when we finish reading it.
with open("ips.txt", "r") as ip_file:
    print(ip_file.read())