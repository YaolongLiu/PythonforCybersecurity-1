#!/usr/bin/env python3

import platform
import os

ip = "140.161.83.8"
ping_cmd = f"ping -c 1 -w 2 {ip} > /dev/null 2>&1"
exit_code = os.system(ping_cmd)

print(exit_code)

