import json
import requests

def urlScan(adresse, cle ):
    headers = {'API-Key': cle, 'Content-Type': 'application/json'}
    data = {"url": f"{adresse}", "visibility": "public"}
    reponse = requests.post('https://urlscan.io/api/v1/scan/', headers=headers, data=json.dumps(data))
    print(reponse)
    a = reponse.json()
    print(a["result"])

    #3fa78c2b-13a3-4bcd-a6c2-c04d16295e94