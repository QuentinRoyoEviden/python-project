#!/usr/bin/env python3
import subprocess
import socket
open("equipements.txt", "a")

with open("equipements.txt", "w") as f:
    f.write("8.8.8.8")

with open("equipements.txt", "r") as f:
    hosts = f.read().splitlines()

def tester_ping(host):
    ping = subprocess.run(["bash", "-c", f"ping -c 1 -W 1 {host}"])
    return ping.returncode

def verifier_port(host, port):
    try: 
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        resultat = sock.connect_ex((host, port))
        return resultat
    except socket.gaierror:
        return -1

ports_a_verifier = [80, 443]

for host in hosts:
    if tester_ping(host) == 0:
        print(f"le ping {host} fonctionne")
        for port in ports_a_verifier:
            if verifier_port(host, port) == 0:
                print(f"le port {port} est ouvert")
            else:
                print(f"le port {port} est fermé")
    else: 
        print(f"le ping {host} ne fonctionne pas")
