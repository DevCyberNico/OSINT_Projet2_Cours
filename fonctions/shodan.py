import json
from pprint import pprint

import requests
from shodan import Shodan



def uShodan(ip, cle):

    api = Shodan(cle)                                                                                                   # entree cle api shodan
    resultat = api.host(ip)
    pprint(resultat)                                                                                                    # sortie de l'api après entree ip

    organisme = resultat['org']
    domaine = resultat['domains']





    print(f"L'organisme est : {organisme} \n"
          f"Son domaine est : {domaine} \n"
          f"")
#cle publique type chiffrement














"""
8.8.8.8

Kxbp0POfDddwB2gwaShqaLQXCY2CdJep


"""