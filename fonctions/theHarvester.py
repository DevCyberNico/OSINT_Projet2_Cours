#   theharvester -d {nomDomaine} -l 200 -b {navigateur} -f {nomFichier}

import os
import platform


def theHarvester():
    nomDomaine = input("Entrez le nom de domaine : \n ")
    navigateur = input("Entrez le navigateur désiré : \n")
    nomFichier = input("Entrez le nom du fichier : \n")

    print(os.system(f"theHarvester -d {nomDomaine} -l 200 -b {navigateur} -f {nomFichier}"))








