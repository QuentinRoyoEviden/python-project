#!/usr/bin/env python3
import os
import socket
import datetime
os.open("equipements.txt", os.O_CREAT)

with open("equipements.txt", "w") as f:
    f.write("8.8.8.8")

with open("equipements.txt", "r") as f:
    hosts = f.read().splitlines()

for host in hosts:
    def tester_ping(host):
        os.system(f"ping -c 3 {host}")

def verifier_port(host, port):
    """
    she tries to connect to a network port on a specific host and returns the connection code.

    Parameters
    --------------

    host : string
        it is an IP address

    port : integer
        it is a network port (example : 80 SSH, 443 HTTP,...)

    Return
    -------------
    return value is an integer
        return a connection code (0 is good, another is bad)
    """
    try: 
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        resultat = sock.connect_ex((host, port))
        return resultat
    except socket.gaierror:
        return -1

def log(message, fichier):
    """
    she displays a message and writes it to a file

    Parameters
    --------------

    message : string
        it is a text that will be saved

    fichier : string
        it is a file object where message will be written

    Return
    -------------
    return value is a string
        no return
    """
    print(message)
    fichier.write(message + "\n")

ports_a_verifier = [80, 443]
date_heure = datetime.datetime.now().strftime("%Y-%b-%d, %H-%M-%S")
chemin = "/home/qroyo/python_project_1/" 
nom = f"rapport_surveillance_{date_heure}.log"
chemin_nom = os.path.join(chemin, nom)

with open(chemin_nom, "a") as f_rapport:
    for host in hosts:
        if tester_ping(host) == 0:
            log(f"le ping {host} fonctionne", f_rapport)
            for port in ports_a_verifier:
                if verifier_port(host, port) == 0:
                    log(f"le port {port} est ouvert", f_rapport)
                else:
                    log(f"le port {port} est fermé", f_rapport)
        else: 
            log(f"le ping {host} ne fonctionne pas", f_rapport)
