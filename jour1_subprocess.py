#!/usr/bin/env python3

import subprocess

ping = subprocess.run(["bash", "-c", "ping -c 3 172.26.42.75"])

print(ping.returncode)

