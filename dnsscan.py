import argparse
import socket

def dnsScan(target):
    try:
        ip = socket.gethostbyname(target)
        print("IP address for {} is {}".format(target, ip))
    except socket.gaierror as e:
        print("Error resolving {}: {}".format(target, e))

