from pprint import pprint

import requests


def dnsScan(dns):
    resultat = requests.get(f"https://networkcalc.com/api/dns/lookup/{dns}").json()
    pprint(resultat)

    ip = resultat['records']['A'][0]['address']

    print(f"L'adresse ip publique est : {ip} \n"
          f"")
    
    
   











