#!/usr/bin/env python3

import platform
import os

ip="140.161.83.8"

if platform.system() == "Windows":
    os_name="Windows"
else:
    os_name="kali"

if os_name.lower() == "windows":
    ping_cmd=f"ping -n 1 -w 2 {ip} > null"
else:
    ping_cmd=f"ping -c 1 -w 2 {ip} > /dev/null 2>&1"

exit_code = os.system(ping_cmd)
print(f"{exit_code} {os_name.split()[0]}")