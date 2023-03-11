
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
        import theHarvester
    except:
        os.system("sudo apt install theHarvester")
        importTheHarvester()
def importUrlScan():
    try:
        import urlscan
    except:
        os.system("sudo apt-get install urlscan")  # uniquement noyaux linux
        importUrlScan()

def verifImport():
    #importDnsScan()
    importShodan()
    importTheHarvester()
    importUrlScan()
    print("imports ok")


"""
    /!\demander clé API shodan/!\ 
"""
#verifImport()