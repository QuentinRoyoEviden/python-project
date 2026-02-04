#!/usr/bin/env python3
import subprocess
open("equipements.txt", "a")

with open("equipements.txt", "w") as f:
    f.write("8.8.8.8")

with open("equipements.txt", "r") as f:
    hosts = f.read().splitlines()

def tester_hote(host):
    ping = subprocess.run(["bash", "-c", f"ping -c 3 {host}"])
    return ping.returncode

for host in hosts:
     if tester_hote(host) == 0:
        print(f"le ping {host} fonctionne")
     else:
        print(f"le ping {host} ne fonctionne pas")


