import os
import subprocess
import sys

from fonctions.urlscan import urlScan

import dnsscan
import shodan
import theHarvester
#import urlscan              call api donc pas necessaire




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
            target = input("Enter the target domain: ")
            dnsscan.run(target)
        elif choice == "2":
            query = input("Enter the Shodan query: ")
            api_key = input("Enter your Shodan API key: ")
            shodan.run(api_key, query)
        elif choice == "3":
            query = input("Enter the search query: ")
            target = input("Enter the target domain: ")
            theHarvester.run(query, target)
        elif choice == "4":
            target = input("Enter the target URL: ")
            api_key = input("Enter your urlscan.io API key: ")
            urlScan("google.com")
        else:
            print("Invalid choice")

if __name__ == '__main__':

    menu()
