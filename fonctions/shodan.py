import json
from pprint import pprint

import requests
from shodan import Shodan



def shodan(ip, cle):

    api = Shodan(cle)                                                                                                   # entree cle api shodan
    resultat = api.host(ip)

    pprint(resultat)                                                                                                    # sortie de l'api après entree ip

    organisme = resultat['org']
    print(f"L'organisme est : {organisme}")















"""
8.8.8.8

Kxbp0POfDddwB2gwaShqaLQXCY2CdJep


"""