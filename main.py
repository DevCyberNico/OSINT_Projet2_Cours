from fonctions.urlscan import urlScan
from fonctions.dnsscan import dnsScan
from fonctions.shodan import uShodan
from fonctions.theHarvester import run_theharvester

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
            domain = input('Insérez le domaine cible : ')
            navigator = input ('Avec quel navigateur ? ')
            output = run_theharvester(domain, navigator)
            filename = f'{domain}.txt'
            with open(filename, 'w') as f:
                f.write(output)
            print(f'Résultats enregsirés dans {filename}')
        elif choice == "4":
            adresse = input("Enter the target URL: ")
            api_key = input("Enter your urlscan.io API key: ")
            urlScan(adresse, api_key)
        else:
            print("Invalid choice")

if __name__ == '__main__':

    menu()
