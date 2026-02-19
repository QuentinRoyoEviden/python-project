# Network Monitor (Network Monitoring Script)

A simple Python script for monitoring the availability of network devices and the status of their critical ports.

The script performs a `ping` test on a defined list of IP addresses, then checks whether specific ports (80 and 443 by default) are open. The results are recorded in a timestamped log file.

##  Features

Connectivity check: Sends ICMP (ping) requests to check if the host is online.
Port scan: Checks the status of specified TCP ports (HTTP/HTTPS by default).
Report generation: Creates a timestamped `.log` file containing detailed results for each check.
Host list management: Reads IP addresses from a text file (equipements.txt).

##  Prerequisites

Python 3 installed on your machine.
Unix/Linux-type operating system (due to the use of the ping -c 3 system command).
Permissions to create files in the log destination directory.

##  Usage

Simply run the script with Python:

python3 script_name.py
~
