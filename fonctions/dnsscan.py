import argparse
import socket
from pprint import pprint

import requests


def dnsScan(dns):

    pprint(requests.get(f"https://networkcalc.com/api/dns/lookup/{dns}").json())
    
    
    
   











