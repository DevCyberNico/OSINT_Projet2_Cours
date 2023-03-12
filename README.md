<h1>Menu d'outils d'OSINT</h1>
Ce script Python est un menu interactif permettant à l'utilisateur de choisir des outils d'OSINT (Open Source Intelligence). Les outils disponibles sont le DNS Scan, Shodan, TheHarvester et urlscan.io.

<h2>Prérequis</h2>
Avant d'utiliser ce script, vous devez avoir Python 3 installé sur votre ordinateur. Les bibliothèques externes suivantes doivent également être installées :
<ul>
<li>Requests (pour le DNS Scan et urlscan.io)</li>
<li>Shodan (pour Shodan)</li>
<li>Selenium (pour TheHarvester)</li>
<ul>

<h2>Utilisation</h2>
Pour exécuter le script, ouvrez une invite de commandes ou un terminal, naviguez jusqu'au répertoire contenant le fichier Python, puis exécutez la commande suivante :
```
python menu.py
```  
Le script affichera un menu interactif dans la console. Choisissez une option en entrant le numéro correspondant, puis suivez les instructions à l'écran pour saisir les informations requises. Les résultats seront affichés dans la console ou enregistrés dans un fichier.

<h2>Fonctions</h2>
Le script contient les fonctions suivantes :

<b>dnsScan(dns)</b>
Effectue une recherche de DNS sur un nom de domaine donné à l'aide de l'API DNSDumpster.

<b>uShodan(ip, cle_api)</b>
Effectue une recherche Shodan sur une adresse IP donnée en utilisant l'API Shodan.

<b>run_theharvester(domain, navigator)</b>
Exécute TheHarvester sur un nom de domaine donné à l'aide de Selenium et d'un navigateur web spécifié.

<b>urlScan(adresse, api_key)</b>
Effectue une analyse de sécurité d'une URL donnée à l'aide de l'API urlscan.io.

<h2>Auteur</h2>
Ce script a été écrit par Nicolas FOESSEL, Thibaut GUESDON, Benjamin FRANCISCO. N'hésitez pas à me contacter pour toute question ou suggestion.
