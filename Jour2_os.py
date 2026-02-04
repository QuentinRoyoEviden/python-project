#!/usr/bin/env python3

import os 

os.open("equipements.txt", os.O_CREAT)
with open("equipements.txt", "w") as f:
    f.write("8.8.8.8")
with open("equipements.txt", "r") as f:
    hosts = f.read().splitlines()
for host in hosts:
    os.system(f"ping -c 3 {host}")
