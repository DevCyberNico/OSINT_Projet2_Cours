import dnsscan
import shodan
import theharvester
import urlscan

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