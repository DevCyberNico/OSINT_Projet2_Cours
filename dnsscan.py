import argparse
import socket

def dnsscan(target):
    try:
        ip = socket.gethostbyname(target)
        print("IP address for {} is {}".format(target, ip))
    except socket.gaierror as e:
        print("Error resolving {}: {}".format(target, e))

"""

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Scan a domain name and return its IP address')
    parser.add_argument('target', help='The domain name to scan')
    args = parser.parse_args()

    dnsscan(args.target)

"""