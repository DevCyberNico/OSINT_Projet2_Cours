from fonctions.urlscan import urlScan
from fonctions.dnsscan import dnsScan
from fonctions.shodan import uShodan
from fonctions.theHarvester import run_theharvester



def menu():
    while True:
        print("Quel outils d'OSINT voulez-vous utilser ?:")
        print("1. DNS Scan")
        print("2. Shodan")
        print("3. TheHarvester")
        print("4. urlscan.io")
        print("0. Exit")

        choice = input("Entrez votre choix : ")
        if choice == "0":
            break
        elif choice == "1":
            dns = input("Entrez le nom de domaine: ")
            dnsScan(dns)
        elif choice == "2":
            ip = input("Entrez l'adresse ip : ")
            cle_api = input("Enter your Shodan API key: ")
            uShodan(ip, cle_api)
        elif choice == "3":
            domain = input('Entrez le nom de domaine : ')
            navigator = input('Avec quel navigateur ? ')
            output = run_theharvester(domain, navigator)
            filename = f'{domain}.txt'
            #with open(filename, 'w') as f:
             #   f.write(output)
            print(f'Résultats enregsirés dans {filename}')
        elif choice == "4":
            adresse = input("Entrez une URL: ")
            api_key = input("Entrez votre clé API 'urlscan.io' : ")
            urlScan(adresse, api_key)
        else:
            print("Invalid choice")

if __name__ == '__main__':

    menu()
