import os
import sys

"""
def importDnsScan():
    try:
        import dnscan
    except:
        os.system("sudo git clone \"https://github.com/rbsec/dnscan.git\"")
        importDnsScan()
def importShodan():
    try:
        import shodan
    except:
        os.system("sudo pip install shodan")
        importShodan()
def importTheHarvester():
    try:
        import theharvester
    except:
        os.system("sudo apt-get install thearvester")
        importTheHarvester()
def importUrlScan():
    try:
        import urlscan
    except:
        os.system("sudo apt-get install urlscan")  # uniquement noyaux linux
        importUrlScan()

def verifImport():
    importDnsScan()
    importShodan()
    importTheHarvester()
    importUrlScan()
    print("imports ok")
"""


"""
    /!\demander clé API shodan/!\ 
"""
#verifImport()



def menu():
    while True:
        print("Choose an OSINT tool to use:")
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
            theharvester.run(query, target)
        elif choice == "4":
            target = input("Enter the target URL: ")
            api_key = input("Enter your urlscan.io API key: ")
            urlscan.run(api_key, target)
        else:
            print("Invalid choice")

if __name__ == '__main__':
    menu()
