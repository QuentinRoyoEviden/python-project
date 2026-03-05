#!/usr/bin/env python3
import os
import socket

def test_ping(host): 
    """ 
    Retrieve ping output of host

    Parameter
    ---------------
    host : str
        IP address as a string

    Return 
    ---------------
    int 
    return exit of the ping command
    1 is failed
    0 is okay 
    """
    return os.system(f"ping -c 3 {host}")

def verify_port(host, port):
    """
    it tries to connect to a network port on a specific host and returns the connection code.
    
    Parameters
    ---------------
    host : str
        IP address as a string

    port : int
        Network Port (example : SSH 22, HTTPS 443 as a integer

    Return
    ---------------
    int
    return exit of the ping command
    else is failed
    0 is okay
    """
    try: 
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((host, port))
        return result
    except socket.gaierror:
        return -1

def log(message, file):
    """
    it executes a message and writes it to a file

    Parameters
    --------------

    message : string
        it is a text that will be saved

    file : string
        it is a file object where message will be written

    Return
    -------------
    return value is a string
        no return
    """
    print(message)
    file.write(message + "\n")
