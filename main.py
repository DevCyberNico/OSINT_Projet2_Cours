from fonctions.urlscan import urlScan
from fonctions.dnsscan import dnsScan
from fonctions.shodan import uShodan
from fonctions.theHarvester import theHarvester

import os
import sys
import shodan
import theHarvester
import requests
import json





def menu():
    while True:
        print("Quel outils d'OSINT voulez-vous utilser ?:")
        print("1. DNS Scan")
        print("2. Shodan")
        print("3. TheHarvester")
        print("4. urlscan.io")
        print("0. Exit")

        choice = input("Enter your choice: ")
        if choice == "0":
            break
        elif choice == "1":
            dns = input("Enter the target domain: ")
            dnsScan(dns)
        elif choice == "2":
            ip = input("Enter the Shodan query: ")
            cle_api = input("Enter your Shodan API key: ")
            uShodan(ip, cle_api)
        elif choice == "3":
            nomDomaine = input("Entrez le nom de domine : ")
            navigateur = input("Entrez le navigateur voulu : ")
            nomFichier = input("Entrez le nom du fichier : ")
            theHarvester(nomDomaine, navigateur, nomFichier)
        elif choice == "4":
            adresse = input("Enter the target URL: ")
            api_key = input("Enter your urlscan.io API key: ")
            urlScan(adresse, api_key)
        else:
            print("Invalid choice")

if __name__ == '__main__':

    menu()
