#!/usr/bin/env python3
import os
import datetime
from utils import test_ping, verify_port, log

def main():
    
    date_time = datetime.datetime.now().strftime("%Y-%b-%d, %H-%M-%S")
    path = "/home/qroyo/python_project_1/"
    filename = f"monitoring_report_{date_time}.log"
    path_name = os.path.join(path, filename)

    with open("equipements.txt", "r") as f:
        hosts = f.read().splitlines() 
        hosts.pop(0)

    with open(path_name, "a") as f_report:
        for host in hosts:
            host_info = host.split(";")
            print("hostname is : ", host_info[0])
            ip = host_info[1]
            port = host_info[4]
            ports_to_verify = [int(item) for item in port.split(",")] 
            if test_ping(ip) == 0:
                for port in ports_to_verify:
                    if verify_port(ip, port) == 0:
                        log(f"the port {port} is open", f_report)
                    else:
                        log(f"the port {port} is closed", f_report)
            else:
                log(f"the ping {ip} doesn't work", f_report)

if __name__ == "__main__":
    main() 
