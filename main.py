#!/usr/bin/env python3
import os
import datetime
from utils.py import tester_ping, verifier_port, log

os.open("equipements.txt", os.O_CREAT)

def main():

    with open("equipements.txt", "w") as f:
        f.write("8.8.8.8")

    with open("equipements.txt", "r") as f:
        hosts = f.read().splitlines()

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

if __name__ == "__main__":
    main()
