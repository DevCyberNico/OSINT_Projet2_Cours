import json
from pprint import pprint

import requests
from shodan import Shodan



def uShodan(ip, cle):

    api = Shodan(cle)                                                                                                   # entree cle api shodan
    resultat = api.host(ip)
    #pprint(resultat)                                                                                                    # sortie de l'api après entree ip


    fichier = open(f"shodan.json", "w")
    json.dump(resultat, fichier, indent=4)
    fichier.close()




    organisme = resultat['org']
    domaine = resultat['domains']
    ports = resultat['ports']
    pays = resultat['country_name']
    clePublique = resultat['data'][2]['ssl']['cert']['pubkey']







    print(f"Pour voir toutes les données, ouvrir le fichier shodan.json \n"
          f"L'organisme est : {organisme} \n"
          f"Son domaine est : {domaine} \n"
          f"ports ouverts : {ports} \n"
          f"Pays : {pays} \n"
          f"Clé publique : {clePublique['bits']}, {clePublique['type']} \n")
#cle publique type chiffrement














"""
8.8.8.8

Kxbp0POfDddwB2gwaShqaLQXCY2CdJep


"""